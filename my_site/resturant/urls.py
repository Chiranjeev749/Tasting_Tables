from django.urls import path 
from . import views


urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('home/',views.home,name = 'home'),
    path('signup/',views.signup,name = 'signup'),
    path('login/',views.user_login,name = 'user_login'),
    path('logout/',views.user_logout,name = 'user_logout'),
    path('resturant_info/',views.restaurant_info,name = 'resturant_info'),
    path('table_info/<int:restaurant_id>',views.table_info,name = 'table_info'),
    path('book_table/<int:restaurant_id>/',views.book_table,name = 'book_table'),
]