#encoding: utf-8
from django import forms
from cms.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        exclude = ['slug','date']
        model = Post
        widgets={
          'title':forms.TextInput(attrs={'placeholder':'Título', 'class':'form-control'}),
          'published':forms.CheckboxInput(attrs={'data-toggle':'switch'}),
          'related_articles':forms.SelectMultiple(attrs={'class':'form-control'}),
        }
