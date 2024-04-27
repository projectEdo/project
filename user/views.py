from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.models import Group


def user_login(request):
	error = ''

	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				user = authenticate(request, username=cd['username'], password=cd['password'])
				if user and user.is_active:
					login(request, user)
					if request.user.groups.filter(name='Project Manager').exists():
						return redirect('main')
					else: 
						return redirect('project')
				else: 
					error = 'Пользователь не найден!'
			else: 
				error = 'Пользователь не найден!'
	else:
		if request.user.groups.filter(name='Project Manager').exists():
			return redirect('main')
		else: 
			return redirect('project')

	data = {
		'form' : LoginForm(),
		'error' : error
	}

	return render(request, 'user/login.html', data)


@login_required
def user_logout(request):
	logout(request)
	if not request.user.is_authenticated:
		return redirect('login')
	
	return render(request, 'user/login.html')

