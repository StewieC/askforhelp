from django import forms
from .models import Article

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl'
            })
        }