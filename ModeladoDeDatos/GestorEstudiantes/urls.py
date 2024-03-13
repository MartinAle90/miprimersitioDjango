from django.urls import path
from .views import mostrar_libros
from . import views

urlpatterns = [
    # path
    # ( se refiere a la url que escribimos en el navegador,
    # la funcionalidad que cumple la url,
    # si se quiere alguna descripcion)
    path('nuevo', views.crear, name='crear'),
    path('nuevoEst', views.crearEstudiante, name='crearEstudiante'),
    path('all', views.mostrar_libros, name='mostrar_libros'),

]
