from django.urls import path

from .views import batch_calculator

app_name = 'one'

urlpatterns = [
    path('', batch_calculator, name='one'),
]
