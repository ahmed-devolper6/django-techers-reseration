from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TeacherProfile , Oder

class StundetSignupForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=20, required=True)
    class meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProflieFrom(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['name' , 'educitons' , 'exprince' , 'number' , 'city' , 'tech' , 'subject' ]


class Oders(forms.ModelForm):
    class Meta:
        model = Oder
        fields = '__all__'
