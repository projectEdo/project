from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignForm
from project.models import Task, Project
# from django.contrib.auth.models import Group

# Create your views here.

@login_required
def main(request):
	sign_result = ''

	if request.method == 'POST':
		if 'sign-up' in request.POST:
			form = SignForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				new_user = form.save(commit=False)
				new_user.set_password(cd['password'])
				form.save()
				new_user.groups.add(cd['group'])
				sign_result = 'Успешно!'
			else:
				sign_result = 'Форма была неверной'

	project = Project.objects.all()
	task = Task.objects.all()
	user = User.objects.all()

	data = {
		'project' : project,
		'task' : task,
		'User' : user,
		'sign_result' : sign_result,
		'form' : SignForm(),
	}

	return render(request, 'main/index.html', data)