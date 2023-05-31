from django.contrib import admin
from .models import Restaurant,Image,Profile,Table,Reservation,Menu

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Menu)