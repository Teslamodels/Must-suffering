from django.db import models

# Create your models here.

class Post3(models.Model):
    Tesla = models.CharField(max_length=200)
    GM = models.CharField(max_length=200)
    Ford = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Tesla
    