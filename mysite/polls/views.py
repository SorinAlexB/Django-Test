from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def queries(request):
    mycursor = connection.cursor()
    for x in mycursor:
        HttpResponse(x)