from django import forms
from .models import RegisterForm

class MyRegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterForm
        fields = ["Name", "Age", "Event_Name", "Contact_Number", "Email_ID"]