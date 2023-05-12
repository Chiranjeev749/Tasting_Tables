from django.contrib import admin
from .models import *

class RestaurantAdmin(admin.ModelAdmin):
    pass

class MenuAdmin(admin.ModelAdmin):
    pass

class TimeSlotAdmin(admin.ModelAdmin):
    pass

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(MenuItem, MenuAdmin)
admin.site.register(TimeSlot, TimeSlotAdmin)