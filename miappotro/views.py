from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    return HttpResponse("<h1> Holaaaaaaaaaaaaaaaaaaaaaaaa </h1> ")


def cocinero(request):
     return HttpResponse("<h1> Holaaaaaaaaaaaaaaaaaaaaaaaa cocinero </h1> ")


def perro(request):
    return HttpResponse("<h1> Holaaaaaaaaaaaaaaaaaaaaaaaa perro </h1> ")


def gato(request):
     return HttpResponse("<h1> Holaaaaaaaaaaaaaaaaaaaaaaaa gato </h1> ")


def loro(request):
    return HttpResponse("<h1> Holaaaaaaaaaaaaaaaaaaaaaaaa loro </h1> ")


def tiburon(request):
     return HttpResponse("<h1> Holaaaaaaaaaaaaaaaaaaaaaaaa tiburon </h1> ")

