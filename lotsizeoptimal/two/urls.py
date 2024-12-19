from django.urls import path
from .views import production_metrics_view

app_name = 'two'

urlpatterns = [
    path("", production_metrics_view, name="two"),
]
