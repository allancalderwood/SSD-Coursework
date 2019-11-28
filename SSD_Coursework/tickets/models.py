from django.conf import settings
from django.db import models


# Create your models here.
class Ticket(models.Model):

    LOW = 'Low'
    MED = 'Medium'
    HIG = 'High'
    PRIORITY = [
        (LOW, 'Low'),
        (MED, 'Medium'),
        (HIG, 'High'),
    ]

    OPN = 'Open'
    RES = 'Resolved'
    CLS = 'Closed'
    STATUS = [
        (OPN, 'Open'),
        (RES, 'Resolved'),
        (CLS, 'Closed'),
    ]

    DEV = 'Development'
    TEST = 'Testing'
    PRO = 'Production'
    STAGE = [
        (DEV, 'Development'),
        (TEST, 'Testing'),
        (PRO, 'Production'),
    ]

    creatorID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='+'
    )

    devID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='+'
    )

    description = models.TextField(max_length=1000)
    priority = models.CharField(
        max_length=7,
        choices=PRIORITY
    )

    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.CharField(
        max_length=8,
        choices=STATUS,
        default='Open',
    )
    stage = models.CharField(
        max_length=11,
        choices=STAGE,
        default='Development',
    )


class Comment(models.Model):
    ticketID = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    userID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
