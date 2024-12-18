from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('one/', include('one.urls')),
    path('two/', include("two.urls")),
    path('admin/', admin.site.urls),
]
