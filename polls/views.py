from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'templates/polls/index.php')
    #../front-end/html/ProjectsPage.html

def create_project(request):
	return HttpResponse("Criar projeto")

def import_project(request, id_projeto):
	return HttpResponse("Importar projeto %s" % id_projeto)

def project_setup(request, id_projeto):
	return HttpResponse("Editar projeto %s" % id_projeto)