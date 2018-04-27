from django.contrib import admin

# Register your models here.
from .models import Projeto, MembrosDoTime

admin.site.register(Projeto)
admin.site.register(MembrosDoTime)
