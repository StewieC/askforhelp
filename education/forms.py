from django import forms
from .models import Article


class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)

        widgets = {
            
            'title': forms.TextInput(attrs={
                
            }),
            'content': forms.Textarea(attrs={
                
            })
        }
        
        
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
        email = forms.CharField(widget=forms.EmailInput(attrs={
            'placeholder': 'Your email',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
        password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
        password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat Password',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
