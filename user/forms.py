from django.forms import TextInput, Form, CharField, PasswordInput

# Форма для авторизации пользователей
class LoginForm(Form):
	username = CharField(label='Логин', widget=TextInput(attrs={
		'class': 'form-input',
		'placeholder' : 'Логин'
		})) # Поле 'Логин' 

	password = CharField(label='Пароль', widget=PasswordInput(attrs={
		'class' : 'form-input',
		'placeholder' : 'Пароль'
	})) # Поле 'Пароль'