from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse("<h1>My amazing blog!</h1>")
