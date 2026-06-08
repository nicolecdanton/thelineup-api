from django.db import models
from django.contrib.auth.models import User


class Gig(models.Model):
    booker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gigs')
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE, related_name='gigs')
    pay_per_musician = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1500, blank=True)