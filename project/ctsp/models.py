from django.db import models
import datetime
from django.utils import timezone
from django.core.validators import RegexValidator


# Create your models here.

'''
This package creates our Project model, which is the essential definition of our table fields and behaviour.
To learn more about MySQL database modeling refer to: https://dev.mysql.com/doc/workbench/en/wb-getting-started-tutorial-creating-a-model.html
To learn more about Django database models refer to: https://docs.djangoproject.com/en/2.0/topics/db/models/
'''


class User(models.Model):
    # user information data
    user_name = models.CharField(max_length=128, null=False, blank=False)
    user_name_max_length = user_name.max_length
    user_last_name = models.CharField(max_length=128, null=False, blank=False)
    user_lane_name_max_length = user_last_name.max_length
    user_birthday = models.DateField(null=False, blank=False)
    user_cellphone_regex = RegexValidator(
        regex=r"^\+\d{2}\s\d{2}\s\d{9,12}$", message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    user_cellphone_number = models.CharField(
        validators=[user_cellphone_regex], max_length=15)
    user_habilities = models.TextField(max_length=300)

    # user logon data
    user_email = models.EmailField(max_length=128)
    user_password = models.CharField(max_length=128, null=False)

    class Meta:
        ordering = ('user_name',)

    def __str__(self):
        return self.user_name


class Project(models.Model):
    # project information
    project_name = models.CharField(max_length=128, null=False, blank=False)
    project_name_max_length = project_name.max_length
    project_start_date = models.DateField(
        default=timezone.now, null=False, blank=False)
    project_final_date = models.DateField(
        default=timezone.now, null=False, blank=False)

    # project relation
    project_members = models.ManyToManyField(User)

    class Meta:
        ordering = ('project_name',)

    def __str__(self):
        return self.project_name


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
