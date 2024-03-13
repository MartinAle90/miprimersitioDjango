from django.contrib import admin
from .models import Producto

# Register your models here. - REGISTRALOS
# Para realizar un CRUD mas accesible

class ProductoAdmin(admin.ModelAdmin):
    # campos o columanas que se muestran en la grilla
    list_display = ("titulo", "categoria", "color", "precio")
    # Estables los campos sobre los cuales vamos a realizar la busqueda
    search_fields = ["titulo"]
    search_fields = ["color"]

admin.site.register(Producto, ProductoAdmin)

