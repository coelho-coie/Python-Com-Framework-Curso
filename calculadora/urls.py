from django.urls import path
from . import views

urlpatterns = [
    path('', views.calcular_imc, name='calculadora_imc'),
]