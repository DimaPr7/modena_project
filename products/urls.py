from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    CategoryProductListView,
)

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('<str:type_name>/', ProductListView.as_view(), name='type_products'),
    path('<str:type_name>/<str:category_name>/', CategoryProductListView.as_view(), name='type_category_products'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
]
