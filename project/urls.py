
from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
	path('project', views.project, name='project'),
	path('project/created', views.created_project, name='created_project'),
	path('task', views.task, name='task'),
	path('project/<int:pk>', views.details_project, name='details_project'),
	path('task/<int:pk>', views.details_task, name='details_task'),
	path('task_created', views.created_task, name='created_task'),
	path('project/<int:pk>/task', views.task_list, name='task_list')
]
