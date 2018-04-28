from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('criar_projeto/', views.create_project, name='criar projeto'),
    path('<int:id_projeto>/importar/', views.import_project, name='importar_projeto'),
    path('<int:id_projeto>/editar/', views.project_setup, name='editar_projeto'),
]
