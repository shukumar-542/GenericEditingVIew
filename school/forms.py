from tkinter import Widget
from django import forms
from .models import Student

class studentForm(forms.ModelForm):
      class Meta:
            model = Student
            fields = ['name','email','password']

            widgets ={'name': forms.TextInput(attrs={'class':'myclass'})}