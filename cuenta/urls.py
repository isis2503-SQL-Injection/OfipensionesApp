from django.urls import path
from . import views

urlpatterns = [
    path('reporte_saldo_pendiente/', views.reporteSaldoPendienteCuenta, name='reporte_saldo_pendiente'),
]
