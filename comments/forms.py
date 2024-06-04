from django import forms
from .models import comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['comment']