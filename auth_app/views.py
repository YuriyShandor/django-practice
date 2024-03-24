from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.


def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:list')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        return redirect('auth:login')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})
