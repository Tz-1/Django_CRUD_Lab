from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('insertar/', views.insertar_lab, name='insertar-lab'),
    path('mostrar/', views.mostrar_lab, name='mostrar-lab'),
    path('editar/<int:pk>', views.editar_lab, name='editar-lab'),
    path('editar/actualizarlaboratorio/<int:id>', views.actualizarlaboratorio, name='actualizarlaboratorio'),
    path('eliminar/<int:pk>', views.eliminar_lab, name='eliminar-lab'),
]
