from django.db import models

# Create your models here.
class Projeto(models.Model):
	id_projeto = models.AutoField(primary_key=True)
	nome_projeto = models.CharField(max_length=30, blank=False)
	membros_projeto = models.CharField(max_length=30, blank=True)

class MembrosDoTime(models.Model):
	id_membro = models.AutoField(primary_key=True)
	nome_membro = models.CharField(max_length=30, blank=False)
	idProjeto_membro = models.ForeignKey(
		'Projeto',
		on_delete=models.CASCADE,
	)
