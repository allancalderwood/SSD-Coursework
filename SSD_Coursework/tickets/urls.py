from django.urls import path
from . import views

app_name = 'tickets'


urlpatterns = [
    path('home/', views.home, name="home"),
    path('tickets/', views.tickets, name="tickets"),
    path('resolve/<ticketid>', views.resolve, name="tickets"),
    path('reopen/<ticketid>', views.reopen, name="reopen"),
    path('close/<ticketid>', views.close, name="close"),
    path('details/<ticketid>', views.details, name="ticket-details"),
    path('settings/', views.settings, name="settings"),
]
