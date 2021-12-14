from django.urls import path
from .import views

app_name = 'cart'
urlpatterns = [
    path('', views.cartView, name='cart'),
    path('add/', views.addToCart , name='add'),
    ]