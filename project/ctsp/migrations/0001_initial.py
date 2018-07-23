# Generated by Django 2.0.7 on 2018-07-22 23:59

import ctsp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=128)),
                ('project_start_date', models.DateField(default=django.utils.timezone.now)),
                ('project_final_date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('project_name',),
            },
        ),
        migrations.CreateModel(
            name='US',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('us_title', models.CharField(max_length=128)),
                ('us_estimative', models.IntegerField()),
                ('us_type', models.CharField(choices=[(ctsp.models.USType('User Story'), 'User Story'), (ctsp.models.USType('Epic'), 'Epic'), (ctsp.models.USType('Theme'), 'Theme')], max_length=2)),
                ('us_priority', models.CharField(choices=[(ctsp.models.USPriority('High'), 'High'), (ctsp.models.USPriority('Medium'), 'Medium'), (ctsp.models.USPriority('Low'), 'Low')], max_length=1)),
                ('us_description', models.TextField(max_length=2144)),
                ('us_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctsp.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=128)),
                ('user_last_name', models.CharField(max_length=128)),
                ('user_birthday', models.CharField(max_length=20)),
                ('user_cellphone_number', models.CharField(max_length=15)),
                ('user_habilities', models.CharField(max_length=300)),
                ('user_usuario', models.OneToOneField(on_delete='Cascade', related_name='usuario_relacionado', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user_name',),
            },
        ),
    ]
