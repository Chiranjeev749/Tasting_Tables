from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as auth_logout, login
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime,json
from .models import Restaurant,Image, Profile, Table, Reservation,Menu


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    restaurants = Restaurant.objects.all()
    search_item = request.GET.get("search")

    if search_item:
        res_match = restaurants.filter(name__icontains=search_item)
        if not res_match.exists():
            messages.error(request, 'No restaurants available with that name')
            res_match = restaurants
    else:
        res_match = restaurants

    context = {
        'restaurant': res_match
    }
    return render(request, 'home.html', context=context)


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        phoneNo = request.POST['phoneNo']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            profile = Profile.objects.create(user=user, address=address, state=state, city=city, pin=pin, phoneNo=phoneNo)
            messages.success(request, "User created successfully")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Failed to create user: {str(e)}")
            return redirect('signup')
    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_path = request.GET.get('next') or 'home'
            return redirect(redirect_path)
        else:
            return redirect('user_login')
    return render(request, 'login.html')

def user_logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out successfully.")
    request.session.flush()  # Clear the session
    redirect_path = request.GET.get('next') or 'home'
    return redirect(redirect_path)

@login_required(login_url='user_login')
def restaurant_info(request):
    existing_restaurant = Restaurant.objects.filter(user=request.user).first()
    if existing_restaurant:
        return redirect('table_info', restaurant_id=existing_restaurant.id)
    
    if request.method == "POST":
        try:
            res_name = request.POST['name']
            res_type = request.POST['type']
            res_address = request.POST['address']
            res_city = request.POST['city']
            res_state = request.POST['state']
            res_pin = request.POST['pin']
            res_email = request.POST['email']
            res_phoneNo = request.POST['phoneNo']
            res_opening = request.POST['opening_time']
            res_closing = request.POST['closing_time']

            restaurant, created = Restaurant.objects.get_or_create(
                user=request.user,
                defaults={
                    'name': res_name,
                    'type': res_type,
                    'address': res_address,
                    'city': res_city,
                    'state': res_state,
                    'pin': res_pin,
                    'email': res_email,
                    'phoneNo': res_phoneNo,
                    'opening_time': res_opening,
                    'closing_time': res_closing
                }
            )

            image = Image.objects.create(
                restaurant=restaurant,
                img1=request.FILES.get('img1'),
                img2=request.FILES.get('img2'),
                img3=request.FILES.get('img3'),
                img4=request.FILES.get('img4')
            )

            menu = Menu.objects.create(
                restaurant=restaurant,
                menu1=request.FILES.get('menu1'),
                menu2=request.FILES.get('menu2'),
                menu3=request.FILES.get('menu3'),
                menu4=request.FILES.get('menu4')
            )

            return redirect('table_info', restaurant_id=restaurant.id)
        except Exception as e:
            print("Unsuccessful:", e)
    else:
        print("POST method problem")

    return render(request, 'resturant_info.html')

@login_required(login_url='user_login')
def table_info(request,restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    if request.method == 'POST' and request.is_ajax:
        entries = json.loads(request.body)
        try:
            for entry in entries:
                table = Table.objects.create(
                    restaurant = restaurant,
                    name_of_table = entry['name'],
                    capacity_per_table = entry['count'],
                    number_of_table = entry['number'],
                    price_per_table = entry['price']
                )
            return JsonResponse({'success':True})
        except Exception as e:
            return JsonResponse({'success':False,'message':str(e)})
    
    return JsonResponse({'success':False,'message':'Invalid Request'})

from django.db import IntegrityError

@login_required(login_url='user_login')
def book_table(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    try:
        table = restaurant.table
    except Table.DoesNotExist:
        table = Table.objects.create(restaurant=restaurant)
    
    opening_time = restaurant.opening_time
    closing_time = restaurant.closing_time
    time_slots = generate_time_slots(opening_time, closing_time)

    if request.method == 'POST':
        date = request.POST.get('date')
        time_slot = request.POST.get('time_slot')
        num_guests = int(request.POST.get('num_guests'))
        

        # Check if the selected time slot is available
        available_time_slots = time_slot
        if time_slot in available_time_slots and available_time_slots[time_slot]:
            available_time_slots[time_slot] = False
            table.available_time_slots = available_time_slots
            table.save()

            # Check if there is an existing reservation for the table
            try:
                reservation = Reservation.objects.get(table=table)
                # If a reservation exists, update it
                reservation.date = date
                reservation.time_slot = time_slot
                reservation.num_guests = num_guests
                reservation.save()
            except IntegrityError:
                # If no reservation exists, create a new one
                reservation = Reservation.objects.create(
                    table=table,
                    date=date,
                    time_slot=time_slot,
                    num_guests=num_guests,
                    user=request.user
                )

            return redirect('success_page')
        else:
            return redirect('unavailable_page')

   

    context = {
        'restaurant': restaurant,
        'time_slots': time_slots
    }
    return render(request, 'book_table.html', context=context)


def generate_time_slots(opening_time, closing_time, interval_minutes=60):
    time_slots = []
    current_time = datetime.datetime.combine(datetime.date.today(), opening_time)
    end_time = datetime.datetime.combine(datetime.date.today(), closing_time)
    interval = datetime.timedelta(minutes=interval_minutes)

    while current_time < end_time:
        end_slot_time = current_time + interval
        time_slot = f"{current_time.strftime('%H:%M')} - {end_slot_time.strftime('%H:%M')}"
        time_slots.append(time_slot)
        current_time = end_slot_time

    return time_slots

