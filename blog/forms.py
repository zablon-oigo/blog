from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','image','content',]
        widget={
            'title':forms.TextInput(attrs={
                'class':'mb-2 w-full px-4 py-3 rounded-xl'
            }),
            'image':forms.ClearableFileInput(attrs={
                'class':'w-full py-3 px-4 border rounded'
            }),
            'content':forms.Textarea(attrs={
                'class':'w-full h-32 p-2 border rounded'
            }),
        }