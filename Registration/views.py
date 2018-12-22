from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .formsreg import UserRegDetails

users = [
    {
        'Title': 'Mr',
        'Name': 'Sarbaroop',
        'DOB': '5/3/1997',
        'Address': 'ISM, Dhanbad',
        'City': 'Dhanbad',
        'State': 'Jharkhand',
        'Nationality': 'Indian',
        'Car_plate_number': 'JH10AG4958',
        'timestamp': '5/6/2018',
        }]

def index(request):
    return render(request, 'home.html')

def home(request):
    context = {
        'users': users
        }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for {username}")
            return redirect('home')
    else:
        form=UserRegisterForm()
    return render(request, 'registration.html', {'form' : form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserRegDetails(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Details submitted for {username}")
            return redirect('home')
    else:
        form = UserRegDetails() 
    return render(request, 'profile.html', {'form': form})
