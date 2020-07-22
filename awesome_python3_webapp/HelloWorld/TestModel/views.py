from django.shortcuts import render,redirect
from django.urls import reverse
# Create your views here.

def test(request):
    return render(request,'MyHtml.html')
