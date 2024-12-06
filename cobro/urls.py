from django.urls import path
from cobro import views
from . import views


urlpatterns = [
    path('', views.index),
    path('cobros/', views.cobros),

]
