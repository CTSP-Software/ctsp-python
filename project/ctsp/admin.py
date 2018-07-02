from django.contrib import admin
from ctsp.models import Project

# Register your models here.

'''
This module contains the application <app_url>/admin/ configuration
To learn more about the ModelAdmin class refer to: https://docs.djangoproject.com/en/2.0/ref/contrib/admin/
'''


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Category Information", {"fields": [
            'id', "name", 'start_date', 'final_date']}),
    ]
    list_display = ('id', "name", 'start_date', 'final_date')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', "project_name",
                    'project_start_date', 'project_final_date')


admin.site.register(Project, ProjectAdmin)
