from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('drinks/<str:drink_name>', views.drinks, name='drinks'),
    path('book/', views.book, name='book'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
]
