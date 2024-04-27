# Generated by Django 5.0.4 on 2024-04-21 00:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_project', models.CharField(max_length=50, verbose_name='Название')),
                ('specification_project', models.TextField(verbose_name='ТЗ')),
                ('deadline_project', models.DateField(verbose_name='Дедлайн')),
                ('file_project', models.FileField(blank=True, null=True, upload_to='file/project/', verbose_name='Документ')),
                ('date_project', models.DateTimeField(verbose_name='Дата создания')),
                ('status_project', models.CharField(blank=True, max_length=20, null=True, verbose_name='Стаутс')),
                ('author_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_project', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('performer_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfomer_project', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_task', models.CharField(max_length=50, verbose_name='Название')),
                ('task', models.TextField(verbose_name='Задача')),
                ('deadline_task', models.DateField(verbose_name='Дедлайн')),
                ('file_task', models.FileField(blank=True, null=True, upload_to='file/task/', verbose_name='Документ')),
                ('date_task', models.DateTimeField(verbose_name='Дата создания')),
                ('status_task', models.CharField(blank=True, max_length=20, null=True, verbose_name='Стаутс')),
                ('author_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_task', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('performer_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfomer_task', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
    ]