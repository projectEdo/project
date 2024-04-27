from .models import Project, Task
from django.forms import ModelForm, TextInput, Textarea, FileInput, ClearableFileInput, DateInput, Select

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ['title_project', 'specification_project', 'deadline_project', 'file_project', 'performer_project']

		widgets = {
			'title_project' : TextInput(attrs={
				# 'class' : 'form-text-create',
				'class' : 'form-input width',
				'placeholder' : 'Название проекта',
			}),
			'specification_project' : Textarea(attrs={
				'class' : 'form-input widhei',
				'placeholder' : 'Техническое задание',
			}),
			'deadline_project' : DateInput(attrs={
				'class' : 'form-input width',
				'placeholder' : 'Крайний срок'
			}),
			'file_project' : ClearableFileInput(attrs={
				'class' : 'form-file',
				'placeholder' : 'Файл'
			}),
			'performer_project' : Select(attrs={
				'class' : 'form-input created-list',
			})
		}

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['title_task', 'task', 'deadline_task', 'file_task', 'performer_task']

		widgets = {
			'title_task' : TextInput(attrs={
				'class' : 'form-input width',
				'placeholder' : 'Название задачи',
			}),
			'task' : Textarea(attrs={
				'class' : 'form-input widhei',
				'placeholder' : 'Описание задачи',
			}),
			'deadline_task' : DateInput(attrs={
				'class' : 'form-input width',
				'placeholder' : 'Крайний срок'
			}),
			'file_task' : ClearableFileInput(attrs={
				'class' : 'form-file',
				'placeholder' : 'Файл'
			}),
			'performer_task' : Select(attrs={
				'class' : 'form-input created-list',
			})
		}
