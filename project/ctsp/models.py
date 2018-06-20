from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    '''
    This class creates our Project model, which is the essential definition of our table fields and behaviour.
    To learn more about MySQL database modeling refer to: https://dev.mysql.com/doc/workbench/en/wb-getting-started-tutorial-creating-a-model.html
    To learn more about Django database models refer to: https://docs.djangoproject.com/en/2.0/topics/db/models/
    '''

    project_name = models.CharField(max_length=128, null=False)
    project_name_max_length = project_name.max_length
    project_start_date = models.DateField(default=timezone.now, null=True)
    project_final_date = models.DateField(default=timezone.now, null=True)

    def _str_(self):
        return self.project_name_max_length


# class Usuario(models.Model):
#     usuario_name = models.CharField(max_length=30, null=False)
#     usuario_name_max_length = usuario_name.max_length
#     usuario_sobrename = models.CharField(max_length=100, null=False)
#     usuario_sobrename_max_length = usuario_sobrename.max_length
#     usuario_nascimento = models.DateField(default=timezone.now, null=True)
#     usuario_telefone = models.CharField(
#         'Telefone para Contato', max_length=13, blank=True, null=True)
#     usuario_habilidades = models.CharField(max_length=300, null=True)
#     usuario_email = models.CharField(max_length=50, null=False)
#     usuario_senha = models.CharField(
#         max_length=100, null=False, primary_key=True)
#     usuario_membroId = models.ForeignKey(
#         'membroDoTime_id', on_delete=models.CASCADE)

#     def _str_(self):
#         return self.usuario_email_max_length


# class MembroDoTime(models.Model):
#         # este ID provávelmente não precisa pois o django criar um ID automático de inteiro para sua base de dados
#     membroDoTime_id = models.IntegerField(primary_key=True)
#     membroDoTime_project = models.ForeignKey(
#         'project_name', on_delete=models.CASCADE)
#     membroDoTime_email = models.ForeignKey(
#         'usuario_email', on_delete=models.CASCADE)
#     membroDoTime_cargos = models.CharField(max_length=50, null=False)
