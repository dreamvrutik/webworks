from django.db import models
import os
# Create your models here.
def rename(instance,filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.name.replace(' ','_'),ext)
    return os.path.join('images/', filename)

def rename_event(instance,filename):
    ext = filename.split('.')[-1]
    filename = "event_%s.%s" % (instance.name.replace(' ','_'),ext)
    return os.path.join('images/', filename)

class approach(models.Model):
    name=models.CharField(max_length=264)
    details=models.CharField(max_length=100000)
    image=models.ImageField(upload_to=rename)

class events(models.Model):
    name=models.CharField(max_length=264)
    details=models.CharField(max_length=100000)
    date=models.DateField()
    image=models.ImageField(upload_to=rename_event)
