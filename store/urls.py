from django.urls import  path
from . import views

app_name = 'store'

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    # path("<int:pk>/detail/", views.ProductDetailView.as_view(), name='detail')
    path("<int:p_id>/detail/", views.detail, name='detail')

]