# university/views.py
from django.shortcuts import render

def index_view(request):
    return render(request, 'university/index.html')

def about_view(request):
    return render(request, 'university/about.html')

def contact_view(request):
    return render(request, 'university/contact.html')
