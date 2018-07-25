from django.db import models
import datetime
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.

'''
This package creates our Project model, which is the essential definition of our table fields and behaviour.
To learn more about MySQL database modeling refer to: https://dev.mysql.com/doc/workbench/en/wb-getting-started-tutorial-creating-a-model.html
To learn more about Django database models refer to: https://docs.djangoproject.com/en/2.0/topics/db/models/
'''


class Usuario(models.Model):
    # user information data
    user_name = models.CharField(max_length=128, null=False, blank=False)
    user_name_max_length = user_name.max_length
    user_last_name = models.CharField(max_length=128, null=False, blank=False)
    user_lane_name_max_length = user_last_name.max_length
    user_birthday = models.CharField(max_length=20, null=False, blank=False)
    user_cellphone_number = models.CharField(max_length=15)
    user_habilities = models.CharField(max_length=300)
    user_usuario = models.OneToOneField(
        User, related_name="usuario_relacionado", on_delete='Cascade')

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


class Project(models.Model):
    # project information
    project_name = models.CharField(max_length=128, null=False, blank=False)
    project_name_max_length = project_name.max_length
    project_start_date = models.DateField(
        default=timezone.now, null=False, blank=False)
    project_final_date = models.DateField(
        default=timezone.now, null=False, blank=False)

    # project relation
    # project_members = models.ManyToManyField(User)

    class Meta:
        ordering = ('project_name',)

    def __str__(self):
        return self.project_name


class US(models.Model):
    USER_STORY = "US"
    EPIC = "EP"
    THEME = "TH"
    us_type_choices = ((USER_STORY, "User Story"), (EPIC, "Epic"), (THEME, "Theme"))

    HIGH = "H"
    MEDIUM = "M"
    LOW = "L"
    us_priority_choices = ((HIGH, "High"), (MEDIUM, "Medium"), (LOW, "Low"))

    # US fields
    us_project = models.ForeignKey(
        Project, on_delete=models.CASCADE)  # many US to one Project

    us_title = models.CharField(max_length=128, null=False, blank=False)
    us_title_max_length = us_title.max_length

    us_estimative = models.PositiveIntegerField(null=False, blank=False)

    us_type = models.CharField(max_length=2, null=False, blank=False, choices=us_type_choices, default=USER_STORY)

    us_priority = models.CharField(max_length=1, null=False, blank=False, choices=us_priority_choices, default=HIGH)

    us_description = models.TextField(max_length=2144, null=False, blank=False)
    us_description_max_length = us_description.max_length

    us_acceptance = models.TextField(max_length=2144, null=False, blank=False)
    us_acceptance_max_length = us_acceptance.max_length