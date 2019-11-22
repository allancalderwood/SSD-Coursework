from django.shortcuts import render
from django.http import HttpResponse


# views here.
def login(request):
    return render(request, 'users/login.html', {'title': 'Login'})
