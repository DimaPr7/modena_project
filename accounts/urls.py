from django.urls import path
from . import views
from .views import AccountView

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', AccountView.as_view(), name='account_profile'),
    path('account/update/', views.profile_update, name='account_update'),
]
