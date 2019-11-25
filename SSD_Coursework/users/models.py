from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Role(models.Model):

    DEVELOPER = 'Developer'
    TESTER = 'Tester'
    CLIENT = 'Client'

    ROLE_TITLES = [
        ('DEV', 'Developer'),
        ('TST', 'Tester'),
        ('CLI', 'Client'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Map role to Django user model
    title = models.CharField(
        max_length=3,
        choices=ROLE_TITLES,
    )
