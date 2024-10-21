from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product


class HomePageView(ListView):
    model = Product
    template_name = "home.html"

