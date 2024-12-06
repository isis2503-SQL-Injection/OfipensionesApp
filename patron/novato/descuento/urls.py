from django.urls import path
from descuento import views

urlpatterns = [
    path('descuentos/', views.revisarDescuentos)

]
