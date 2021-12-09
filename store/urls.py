from django.urls import  path
from . import views

app_name = 'store'

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("contact/", views.contact, name='contact'),

]