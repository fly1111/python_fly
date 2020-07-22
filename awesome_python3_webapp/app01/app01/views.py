from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse 
from django.db.models import Avg,Max,Min,Count,Sum
from app01 import models
from app01.My_Forms import EmpForm
from app01 import valid
def add_book(request):
    wo  = models.Author.objects.filter(name='令狐冲').first()
    res = models.Publish.objects.filter(name="古墓出版社").values_list("book__title", "book__price")
    book = models.Book.objects.aggregate(Count('id'),Avg("price"),Max('price'))
    print(book,type(book))
    return HttpResponse(book)
def add_emp(request):
    if request.method =="GET":
        form = EmpForm()
        return render(request,'add_emp.html',{"form":form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data.pop('r_salary')
            print(data)

            models.Emp.objects.create(**data)
            return HttpResponse('ok')
        else:
            print(form.errors)
            clean_errors = form.errors.get("__all__")
            print(222,clean_errors)
        return render(request,'add_emp.html',{'form':form})
def login(request):
    temp_str = valid.get_valid_img(request)
    request.session["temp_str"] = temp_str

    if request.method =="GET":
        return render(request,"login.html")
    username = request.POST.get("name")
    password = request.POST.get("pwd")
    #valid_num = request.POST.get("valid_num")
    #if temp_str.upper() == valid_num.upper():
    user_obj = models.Login.objects.filter(username= username,password=password).first()
    if not user_obj:
        return redirect("/login/")
    else:
        rep = redirect("/index/")
        rep.set_cookie("is_login",True)
        return rep
    #else: 
     #   return redirect("/login/")
def index(request):
    print(request.COOKIES.get("is_login"))
    status = request.COOKIES.get("is_login")
    if not status:
        return redirect('/login/')
    return render(request,'index.html')
def logout(request):
    rep = redirect('/login/')
    rep.delete_cookie("is_login")
    return rep
def order(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request,"order.html")

