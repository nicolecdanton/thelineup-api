"Model for instruments. Many instruemnts may be chosen by many users"
from django.db import models

class Instrument(models.Model):
    name = models.CharField(max_length=255, unique=True)
