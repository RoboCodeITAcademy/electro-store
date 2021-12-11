from django.shortcuts import render
# from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product

# Create your views here.

class HomeView(ListView, LoginRequiredMixin):
    model = Product
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["starCount"] = range(8)
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
