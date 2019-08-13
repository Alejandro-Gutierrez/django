
from django.urls import path
from miappotro.views import *

urlpatterns = [
    path('', saludar),
    path('Cocinero/new', cocinero),
    path('perro/new', perro),
    path('gato/new', gato),
    path('loro/new', loro),
    path('tiburon/new', tiburon),

]