from django.db import models
from django.contrib.auth.models import User
from .gig import Gig
from .instrument import Instrument


class GigSlot(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, related_name='gig_slots')
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    filled_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)