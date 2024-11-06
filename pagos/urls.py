from django.urls import path
from pagos import views

urlpatterns = [
    path('generar_recibo_prematricula/', views.generarReciboPrematricula, name='generar_recibo_prematricula'),
    path('health-check/', views.healtCheck),
    
]
