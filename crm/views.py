from django.shortcuts import render
from django.views.generic import View
from crm.forms import Student_form
from crm.models import Student_details

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
  
        


