from django.db import models

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, default="Active")  
