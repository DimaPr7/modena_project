from django.contrib import admin
from django.urls import path, include
from .views import ProductDetailView, ProductListView, TrousersListView, TShortsListView

urlpatterns = [
    path("detail/<int:pk>/", ProductDetailView.as_view(), name="detail"),
    path("list/", ProductListView.as_view(), name="list"),
    path("trousers/", TrousersListView.as_view(), name="trousers"),
    path("t-shorts/", TShortsListView.as_view(), name="t-shorts"),
]

