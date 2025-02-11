from django.shortcuts import render
from django.views.generic import View
from crm.forms import Student_form,User_form,Login_form
from crm.models import Student_details,User
from django.contrib.auth import authenticate,login

class Add_details(View):
    def get(self,request):
        form=Student_form
        return render(request,"create.html",{"form":form})
    def post(self,request):
        form=Student_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Student_details.objects.create(**form.cleaned_data)
            form=Student_form
            return render(request,"create.html",{"form":form})



class View_details(View):
    def get(self,request):
        data=Student_details.objects.all()
        return render(request,"view.html",{"data":data})
    
class Delete_details(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        data=Student_details.objects.get(id=id).delete()
        return render(request,'delete.html')
  
class Update_details(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        data=Student_details.objects.get(id=id)
        form=Student_form(instance=data)
        return render(request,"update.html",{"form":form})
    def post(self,request,**kwargs):
        id=kwargs.get("pk")
        data=Student_details.objects.get(id=id)
        form=Student_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return render(request,"update.html",{"form":form})
    
class Registration(View):
    def get(self,request):
        form=User_form
        return render(request,"reg.html",{"form":form})
    
    def post(self,request):
        form=User_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            User.objects.create_user(**form.cleaned_data)
            return render(request,"reg.html",{"form":form})
        
class LoginView(View):
    def get(self,request):
        form=Login_form
        return render(request,"login.html",{"form":form})
        
    def post(self,request):
        form=Login_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=u_name,password=pwd)
            if user:
                login(request,user)
                return render(request,"welcome.html")
            else:
                print("Not found")
        return render(request,"login.html",{"form":form})
        

    
   

        



        