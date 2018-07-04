from django.urls import path
from . import views
from django.contrib.auth.views import login, logout_then_login
app_name = 'ctsp'


'''
This module provides all our ctsp application urls.
Direct accesses and redirects needs to pass here.
To learn more about the django urls refer to: https://docs.djangoproject.com/en/2.0/ref/urls/
'''

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('welcome/', views.CreateProjectView.as_view(), name='create_project'),
    path('welcome/<int:pk>/', views.WelcomeProjectView.as_view(), name='project_welcome'),
    path('create_pbacklog/<int:pk>/', views.CreatePbacklogView.as_view(), name='create_pbacklog'),
    path('create_sprint/<int:pk>/', views.CreateSprintView.as_view(), name='create_sprint'),
    path('assign_members/<int:pk>/', views.AssignMembersView.as_view(), name='assign_members'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('create_members/<int:pk>/', views.CreateMembers.as_view(), name='create_members'),
    path('register_user/', views.RegisterUser.as_view(), name='register_user'),
    path('login/', login, {'template_name': 'ctsp/login.html'}, name='login'),
    path('logout/', logout_then_login, {'login_url': '/login/'}, name='logout')
]
