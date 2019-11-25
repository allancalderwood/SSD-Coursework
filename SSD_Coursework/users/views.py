from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def account(request):
    return render(request, 'users/account.html', {'title': 'Account'})
