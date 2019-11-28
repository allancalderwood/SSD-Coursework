from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.contrib.auth import get_user_model
from .models import Ticket, Comment
from .forms import CommentForm, TicketForm
from django.contrib import messages


# views here.
@login_required
def home(request):
    role = request.user.role.title
    if (role=="TST"):
        tickets = Ticket.objects.filter(Q(status='Resolved') | Q(status='Closed'))
    elif (role=="DEV"):
        ticketsUnfiltered = Ticket.objects.filter(Q(creatorID=request.user.id) | Q(devID=request.user.id))
        tickets = ticketsUnfiltered.filter(status="Open")
    else:
        tickets = Ticket.objects.filter(Q(creatorID=request.user.id) | Q(devID=request.user.id))
    return render(request, 'tickets/home.html', {'title': 'Home','tickets': tickets,'role':role})


@login_required
def tickets(request):
    role = request.user.role.title
    if (role=="TST"):
        tickets = Ticket.objects.filter(Q(status='Resolved') | Q(status='Closed'))
    else:
        ticketsUnfiltered = Ticket.objects.filter(Q(creatorID=request.user.id) | Q(devID=request.user.id))
        tickets = ticketsUnfiltered.filter(status="Open")
    ticketsAll = Ticket.objects.all()
    for ticket in tickets:
        if (len(ticket.description) > 40):
            ticket.description=ticket.description[:40]+"..."
    for ticket in ticketsAll:
        if (len(ticket.description) > 40):
            ticket.description=ticket.description[:40]+"..."
    return render(request, 'tickets/tickets.html', {'title': 'Tickets', 'tickets': tickets,'ticketsAll': ticketsAll,'role':role})


@login_required
def create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            extendedForm = form.save(commit=False)
            extendedForm.creatorID=request.user
            extendedForm.save()
            messages.add_message(request, messages.SUCCESS, 'Ticket created.')
            return redirect('../tickets/')
    else:
         form = TicketForm()

    role = request.user.role.title
    return render(request, 'tickets/create.html', {'title': 'Create a ticket', 'role':role, 'form':form})


@login_required
def details(request, ticketid):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            extendedForm = form.save(commit=False)
            extendedForm.userID=request.user
            extendedForm.ticketID=Ticket.objects.filter(id=ticketid)[0]
            extendedForm.save()
    else:
         form = CommentForm()

    details = Ticket.objects.filter(id=ticketid)
    devID =details[0].devID.id
    dev = get_user_model().objects.get(id=devID)
    comments = Comment.objects.filter(ticketID=ticketid)

    role = request.user.role.title
    for comment in comments:
        comment.author=get_user_model().objects.get(id=comment.userID.id)

    return render(request, 'tickets/details.html', {'title': 'Ticket Details',
    'details': details, 'dev': dev, 'comments':comments, 'role':role})


@login_required
def settings(request):
    return render(request, 'tickets/settings.html', {'title': 'Settings'})

def dev_test(user):
    if not user.is_authenticated:
        return false
    else:
        return user.role.title=="DEV"

def tst_test(user):
    if not user.is_authenticated:
        return false
    else:
        return user.role.title=="TST"

@user_passes_test(dev_test)
def resolve(request, ticketid):
    t = Ticket.objects.get(id=ticketid)
    t.status="Resolved"
    t.save()
    messages.add_message(request, messages.SUCCESS, 'Ticket resolved.')
    return redirect('../tickets/')

@user_passes_test(tst_test)
def reopen(request, ticketid):
    t = Ticket.objects.get(id=ticketid)
    t.status="Open"
    t.save()
    messages.add_message(request, messages.SUCCESS, 'Ticket reopened.')
    return redirect('../tickets/')

@user_passes_test(tst_test)
def close(request, ticketid):
    t = Ticket.objects.get(id=ticketid)
    t.status="Closed"
    t.save()
    messages.add_message(request, messages.SUCCESS, 'Ticket closed.')
    return redirect('../tickets/')
