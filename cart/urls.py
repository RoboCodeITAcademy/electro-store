from django.urls import path
from .import views

app_name = 'cart'
    
urlpatterns = [
    path('', views.cartView, name='cart'),
    path("checkout/", views.checkout, name='checkout'),
    path('add/', views.addToCart , name='add'),
    path('remove/', views.removeCartItems , name='removeAllItems'),
    path('<int:product_id>/<int:qty>/delete', views.deleteCartItem , name='delete'),
    ]