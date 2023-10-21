from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newitem/', views.newitem, name='newitem'),
    path('message/', views.message, name='message'),
    path('cart/', views.cart, name='cart'),
]