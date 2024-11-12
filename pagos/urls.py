from django.urls import path
from pagos import views

urlpatterns = [
    path('generar_recibo_prematricula/', views.generarReciboPrematricula, name='generar_recibo_prematricula'),
    path('health-check/', views.healtCheck),
    path('menu/', views.menu),
    path('avisar/', views.avisar),
    path('auth0_recibo_prematricula/', views.VerReciboPrematricula, name='auth0_recibo_prematricula'),

    
]
