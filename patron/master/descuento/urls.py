from django.urls import path
from descuento import views

urlpatterns = [
    path('nuevodescuento/', views.nuevo_descuento)

]
