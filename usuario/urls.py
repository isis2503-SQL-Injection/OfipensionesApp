from django.urls import path
from usuario import views

urlpatterns = [
    path('', views.index),

]