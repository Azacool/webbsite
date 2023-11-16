from django.shortcuts import render
from .models import Customer

def index(request):
    content=Customer.objects.all()
    return render(request=request,template_name='index.html',context={'content':content})
def about(request):
    content=Customer.objects.all()
    return render(request=request,template_name='about.html',context={'content':content})
def service(request):
    content=Customer.objects.all()
    return render(request=request,template_name='service.html',context={'content':content})
def why(request):
    content=Customer.objects.all() 
    return render(request=request,template_name='why.html',context={'content':content})
def team(request):
    content=Customer.objects.all() 
    return render(request=request,template_name='team.html',context={'content':content})
    
 
