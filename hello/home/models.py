from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=200, default='DEFAULT VALUE')
    password = models.CharField(max_length=120, default='DEFAULT VALUE')
    #date = models.DateTimeField
    
    def __str__(self):
        return self.email