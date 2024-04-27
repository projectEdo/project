from django.contrib.auth.models import User, Group
from django.forms import ModelForm, TextInput, CharField, PasswordInput, ModelChoiceField, Select



class SignForm(ModelForm):

	password = CharField(label='Пароль', widget=PasswordInput(attrs={
				'class' : 'form-input',
				'placeholder' : 'Пароль'
			})) # Поле 'Пароль'
	
	password_two = CharField(label='Повторный пароль', widget=PasswordInput(attrs={
				'class' : 'form-input',
				'placeholder' : 'Повторите пароль'
			})) # Поле 'Повторите пароль'
	
	group = ModelChoiceField(queryset=Group.objects.all(), empty_label=None, label='Должность', widget=Select(attrs={
		'class' : 'form-input',
		'value' : 'Роль'
		}))

	class Meta:
		

		model = User
		fields = ['username', 'first_name']

		widgets = {
			'first_name' : TextInput(attrs={
				'class' : 'form-input',
				'placeholder' : 'Имя',
			}), # Виджет для поля 'Имя'
			'username' : TextInput(attrs={
				'class' : 'form-input',
				'placeholder' : 'Логин'
			}), # Виджет для поля 'Логин'
		}