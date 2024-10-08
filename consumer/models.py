from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    golf_club_size = models.CharField(max_length=10)

class Fitting(models.Model):
    FITTING_STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('prepped', 'Prepped'),
        ('scheduled', 'Scheduled'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    comments = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=FITTING_STATUS_CHOICES, default='submitted')