from django.db import models
import datetime
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from usuarios.models import Usuario
from .models import Project

# Create your models here.

'''
This package creates our Project model, which is the essential definition of our table fields and behaviour.
To learn more about MySQL database modeling refer to: https://dev.mysql.com/doc/workbench/en/wb-getting-started-tutorial-creating-a-model.html
To learn more about Django database models refer to: https://docs.djangoproject.com/en/2.0/topics/db/models/
'''


class Papel(models.model):
    nome_papel = models.CharField(max_length=128)
    usuario_designado = models.ForeignKey(Usuario)
    projeto_designado = models.ForeignKey(Project)


class Project(models.Model):
    # project information
    project_name = models.CharField(max_length=128, null=False, blank=False)
    project_name_max_length = project_name.max_length
    project_start_date = models.DateField(default=timezone.now, null=False, blank=False)
    project_final_date = models.DateField(default=timezone.now, null=False, blank=False)
    project_members = models.ManyToManyField(Usuario, related_name='projetos_atuais')

    # project relation
    # project_members = models.ManyToManyField(User)

    class Meta:
        ordering = ('project_name',)

    def __str__(self):
        return self.project_name


# class MembroDoTime(models.Model):
#         # este ID provávelmente não precisa pois o django criar um ID automático de inteiro para sua base de dados
#     membroDoTime_id = models.IntegerField(primary_key=True)
#     membroDoTime_project = models.ForeignKey(
#         'project_name', on_delete=models.CASCADE)
#     membroDoTime_email = models.ForeignKey(
#         'usuario_email', on_delete=models.CASCADE)
#     membroDoTime_cargos = models.CharField(max_length=50, null=False)
