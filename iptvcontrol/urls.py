from django.urls import path
from . import views

urlpatterns = [
    path('control/', views.iptv_control, name='iptv_control'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('deletar/<int:id>/', views.deletar_cliente, name='deletar_cliente'),
]
