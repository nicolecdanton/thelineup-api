"Model for venues. One venue can be chose per gig. Venues will be read only and seeded in the database."

from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    