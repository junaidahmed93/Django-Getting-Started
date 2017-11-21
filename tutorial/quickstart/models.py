from django.db import models

# Create your models here.


class Ticket(models.Model):
    SEVERITY = (
        (1,'Major'),
        (2,'Minor')
    )
    created = models.DateTimeField(auto_now_add=True)
    assignee = models.CharField(max_length=90, blank=True)
    reporter = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    done_date = models.DateTimeField(null=True)
    severity = models.CharField(max_length=100,choices=SEVERITY,default='')
    is_done = models.BooleanField(default= False)

    class Meta:
        ordering = ('created',)