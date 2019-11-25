from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# views here.
@login_required
def home(request):
    return render(request, 'tickets/home.html', {'title': 'Home'})

@login_required
def tickets(request):
    return render(request, 'tickets/tickets.html', {'title': 'Tickets'})

@login_required
def settings(request):
    return render(request, 'tickets/settings.html', {'title': 'Settings'})
