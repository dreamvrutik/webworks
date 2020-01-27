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
    class Meta:
        verbose_name_plural = "Approach"

class events(models.Model):
    name=models.CharField(max_length=264)
    details=models.TextField()
    date=models.DateField()
    image=models.ImageField(upload_to=rename_event)
    class Meta:
        verbose_name_plural = "Events"


class groups(models.Model):
    group_name=models.CharField(max_length=264,primary_key=True)
    class Meta:
        verbose_name_plural = "Groups"


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
    class Meta:
        verbose_name_plural = "Group_Images"

def rename_blog(instance,filename):
    ext = filename.split('.')[-1]
    filename = "blog_%s.%s" % (instance.title.replace(' ','_'),ext)
    return os.path.join('images/', filename)

class blogs(models.Model):
    details=models.TextField(max_length=100000)
    title=models.CharField(max_length=264)
    image=models.ImageField(upload_to=rename_blog)
    class Meta:
        verbose_name_plural = "Blogs"

class about_us(models.Model):
    details=models.TextField()
    class Meta:
        verbose_name_plural = "About_Us"

class contact_us(models.Model):
    address=models.TextField(max_length=100000)
    mobile_number=models.CharField(max_length=264)
    email=models.CharField(max_length=264)
    class Meta:
        verbose_name_plural = "Contact_Us"

class school_tiles(models.Model):
    title=models.CharField(max_length=264)
    details=models.TextField(max_length=100000)
    class Meta:
        verbose_name_plural = "School_Tiles"
