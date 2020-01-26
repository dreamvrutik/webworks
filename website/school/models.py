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
    details=models.TextField()
    image=models.ImageField(upload_to=rename)

class events(models.Model):
    name=models.CharField(max_length=264)
    details=models.TextField()
    date=models.DateField()
    image=models.ImageField(upload_to=rename_event)


class groups(models.Model):
    group_name=models.CharField(max_length=264,primary_key=True)


def rename_image(instance,filename):
    ext = filename.split('.')[-1]
    ct=0
    try:
        obj=group_images.objects.filter(name=instance.group_name.group_name)
        ct=len(obj)+1
    except Exception as e:
        ct=1
    print(filename)
    filename = "image_%s_%d.%s" % (instance.group_name.group_name.replace(' ','_'),ct,ext)
    return os.path.join('images/', filename)

class group_images(models.Model):
    group_name=models.ForeignKey(groups,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=rename_image)

def rename_blog(instance,filename):
    ext = filename.split('.')[-1]
    filename = "blog_%s.%s" % (instance.title.replace(' ','_'),ext)
    return os.path.join('images/', filename)

class blogs(models.Model):
    title=models.CharField(max_length=264)
    details=models.TextField(max_length=100000)
    image=models.ImageField(upload_to=rename_blog)

class about_us(models.Model):
    details=models.TextField()
