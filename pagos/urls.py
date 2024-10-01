from django.urls import path
from . import views

urlpatterns = [
    path('generar_recibo_prematricula/', views.generarReciboPrematricula, name='generar_recibo_prematricula'),
]
