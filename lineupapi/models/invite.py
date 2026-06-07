from django.db import models
from django.contrib.auth.models import User

class Invite(models.Model):
    slot = models.ForeignKey('GigSlot', on_delete=models.CASCADE, related_name='invites')
    musician = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invites')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('withdrawn', 'Withdrawn')], default='pending')
    sent_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(null=True, blank=True)
                                                
                
                                                      
