from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # ordenar por 'id', si se antepone el simbolo menos (-) orden descendente
    # sin simbolo, es orden ascendente.
    ordering = ['id']
    # campos o columanas que se muestran en la grilla
    # En list_display podemos agregar 'id' para mostrar en la grilla
    list_display = ['nombre', 'autor', 'disponible']
    # Estables los campos sobre los cuales vamos a realizar la busqueda
    search_fields = ["nombre", "autor"]
    

admin.site.register(Book, BookAdmin)