from django.db import models
import random
# Create your models here.

class Contact(models.Model):
    fullname=models.CharField(max_length=100 )
    phone_number=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    adress=models.CharField(max_length=100)
    website=models.URLField(max_length=400)
    occupation=models.CharField(max_length=50, blank=True, null=True)
    company=models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.fullname