from django import forms
from . import models


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'description']
        widget = {
            'category': forms.Select(),
            'title': forms.TextInput(),
            'description': forms.Textarea()
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'status']
        widget = {
            'category': forms.Select(),
            'title': forms.TextInput(),
            'status': forms.Select()
        }