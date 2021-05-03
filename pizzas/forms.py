from django import forms 

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta: 
        Model = Comment
        fields = ['text']
        labels = {'text':''}