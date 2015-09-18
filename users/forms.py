#encoding: utf-8
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User


class AddUserForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = "Usuario"
		self.fields['password1'].label = "Contraseña"
		self.fields['password2'].label = "Confirmar contraseña"

		self.fields['username'].widget = forms.TextInput(attrs={'placeholder':'Nombre de usuario', 'class':'form-control'})
		self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Nueva contraseña', 'class':'form-control'})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Confirmación', 'class':'form-control'})


class UpdateUserForm(UserChangeForm):
	def __init__(self, *args, **kwargs):
		super(UserChangeForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = "Usuario"
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
		self.fields['email'].required = True

	class Meta:
		model = User
		fields = [
			'first_name', 'last_name', 'username', 'email', 'avatar',
			'is_active', 'is_superuser', 'is_staff', 'password'
		]

		labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
			'is_staff': 'Es administrador',
			'avatar': '',
			'password':''
        }

		widgets = {
			'first_name': forms.TextInput(attrs={'class':'form-control'}),
			'last_name': forms.TextInput(attrs={'class':'form-control'}),
			'username': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			'is_active':forms.CheckboxInput(attrs={'data-toggle':'switch'}),
			'is_staff':forms.CheckboxInput(attrs={'data-toggle':'switch'}),
			'is_superuser':forms.CheckboxInput(attrs={'data-toggle':'switch'}),
			'avatar': forms.FileInput(attrs={'class':'hidden'}),
		}