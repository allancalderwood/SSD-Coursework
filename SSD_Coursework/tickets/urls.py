from django.urls import path
from . import views

app_name = 'tickets'


urlpatterns = [
    path('home/', views.home, name="home"),
    path('tickets/', views.tickets, name="tickets"),
    path('details/<ticketid>', views.details, name="ticket-details"),
    path('settings/', views.settings, name="settings"),
]
