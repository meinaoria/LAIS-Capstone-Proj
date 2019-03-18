from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Login Successful, Welcome {username}')
            return redirect('login')
        else:
            form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
