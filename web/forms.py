from django import forms 
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Categoria, Photocard

class RegistroUserForm(UserCreationForm):
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput(attrs={
        'placeholder': 'Ingrese su contraseña..',
        'id': 'password1',
        'required': 'required'
    }))
    password2 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput(attrs={
        'placeholder': 'Ingrese nuevamente su contraseña..',
        'id': 'password2',
        'required': 'required'
    }))
    class Meta: 
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets ={
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre de usuario..',
                    'id': 'username',
                    'required': 'required'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su Nombre..',
                    'id': 'nombre',
                    'required': 'required'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su Apellido..',
                    'id': 'apellido',
                    'required': 'required'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Ingrese su Email..',
                    'id': 'email',
                    'required': 'required'
                }
            ),
        }
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        


class PhotocardForm(forms.ModelForm):
    class Meta: 
        model = Photocard
        fields = ['idPhotocard', 'marca', 'modelo', 'imagen', 'categoria', 'precio', 'stock']
        labels = {
            'idPhotocard': 'Id Photocard',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'imagen': 'Imagen',
            'categoria': 'Categoria',
            'precio': 'Precio',
            'stock': 'Stock'
        }
        widgets ={
            'idPhotocard': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Id Photocard',
                    'id': 'idPhotocard'
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese marca Photocard',
                    'id': 'marca'
                }
            ),
            'modelo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese modelo Photocard',
                    'id': 'modelo'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'precio',
                    'placeholder': 'Ingrese precio Photocard',
                    'min': 0
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'stock',
                    'placeholder': 'Ingrese stock Photocard',
                    'min': 0
                }
            ),
        }#fin_form

