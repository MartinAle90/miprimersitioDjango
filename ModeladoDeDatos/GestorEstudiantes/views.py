from django.shortcuts import render
from .models import Estudiante

# crear Estudiante de forma hardcodeada
def crear(request):
    estud = Estudiante.objects.create(
        nombreEst= 'prueba',
        apellidoEst= 'estudiante',
        edadEst = 18,
        notaEst= 10,
    )
    estud.save()
    return render(request, 'ultimoEstudiante.html', {'estudiante': estud})

# crear Estudiante
def crearEstudiante(request, nombre, apellido, edad, nota):
    nuevoEstudiante = Estudiante.objects.create(
        nombreEst= nombre,
        apellidoEst= apellido,
        edadEst = edad,
        notaEst= nota,
    )
    nuevoEstudiante.save()
    return render(request, 'estudiante.html', {'Nuevo Estudiante': nuevoEstudiante})


# Leer todos los estudiantes
def mostrar_libros(request):
    libros = Estudiante.objects.all()
    return render(request, 'listaEstudiantes.html', {'listaLibro':libros})


# Eliminar todos los estudiantes
def borrar_Estudiante(request):
    libros = Estudiante.objects.delete()
    return render(request, 'listaEstudiantes.html', {'listaLibro':libros})