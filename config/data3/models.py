from django.db import models

# Create your models here.

class Post2(models.Model):
    Birtdate = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Address

