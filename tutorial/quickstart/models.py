from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Ticket(models.Model):
    print('auth.user')
    SEVERITY = ( 
        (1,'Major'),
        (2,'Minor')
    )
    created = models.DateTimeField(auto_now_add=True)
    # assignee = models.CharField(max_length=90, blank=True)
    assignee = models.ForeignKey('auth.User', related_name='assignee') 
    reporter = models.CharField(max_length=100, blank=True)
    description = models.TextField() 
    done_date = models.DateTimeField(null=True)
    severity = models.CharField(max_length=100,choices=SEVERITY,default='')
    is_done = models.BooleanField(default= False)

    class Meta:
        ordering = ('created',)