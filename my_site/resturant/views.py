from django.shortcuts import render, get_object_or_404
from .models import Restaurant, TimeSlot, MenuItem

def index(request):
    return render(request,'index.html')

def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})

def book_table(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    time_slots = TimeSlot.objects.filter(restaurant=restaurant)
    return render(request, 'book_table.html', {'restaurant': restaurant, 'time_slots': time_slots})

def view_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    menu_items = MenuItem.objects.filter(restaurant=restaurant)
    return render(request, 'view_menu.html', {'restaurant': restaurant, 'menu_items': menu_items})
