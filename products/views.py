from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView
from django.views.generic import TemplateView
from core.models import Category
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"


class CategoryProductListView(ListView):
    model = Product
    template_name = "products/category_product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        category_name = self.kwargs.get("category_name")
        category = get_object_or_404(Category, name=category_name)
        return Product.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs.get("category_name")
        context['category_name'] = category_name
        return context


class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    template_name = "products/product_update.html"
    success_url = reverse_lazy('products:product_list')


class ContactView(TemplateView):
    template_name = 'contacts.html'


class AboutUsView(TemplateView):
    template_name = 'about_us.html'
