from django.urls import path

from .views import batch_calculator

urlpatterns = [
    path('', batch_calculator, name='nazad'),
]
