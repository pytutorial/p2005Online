from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
#from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import login, authenticate

def signup(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username,
                    password=request.POST['password1'])
            login(request, user)
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'registration/signup.html', context)
