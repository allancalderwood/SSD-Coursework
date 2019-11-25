from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import get_user_model
from .models import Ticket, Comment

# views here.
@login_required
def home(request):
    return render(request, 'tickets/home.html', {'title': 'Home'})


@login_required
def tickets(request):
    tickets = Ticket.objects.filter(Q(creatorID=request.user.id) | Q(devID=request.user.id))
    return render(request, 'tickets/tickets.html', {'title': 'Tickets', 'tickets': tickets})


@login_required
def details(request, ticketid):
    details = Ticket.objects.filter(id=ticketid)
    devID=details[0].devID.id
    dev = get_user_model().objects.get(id=devID)
    return render(request, 'tickets/details.html', {'title': 'Ticket Details', 'details': details, 'dev': dev})


@login_required
def settings(request):
    return render(request, 'tickets/settings.html', {'title': 'Settings'})
