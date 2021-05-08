from django.db import models

# Create your models here.

class Companies(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField(null=True)
    Offer = models.FileField(upload_to='uploads/')

