from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register_page(request):
    form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})
