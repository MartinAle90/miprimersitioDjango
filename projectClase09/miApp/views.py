from django.shortcuts import render
from .models import Book

def crearBook(request):
    libro = Book.objects.create(
        nombre ="Test Libro",
        autor ='Test Autor',
        disponible = False
    )
    return render(request, 'libro.html', {'book': libro})
