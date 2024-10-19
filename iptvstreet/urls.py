from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iptv/', include('iptvcontrol.urls')),  # Corrigido para incluir as URLs do app
]
