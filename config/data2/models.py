from django.db import models

# Create your models here.

class Post(models.Model):
    Firstname = models.CharField(max_length=200)
    Lastname = models.CharField(max_length=200)
    Middlename = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Age = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Firstname