from django.urls import path
from . import views

app_name = 'ctsp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('welcome/', views.ProjectWelcomeView.as_view(), name='project_welcome'),
]
