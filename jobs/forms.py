from typing import Any
from django import forms
from .models import Application, Category, Job



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe the catategory...'}),
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'summary', 'description', 'category', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe the job...'}),
            'deadline': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['job', 'description', 'resume']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Explain why you are applying...'}),
            'job': forms.Select(attrs={'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        application = super().save(commit=False)
        application.applicant = self.user
        if commit:
            application.save()
        return application

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
