from django.shortcuts import render,HttpResponse,redirect
from .models import Employe,Depart,Role,DepartSeri,EmployeSeri
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.db.models import Q

def ViewALL(request):
    return render(request,'index.html')
# Create your views here.

class GETallDetails(generics.ListCreateAPIView):
    serializer_class=EmployeSeri
    queryset=Employe.objects.all()

def ShowallData(request):
    emp=Employe.objects.all()
    context={
        "emp":emp
    }
    return render(request,"viewall.html",context)
def getDeplist(request):
    dep_list=Depart.objects.all()
    return render(request,'add.html',{ 'dep_list': dep_list })
def adddetails(request):
    if request.method=="GET":
        dep_list=Depart.objects.all()
        role_list=Role.objects.all()
        return render(request,'add.html',{ 'dep_list': dep_list ,'role_list':role_list })
    elif request.method=="POST":
        fn=request.POST['first_name']
        ln = request.POST['last_name']
        d = int(request.POST['department'])
        s = int(request.POST['salary'])
        b = int(request.POST['Bonus'])
        r = int(request.POST['role'])
        dob=request.POST['DOB']
        Emp=Employe(first_name=fn,last_name=ln,department_id=d,salary=s,Bonus=b,role_id=r,Joining=datetime.now(),DOB=dob)
        Emp.save()
        return HttpResponse("Employe added Succesfully")
        
    else:
        return HttpResponse("Employe NOT added Succesfully")


def Filterdetails(request):
    if request.method=="POST":
        name=request.POST["first_name"]
        d = request.POST['department']
        print(name,d)
        filterr=Employe.objects.all()
        if name:
            filterr=filterr.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if d:
            filterr=filterr.filter(department__Dname=d)

        context={
            "emp":filterr
        }
        return render(request,'viewall.html',context)

    elif request.method=="GET":
        dep_list=Depart.objects.all()
        data={'dep_list': dep_list}
        return render(request,'Edit.html',data)
def removeEmployee(request,pk=0):
    if pk!=0:
        try:
            Employeee=Employe.objects.get(id=pk)
            Employeee.delete()
            return HttpResponse("Employe deleted Succesfully")
        except:
            return HttpResponse("Please enter a valid Employe ID")
    remove=Employe.objects.all()
    context={
        'remove':remove
    }
    return render(request,'remove.html',context)
# def SigninPage(request):
#     if request.method=="POST":
#         username=request.POST['username']
#         password=request.POST['password']

#         user=authenticate(username=username,password=password)
#         print(username,password)
#         if user is not None:
#             login(request,user)
#             return render(request,'index.html')
#         else:
#             messages.error(request,"Invalid Cridential")
#             return render(request,'SignIn.html')

#     return render(request,'SignIn.html')

# def SignUpPage(request):
#     if request.method=="POST":
#         uname=request.POST.get("username")
#         em=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get("password2")
#         my_user=User.objects.create_user(uname,em,pass1)
#         my_user.save()
#         messages.success(request,"Registerd Succesfully")
#         return render(request,"SignIn.html")
#     return render(request,'SignUp.html')

# def mainpage(request):
    # return render(request,'Home.html')