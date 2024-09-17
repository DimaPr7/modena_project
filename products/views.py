from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import TemplateView
from core.models import Category
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"


class TrousersListView(ListView):
    model = Product
    template_name = "products/trousers_list.html"

    def get_queryset(self):
        try:
            trousers_category = Category.objects.get(name='Штаны')
        except Category.DoesNotExist:
            trousers_category = None
        return Product.objects.filter(category=trousers_category) if trousers_category else Product.objects.none()


class TShortsListView(ListView):
    model = Product
    template_name = "products/t-shorts_list.html"

    def get_queryset(self):
        try:
            tshorts_category = Category.objects.get(name='Рубашкa')
        except Category.DoesNotExist:
            tshorts_category = None
        return Product.objects.filter(category=tshorts_category) if tshorts_category else Product.objects.none()


class ContactView(TemplateView):
    template_name = 'products/contacts.html'


class AboutUsView(TemplateView):
    template_name = 'products/about_us.html'
