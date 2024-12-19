from django.urls import path

from .views import index, calculate

app_name = 'three'

urlpatterns = [
    path('', index, name='index'),
    path('calculate/', calculate, name='three'),
]
