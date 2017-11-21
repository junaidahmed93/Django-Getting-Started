from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ticket(models.Model):
    print('auth.user')
    SEVERITY = ( 
        (1,'Major'),
        (2,'Minor')
    )
    created = models.DateTimeField(auto_now_add=True)    
    reporter = models.ForeignKey('auth.User', related_name='reporter') 
    assignee = models.ForeignKey('auth.User', related_name='assignee')
    description = models.TextField() 
    done_date = models.DateTimeField(null=True)
    severity = models.CharField(max_length=100,choices=SEVERITY,default='')
    is_done = models.BooleanField(default= False)

    class Meta:
        ordering = ('created',)