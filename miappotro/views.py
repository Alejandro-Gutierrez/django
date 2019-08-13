from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    return HttpResponse("Holaaaaaaaaaaaaaaaaaaaaaaaa")


def cocinero(request):
     return HttpResponse("Holaaaaaaaaaaaaaaaaaaaaaaaa cocinero")


def perro(request):
    return HttpResponse("Holaaaaaaaaaaaaaaaaaaaaaaaa perro")


def gato(request):
     return HttpResponse("Holaaaaaaaaaaaaaaaaaaaaaaaa gato")


def loro(request):
    return HttpResponse("Holaaaaaaaaaaaaaaaaaaaaaaaa loro")


def tiburon(request):
     return HttpResponse("Holaaaaaaaaaaaaaaaaaaaaaaaa tiburon")