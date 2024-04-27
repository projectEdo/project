from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	author_project = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель', related_name='author_project')
	performer_project = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Исполнитель', related_name='performer_project')
	title_project = models.CharField('Название', max_length=50)
	specification_project = models.TextField('ТЗ')
	deadline_project = models.DateField('Дедлайн')
	file_project = models.FileField('Документ', null=True, blank=True, upload_to='file/project/')
	date_project = models.DateTimeField('Дата создания', auto_now_add=True)

	def __str__(self):
		return self.title_project


	class Meta:
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'


class Task(models.Model):
	author_task = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель', related_name='author_task')
	performer_task = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Исполнитель', related_name='performer_task')
	project_task = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект', related_name='project_task', null=True, blank=True)
	title_task = models.CharField('Название', max_length=50)
	task = models.TextField('Задача')
	deadline_task = models.DateField('Дедлайн')
	file_task = models.FileField('Документ', null=True, blank=True, upload_to='file/task/')
	date_task = models.DateTimeField('Дата создания', auto_now_add=True)
	status_task = models.CharField('Стаутс', max_length=20, default='создано')

	def __str__(self):
		return self.title_task


	class Meta:
		verbose_name = 'Задание'
		verbose_name_plural = 'Задания'