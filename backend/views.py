from django.shortcuts import render
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse, HttpResponseNotFound
from django.shortcuts import render,redirect
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.template import loader

# Create your views here.

@api_view(['GET'])
def index(request):
    template = loader.get_template('index.html')
    print("Database failure")
    return HttpResponse(template.render())

