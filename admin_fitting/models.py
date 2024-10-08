from django.db import models

class GettingStartedInfo(models.Model):
    content = models.TextField()

    def __str__(self):
        return "Golf Club Fitting Information"