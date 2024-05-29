from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from account.forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a 'home' page or any other page
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})


def home(request):
    return render(request, 'account/home.html')
