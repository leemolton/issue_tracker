from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.conf import settings
from django.utils import timezone


def index(request):
    entries = Entry.objects.order_by('-date_posted')
    
    context = {'entries' : entries}
    return render(request, 'index.html', context)
    
    
def home(request):
    template = 'index.html'
    return render(request, template)
    

def view(request):
    template = 'datesdiary.html'
    return render(request, template)
    
    
def predict(request):
    return render_to_response('predict.html')