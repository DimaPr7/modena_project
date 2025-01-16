from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductCategoryTypeListView,
    ProductCategoryListView,
)

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('<str:category_name>/', ProductCategoryListView.as_view(), name='category_products'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('<str:type_name>/<str:category_name>/', ProductCategoryTypeListView.as_view(), name='type_category_products'),
]
