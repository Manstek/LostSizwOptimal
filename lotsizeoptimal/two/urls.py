from django.urls import path
from .views import production_metrics_view

urlpatterns = [
    path("", production_metrics_view, name="production_metrics"),
]
