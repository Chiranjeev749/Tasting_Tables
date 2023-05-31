from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

type = [
    ('veg', 'veg'),
    ('non-veg', 'non-veg')
]

class Restaurant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=10, null=True, choices=type, default='non-veg')
    email = models.CharField(max_length=100, null=False)
    phoneNo = models.CharField(max_length=10, null=False, default='')
    address = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=30, null=False)
    pin = models.CharField(max_length=10,default=0)
    opening_time = models.TimeField(default=datetime.time(10, 0))
    closing_time = models.TimeField(default=datetime.time(22, 0))
    

class Image(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    img1 = models.ImageField(upload_to='image/', null=False, default='')
    img2 = models.ImageField(upload_to='image/', null=True, default='', blank=True)
    img3 = models.ImageField(upload_to='image/', null=True, default='', blank=True)
    img4 = models.ImageField(upload_to='image/', null=True, default='', blank=True)

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu1 = models.ImageField(upload_to='menu/', null=True, blank=True, default='')
    menu2 = models.ImageField(upload_to='menu/', null=True, default='', blank=True)
    menu3 = models.ImageField(upload_to='menu/', null=True, default='', blank=True)
    menu4 = models.ImageField(upload_to='menu/', null=True, default='', blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=False, blank=False, default='')
    pin = models.IntegerField(null=False, blank=False, default=0)
    city = models.CharField(max_length=20, null=False, blank=False, default='')
    state = models.CharField(max_length=20, null=False, blank=False, default='')
    phoneNo = models.CharField(max_length=10, null=False, blank=False, default='')
    time_start_of_user = models.DateTimeField(auto_now=True)

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name_of_table = models.CharField(max_length=30, default='standard')
    number_of_table = models.IntegerField(default=10)
    capacity_per_table = models.IntegerField(default=5)
    price_per_table = models.IntegerField(null=True, default=100)

class Reservation(models.Model):
    table = models.OneToOneField(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    num_guests = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

