from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.base import TemplateView
from .models import Student
from django import forms
from .forms import studentForm
# Create your views here.
# class studentCreateView(CreateView):
#       model = Student
#       fields = ['name', 'email','password']
#       template_name ='school/home.html'
#       success_url = '/thank/'

#       def get_form(self):
#             form = super().get_form()
#             form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
#             form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})

#             return form


class studentCreateView(CreateView):
      form_class = studentForm
      template_name ='school/home.html'
      success_url = '/thank/'
      

class thiankTemplateView(TemplateView):
      template_name = 'school/thank.html'

class studentupdate(UpdateView):
      model = Student
      form_class = studentForm
      template_name ='school/home.html'
      success_url = '/thank/'



# class studentupdate(UpdateView):
#       model = Student
#       fields = ['name','email','password']
#       template_name ='school/home.html'
#       success_url = '/thank/'


#       def get_form(self):
#             form = super().get_form()
#             form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
#             form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})

#             return form