#encoding: utf-8
from django import forms
from cms.models import Post, Document


class PostForm(forms.ModelForm):

    class Meta:
        exclude = ['slug','date', 'special']
        model = Post
        widgets={
          'title':forms.TextInput(attrs={'placeholder':'Título', 'class':'form-control'}),
          'published':forms.CheckboxInput(attrs={'data-toggle':'switch'}),
          'related_articles':forms.SelectMultiple(attrs={'class':'form-control'}),
          'related_documents':forms.SelectMultiple(attrs={'class':'form-control'}),
        }

class DocumentForm(forms.ModelForm):

    class Meta:
        exclude = ['slug','date', 'special']
        model = Document
        widgets={
          'name':forms.TextInput(attrs={'placeholder':'Nombre', 'class':'form-control'}),
          'file':forms.ClearableFileInput(attrs={'placeholder':'Archivo', 'class':'form-control'}),
          'published':forms.CheckboxInput(attrs={'data-toggle':'switch'}),
          'related_documents':forms.SelectMultiple(attrs={'class':'form-control'}),
          'related_articles':forms.SelectMultiple(attrs={'class':'form-control'}),
        }