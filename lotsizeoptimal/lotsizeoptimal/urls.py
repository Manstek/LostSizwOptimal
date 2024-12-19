from django.contrib import admin
from django.urls import path, include

from one.views import menu


urlpatterns = [
    path('', menu),
    path('one/', include('one.urls')),
    path('two/', include("two.urls")),
    path('three/', include('three.urls')),
    path('admin/', admin.site.urls),
]
