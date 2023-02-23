from django.shortcuts import render
from django.views.generic import ListView
from app.models import *
# Create your views here.

class School_list(ListView):
    #template_name='app/school_list.html'
    model=School
    context_object_name='schools'
    #queryset=School.objects.filter(name='Jspiders')
    #ordering=['name']
