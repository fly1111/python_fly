from django.shortcuts import render,redirect
from django.urls import reverse

def hello(request,year,month):
    context = {}
    context['hello'] = 'Hello World'
    print(year,month)
    return redirect(reverse('TestModel:test'))
