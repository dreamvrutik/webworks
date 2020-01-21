from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def pre(request):
    return render(request,'pre.html')

def middle(request):
    return render(request,'middle.html')

def high(request):
    return render(request,'high.html')
