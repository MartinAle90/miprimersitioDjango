from django.shortcuts import render
from .models import Book
from django.http import JsonResponse

# Create
def crearBook(request):
    libro = Book.objects.create(
        nombre ="Final Libro",
        autor ='Jaimecito',
        disponible = True
    )
    libro.save()
    return render(request, 'libro.html', {'book': libro})

#Read

def mostrar_libros(request):
    libros = Book.objects.all()
    return render(request, 'allBooks.html', {'listaLibro':libros})
    

#Json response
def ejemplo_json_view(request):
    
    data = {'mensaje': 'Hola desde Json Response', 'numero': 42}
    return render(request, 'json.html', {'data': JsonResponse(data)}) 