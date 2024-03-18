import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template

def saludo1(request):
    documento = """
        <html>
            <body>
                <h1>
                    Hola Mundoooo
                </h1>
            </body>
        </html>
    """


def saludo3(request):
    # se creearon dos variables que se van a usar en la plantilla
    nombre = "Juan"
    fecha_actual = datetime.datetime.now
    cursos = ["React", "Django", "PHP", "JavaScrip"]
    #cursos = []
    ruta = "D:/Cursos/Alkemy - Python/ProyectoDjango/clase12Template/miApp/templates/plantilla3.html"
    doc_externo = open(ruta) # ruta absoluta
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    # creamos un contexto
    # le establecemos un diccionario, donde vamos a llmar a la variable que necesitamos
    contexto = Context({
        "nombre_user": nombre,
        "fecha_actual": fecha_actual,
        "cursos": cursos
    })
    
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
    

