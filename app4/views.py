from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jsp (request):
    return HttpResponse('<h1>this is makes for people</h1> <h6> he was tarchbarer</h6>')