from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect('education:index')
    else:
        form = SignupForm()
    return render(request, 'loginSystem/signup.html', {'form': form})