from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Usuario(models.Model):
    # user information data
    user_name = models.CharField(max_length=128, null=False, blank=False)
    user_name_max_length = user_name.max_length
    user_last_name = models.CharField(max_length=128, null=False, blank=False)
    user_lane_name_max_length = user_last_name.max_length
    user_birthday = models.CharField(max_length=20, null=False, blank=False)
    user_cellphone_number = models.CharField(max_length=15)
    user_habilities = models.CharField(max_length=300)
    user_usuario = models.OneToOneField(User, related_name="usuario_relacionado", on_delete='Cascade')

    @property
    def email(self):
        return self.user_usuario.email

    # user logon data
    # user_email = models.EmailField(max_length=128)
    # user_password = models.CharField(max_length=128, null=False)

    class Meta:
        ordering = ('user_name',)

    def __str__(self):
        return self.user_name
