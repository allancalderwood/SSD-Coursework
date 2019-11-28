from django import forms
from .models import Ticket, Comment
from django.contrib.auth import get_user_model

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
    STAGE = [
        ('Development', 'Development'),
        ('Testing', 'Testing'),
        ('Production', 'Production'),
    ]
    priority = forms.ChoiceField(choices=PRIORITY,required = True,initial='Low')
    stage = forms.ChoiceField(choices=STAGE,required = True,initial='Development')
    class Meta:
        model = Ticket
        fields = [
            'description',
            'devID',
            'priority',
            'stage',
        ]
        labels = {
            'devID': ('Developer'),
        }

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['devID'].queryset = get_user_model().objects.filter(role__title='DEV')
