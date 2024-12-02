from django.urls import path
from reporte import views

urlpatterns = [
    path('reporte_estado_cuenta/', views.reporteEstadoCuenta, name='reporte_estado_cuenta'),

]
