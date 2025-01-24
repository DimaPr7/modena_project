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
        queryset = Product.objects.all()
        search_query = self.request.GET.get('q')
        if search_query:
            search_terms = search_query.split()
            for term in search_terms:
                queryset = queryset.filter(name__icontains=term)
        return queryset


class ProductCategoryListView(ListView):
    model = Product
    template_name = "products/category_product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        category_name = self.kwargs.get("category_name", None)
        if category_name:
            category_name = get_object_or_404(Category, name=category_name)
            return Product.objects.filter(category=category_name)
        return Product.objects.all()


class ProductCategoryTypeListView(ListView):
    model = Product
    template_name = "products/category_product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        type_name = self.kwargs.get("type_name")
        category_name = self.kwargs.get("category_name")
        gender = get_object_or_404(Gender, name=type_name)
        category = get_object_or_404(Category, name=category_name)
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
    template_name = "products/product_detail.html"
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    template_name = "products/product_update.html"

    def get_success_url(self):
        return reverse_lazy('products:detail', kwargs={'pk': self.object.pk})


class ContactView(TemplateView):
    template_name = 'contacts.html'


class AboutUsView(TemplateView):
    template_name = 'about_us.html'
