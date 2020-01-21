from django.db import models

# Create your models here.
class approach(models.Model):
    name=models.CharField(max_length=264)
    details=models.CharField(max_length=100000)
