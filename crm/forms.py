from django import forms
from crm.models import Student_details

class Student_form(forms.ModelForm):
    class Meta:
        model=Student_details
        fields="__all__"
        # fields=["s_name","age"]
        # exclude=("s_name")

