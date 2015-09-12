#encoding: utf-8
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User


class AccountForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'avatar', 'password',]

        labels = {
            'username': 'Usuario',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Email',
            'avatar':''
        }

        widgets={
            'first_name':forms.TextInput(attrs={'readonly':'readonly', 'placeholder':'Nombres', 'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'readonly':'readonly', 'placeholder':'Apellidos', 'class':'form-control'}),
            'username':forms.TextInput(attrs={'readonly':'readonly', 'placeholder':'Usuario', 'class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'Correo electrónico', 'class':'form-control'}),
            'avatar': forms.FileInput(attrs={'class':'hidden'}),
            'password': forms.Textarea(attrs={'readonly':'readonly','class':'hidden'}),
        }



class CustomPasswordChangeForm(PasswordChangeForm):
        def __init__(self, *args, **kwargs):
            super(PasswordChangeForm, self).__init__(*args, **kwargs)
            for key in ('old_password','new_password1','new_password2'):
                self.fields[key] = self.fields.pop(key)

            self.fields['old_password'].widget = forms.PasswordInput(attrs={'placeholder':'Contraseña antigua', 'class':'form-control'})
            self.fields['new_password1'].widget = forms.PasswordInput(attrs={'placeholder':'Nueva contraseña', 'class':'form-control'})
            self.fields['new_password2'].widget = forms.PasswordInput(attrs={'placeholder':'Confirmación', 'class':'form-control'})
