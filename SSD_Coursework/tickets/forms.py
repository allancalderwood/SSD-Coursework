from django import forms
from .models import Ticket, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]


class TicketForm(forms.ModelForm):

    PRIORITY = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    priority = forms.ChoiceField(choices=PRIORITY, widget=forms.RadioSelect(),required = True,initial='Low')
    class Meta:
        model = Ticket
        fields = [
            'description',
            'priority',
            'devID'
        ]
        labels = {
            'devID': ('Developer'),
        }
