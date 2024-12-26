from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .models import Product
from core.models import Gender, Category


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        # Проверяем, есть ли параметр type_name
        type_name = self.kwargs.get("type_name", None)
        if type_name:
            # Если type_name указан, фильтруем продукты по гендеру
            gender = get_object_or_404(Gender, name=type_name)
            return Product.objects.filter(gender=gender)
        # Если type_name нет, возвращаем все продукты
        return Product.objects.all()


class CategoryProductListView(ListView):
    model = Product
    template_name = "products/category_product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        # Получаем параметры type_name и category_name
        type_name = self.kwargs.get("type_name")
        category_name = self.kwargs.get("category_name")

        # Проверка наличия типа (gender) и категории
        gender = get_object_or_404(Gender, name=type_name)
        category = get_object_or_404(Category, name=category_name)

        # Фильтруем продукты по гендеру и категории
        return Product.objects.filter(gender=gender, category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type_name = self.kwargs.get("type_name")
        category_name = self.kwargs.get("category_name")
        context['type_name'] = type_name
        context['category_name'] = category_name
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"  # Убедитесь, что такой шаблон существует
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    template_name = "products/product_update.html"
    success_url = reverse_lazy('products:product_list')

class ContactView(TemplateView):
    template_name = 'contacts.html'

class AboutUsView(TemplateView):
    template_name = 'about_us.html'