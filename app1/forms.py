from pyexpat import model
from django import forms
from app1.models import employees

class employeeforms(forms.ModelForm):
    class Meta:
        model = employees
        fields = '__all__'