# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.template import loader
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')

