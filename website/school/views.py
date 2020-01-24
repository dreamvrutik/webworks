from django.shortcuts import render
from school.models import *
import shutil
import datetime
# Create your views here.
def index(request):
    obj=approach.objects.all()
    data=[]
    for i in obj:
        a=[]
        a.append(i.name)
        a.append(i.details[0:150])
        x=i.name
        x=x.replace(' ','_')
        x="approach/"+x
        a.append(x)
        img="/media/"+str(i.image)
        a.append(img)
        data.append(a)
    obj=events.objects.filter(date__gte=datetime.datetime.now()).order_by('date')
    eves=[]
    ct=0
    for i in obj:
        a=[]
        a.append(i.name)
        x=str(i.date)
        x=x.split('-')
        x=x[2]+'-'+x[1]+'-'+x[0]
        a.append(x)
        img="/media/"+str(i.image)
        a.append(img)
        x=i.name
        x=x.replace(' ','_')
        x="/events/"+x
        a.append(x)
        eves.append(a)
        ct+=1
        if ct==2:
            break


    return render(request,'index.html',context={'data':data,'no_of_events':ct,'events':eves})

def pre(request):
    obj=events.objects.filter(date__gte=datetime.datetime.now()).order_by('date')
    eves=[]
    ct=0
    for i in obj:
        a=[]
        a.append(i.name)
        x=str(i.date)
        x=x.split('-')
        x=x[2]+'-'+x[1]+'-'+x[0]
        a.append(x)
        img="/media/"+str(i.image)
        a.append(img)
        x=i.name
        x=x.replace(' ','_')
        x="/events/"+x
        a.append(x)
        eves.append(a)
        ct+=1
        if ct==2:
            break

    return render(request,'pre.html',context={'no_of_events':ct,'events':eves})

def middle(request):
    obj=events.objects.filter(date__gte=datetime.datetime.now()).order_by('date')
    eves=[]
    ct=0
    for i in obj:
        a=[]
        a.append(i.name)
        x=str(i.date)
        x=x.split('-')
        x=x[2]+'-'+x[1]+'-'+x[0]
        a.append(x)
        img="/media/"+str(i.image)
        a.append(img)
        x=i.name
        x=x.replace(' ','_')
        x="/events/"+x
        a.append(x)
        eves.append(a)
        ct+=1
        if ct==2:
            break


    return render(request,'middle.html',context={'no_of_events':ct,'events':eves})

def high(request):
    obj=events.objects.filter(date__gte=datetime.datetime.now()).order_by('date')
    eves=[]
    ct=0
    for i in obj:
        a=[]
        a.append(i.name)
        x=str(i.date)
        x=x.split('-')
        x=x[2]+'-'+x[1]+'-'+x[0]
        a.append(x)
        img="/media/"+str(i.image)
        a.append(img)
        x=i.name
        x=x.replace(' ','_')
        x="/events/"+x
        a.append(x)
        eves.append(a)
        ct+=1
        if ct==2:
            break


    return render(request,'high.html',context={'no_of_events':ct,'events':eves})

def display_approach(request,title):
    obj=events.objects.filter(date__gte=datetime.datetime.now()).order_by('date')
    eves=[]
    ct=0
    for i in obj:
        a=[]
        a.append(i.name)
        x=str(i.date)
        x=x.split('-')
        x=x[2]+'-'+x[1]+'-'+x[0]
        a.append(x)
        img="/media/"+str(i.image)
        a.append(img)
        x=i.name
        x=x.replace(' ','_')
        x="/events/"+x
        a.append(x)
        eves.append(a)
        ct+=1
        if ct==2:
            break

    title=title.replace('_',' ')
    obj=approach.objects.get(name=title)
    data=[title,obj.details]
    return render(request,'approach.html',context={'data':data,'no_of_events':ct,'events':eves})

def display_event(request,title):
    obj=events.objects.filter(date__gte=datetime.datetime.now()).order_by('date')
    eves=[]
    ct=0
    for i in obj:
        a=[]
        a.append(i.name)
        x=str(i.date)
        x=x.split('-')
        x=x[2]+'-'+x[1]+'-'+x[0]
        a.append(x)
        img="/media/"+str(i.image)
        a.append(img)
        x=i.name
        x=x.replace(' ','_')
        x="/events/"+x
        a.append(x)
        eves.append(a)
        ct+=1
        if ct==2:
            break

    title=title.replace('_',' ')
    obj=events.objects.get(name=title)
    data=[title,obj.date,obj.details]
    return render(request,'events.html',context={'data':data,'no_of_events':ct,'events':eves})

def gallery(request):
    grouplist=[]
    obj=groups.objects.all()
    for i in obj:
        a=[]
        a.append(i.group_name.upper())
        print(a)
        try:
            obj1=group_images.objects.filter(group_name=i)
            a.append("/media/"+str(obj1[0].image))
            a.append("/gallery/"+i.group_name.replace(" ","_"))
            grouplist.append(a)
        except Exception as e:
            print(e)
            continue
    print(grouplist)
    obj=events.objects.filter(date__gte=datetime.datetime.now()).order_by('date')
    eves=[]
    ct=0
    for i in obj:
        a=[]
        a.append(i.name)
        x=str(i.date)
        x=x.split('-')
        x=x[2]+'-'+x[1]+'-'+x[0]
        a.append(x)
        img="/media/"+str(i.image)
        a.append(img)
        x=i.name
        x=x.replace(' ','_')
        x="/events/"+x
        a.append(x)
        eves.append(a)
        ct+=1
        if ct==2:
            break
    return render(request,"gallery.html",context={'grouplist':grouplist,'no_of_events':ct,'events':eves})

def gallery_group(request,name):
    name=name.replace('_',' ')
    obj=groups.objects.get(group_name=name)
    obj=group_images.objects.filter(group_name=obj)
    name=name.upper()
    imagelist=[]
    for i in obj:
        imagelist.append("/media/"+str(i.image))
    obj=events.objects.filter(date__gte=datetime.datetime.now()).order_by('date')
    eves=[]
    ct=0
    for i in obj:
        a=[]
        a.append(i.name)
        x=str(i.date)
        x=x.split('-')
        x=x[2]+'-'+x[1]+'-'+x[0]
        a.append(x)
        img="/media/"+str(i.image)
        a.append(img)
        x=i.name
        x=x.replace(' ','_')
        x="/events/"+x
        a.append(x)
        eves.append(a)
        ct+=1
        if ct==2:
            break

    return render(request,'group_gallery.html',context={'name':name,'imagelist':imagelist,'no_of_events':ct,'events':eves})
