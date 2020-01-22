from django.shortcuts import render
from school.models import *
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
        data.append(a)
    return render(request,'index.html',context={'data':data})

def pre(request):
    return render(request,'pre.html')

def middle(request):
    return render(request,'middle.html')

def high(request):
    return render(request,'high.html')
