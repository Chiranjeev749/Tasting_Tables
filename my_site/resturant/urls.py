from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('home/', views.home, name='home'),
    path('book-table/<int:restaurant_id>/', views.book_table, name='book_table'),
    path('view-menu/<int:restaurant_id>/', views.view_menu, name='view_menu'),
]
