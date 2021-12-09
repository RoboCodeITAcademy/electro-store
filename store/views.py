from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(TemplateView, LoginRequiredMixin):
    template_name = 'index.html'

def contact(request):
    return render(request, "blank.html")