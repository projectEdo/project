from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Task
from .forms import ProjectForm, TaskForm


@login_required
def project(request):
	project = Project.objects.all()
	error=''

	if request.method == 'POST':
		if 'project-btn' in request.POST:
			form = ProjectForm(request.POST)
			if form.is_valid():
				new_project = form.save(commit=False)
				new_project.author_project = request.user
				new_project.save()
				return redirect('project')
			else: error='Что-то пошло не так!'

	data = {
		'project' : project,
		'projectForm' : ProjectForm(),
		'error' : error
	}

	return render(request, 'project/project.html', data)



@login_required
def task(request):
	task = Task.objects.all()

	return render(request, 'project/task.html', {'task' : task})



@login_required
def created_project(request):
	
	data = {
		'projectForm' : ProjectForm()
	}
	
	return render(request, 'project/create_project.html', data)



@login_required
def details_project(request, pk):
	project = get_object_or_404(Project, pk=pk)
	error = ''

	if request.method == 'POST':
		if 'project-btn' in request.POST:
			form = TaskForm(request.POST)
			if form.is_valid():
				new_task = form.save(commit=False)
				new_task.author_task = request.user
				new_task.project_task = project
				new_task.save()
				return redirect('details_project', pk=pk)
			else: error='Что-то пошло не так!'

	data = {
		'taskForm' : TaskForm(),
		'project' : project,
		'error' : error
	}

	return render(request, 'project/details_project.html', data)



@login_required
def details_task(request, pk):
	task = get_object_or_404(Task, pk=pk)
	project = task.project_task

	data = {
		'task' : task,
		'project' : project,
		'taskForm' : TaskForm()
	}

	return render(request, 'project/details_task.html', data)



@login_required
def task_list(request, pk):
	project = get_object_or_404(Project, pk=pk)
	task = Task.objects.filter(project_task = project)

	data = {
		'task' : task,
		'project' : project
	}

	return render(request, 'project/task.html', data)



@login_required
def created_task(request):
	error = ''

	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			new_task = form.save(commit=False)
			new_task.author_task = request.user
			new_task.project_task = request.Project
			new_task.save()
			return redirect('details_project')
		else: error='Что-то пошло не так!'

	data = {
		'taskForm' : TaskForm(),
		'error' : error
	}
	
	return render(request, 'project/create_task.html', data)