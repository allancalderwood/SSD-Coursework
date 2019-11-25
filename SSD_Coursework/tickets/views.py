from django.shortcuts import render


# views here.
def home(request):
    return render(request, 'tickets/home.html', {'title': 'Home'})


def tickets(request):
    return render(request, 'tickets/tickets.html', {'title': 'Tickets'})


def settings(request):
    return render(request, 'tickets/settings.html', {'title': 'Settings'})
