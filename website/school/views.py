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
        eves.append(a)
        ct+=1
        if ct==2:
            break

    return render(request,'index.html',context={'data':data,'no_of_events':ct,'events':eves})

def pre(request):
    return render(request,'pre.html')

def middle(request):
    return render(request,'middle.html')

def high(request):
    return render(request,'high.html')

def display_approach(request,title):
    title=title.replace('_',' ')
    obj=approach.objects.get(name=title)
    data=[title,obj.details]
    return render(request,'approach.html',context={'data':data})

def display_event(request,title):
    title=title.replace('_',' ')
    obj=events.objects.get(name=title)
    data=[title,obj.date,obj.details]
    return render(request,'events.html',context={'data':data})
