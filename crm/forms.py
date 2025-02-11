from django import forms
from crm.models import Student_details

class Student_form(forms.ModelForm):
    class Meta:
        model=Student_details
        fields="__all__"
        # fields=["s_name","age"]
        # exclude=("s_name")

class User_form(forms.Form):
    username=forms.CharField(max_length=100)
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=100)
    password=forms.CharField(max_length=100)

class Login_form(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)


    