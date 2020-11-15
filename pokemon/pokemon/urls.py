from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pokedex/', include('pokedex.urls')),
    path('admin/', admin.site.urls),
]