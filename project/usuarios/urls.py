from django.urls import path
from . import views
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    path('register_user/', views.RegisterUser.as_view(), name='register_user'),
    path('', login, {'template_name': 'login.html'}, name='login'),
    path('logout/', logout_then_login, {'login_url': ''}, name='logout')
]