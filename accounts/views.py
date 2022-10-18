from django.shortcuts import render, redirect
from .models import TeacherProfile
from django.views.generic import DetailView , ListView
from .froms import StundetSignupForm , ProflieFrom , Oders
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def studnetcreate(request):
    if request.method == "POST":
        form = StundetSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            myfrom = form.save()
            proflie = TeacherProfile.objects.get(user__username=username)
            proflie.save()
            return redirect("/accounts/login")
    else:
        form = StundetSignupForm()
    return render(request, "registration/stu_signup.html", {"form": form})




class TechersView(ListView):
    model = TeacherProfile
    paginate_by = 20

class TecherDetil(DetailView):
    model = TeacherProfile


    
def khtechers(request):             #where
   techers =  TeacherProfile.objects.filter(city = 'Karthum' )
   return render(request , 'accounts/kh.html' , {'techers':techers})


def batechers(request):
   techers =  TeacherProfile.objects.filter(city = 'bahri' )
   return render(request , 'accounts/ba.html' , {'techers':techers})

def omtechers(request):
   techers =  TeacherProfile.objects.filter(city = 'omdrman' )
   return render(request , 'accounts/om.html' , {'techers':techers})

def shtechers(request):
   techers =  TeacherProfile.objects.filter(city = "sharq alnel" )
   return render(request , 'accounts/sh.html' , {'techers':techers})
def proflie(request):
    techer = TeacherProfile.objects.get(user = request.user)
    if request.method == 'POST':
        form = ProflieFrom(request.POST , instance= techer)
        if form.is_valid():
            form.save(commit=False)
            form.user = techer
            form.save()
        redirect('/accounts/techer/')
    else: 
        form = ProflieFrom(instance= techer)

    return render(request , 'registration/proflie.html' , {'from':form})


def oders(request):
    if request.method == 'POST':
        form = Oders(request.POST)
        if form.is_valid():
            form.save()
        redirect('/accounts/techer/')
    else:
        form = Oders()
    return render(request , 'accounts/oders.html' , {'form':form})



