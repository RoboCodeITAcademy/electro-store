from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'account'

urlpatterns = [
    path("login/", LoginView.as_view(template_name="account/login.html", success_url="/"),name="login"),
    path("logout/", LogoutView.as_view(template_name="account/logout.html"),name="logout"),
    path("register/", views.register, name='register'),
]