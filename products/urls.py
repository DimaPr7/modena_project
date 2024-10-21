from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import ProductDetailView, ProductListView, CategoryProductListView, ProductUpdateView

app_name = 'products'

urlpatterns = [
    path("detail/<int:pk>/", ProductDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="update"),
    path("list/", ProductListView.as_view(), name="product_list"),
    path('<str:category_name>/', CategoryProductListView.as_view(), name='category_products'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
