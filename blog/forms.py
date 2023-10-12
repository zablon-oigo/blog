from django import forms
from django.forms import ModelForm
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','image','content',]
        # widget={
        #     'title':forms.TextInput(attrs={
        #         'class':'mb-2 w-full px-4 py-3 rounded-xl'
        #     }),
        #     'image':forms.ClearableFileInput(attrs={
        #         'class':'w-full py-3 px-4 border rounded'
        #     }),
        #     'content':forms.Textarea(attrs={
        #         'class':'w-full h-32 p-2 border rounded'
        #     }),
        # 
    title=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Write a nice title for your content ',
        'class':'w-full px-4 py-3 rounded-lg border border-gray-500'
    }))
    image=forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class':'w-full py-3 px-4 border border-gray-500 rounded'
    }))
    content=forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'write your creative thoughts here...',
        'class':'border border-gray-500 rounded-lg h-48 w-full p-2'
    }))


class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['body']
        widgets={
            'body':forms.Textarea(attrs={
                'placehodler':'Comment here.....',
                'class':'px-6 py-4 h-32 w-full rounded-lg border border-gray-600'
            })
        }