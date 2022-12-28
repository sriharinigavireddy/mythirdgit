from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def string1(request):
    return HttpResponse('This is my first string1')


def string2(request):
    return HttpResponse('this is my second string2')
