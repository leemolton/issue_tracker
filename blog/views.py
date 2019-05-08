from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.utils import timezone
from django.http import HttpResponse


def index(request):
    entries = Entry.objects.order_by('-date_posted')
    
    context = {'entries' : entries}
    return render(request, 'index.html', context)
    
    
def home(request):
    template = 'index.html'
    return render(request, template)
    

def diary(request):
    return render(request, 'datesdiary.html')

    
def henry(request):
    return render(request, 'henry.html')
    

def jose(request):
    return render(request, 'jose.html')
    
    
def predict(request):
    return render(request, 'predict.html')