from django import forms
from django.forms.models import ModelForm
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','course']




