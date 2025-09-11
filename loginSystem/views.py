from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignupForm, LoginForm
from django.contrib.auth.views import LoginView

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('education:index')
    else:
        form = SignupForm()
    return render(request, 'loginSystem/signup.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('education:index')
    return render(request, 'loginSystem/logout.html')