import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

# Create your views here.
def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
#    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
#        'database': database.info(),
#        'count': PageView.objects.count()
    })

def basic_questions(request):
    return render(request, 'welcome/basic_questions.html')

def headers(request):
    return render(request, 'welcome/headers.html', {
        'env': request.META,
    })

def health(request):
    return render(request, 'welcome/health.html')

