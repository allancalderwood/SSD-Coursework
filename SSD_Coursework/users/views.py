from django.shortcuts import render
from django.http import HttpResponse

def account(request):
    return render(request, 'tickets/account.html', {'title': 'Account'})
