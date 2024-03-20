from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context

# Create your views here.
def test(request):
    ruta = "D:/Cursos/Alkemy - Python/ProyectoDjango/clase13_StaticFiles/miApp/templates/test.html"
    doc_ext = open(ruta)
    template = Template(doc_ext.read())
    doc_ext.close()
    contexto = Context()
    return HttpResponse(template.render(contexto))