from django.urls import path
from . import views

urlpatterns = [
    path('cont/', views.index, name='contstr'),
]