from django.template import Template, Context

# 1 creacion del objeto de tipo template
documento_ext = "ruta de ese documento(el html)"

plt = Template(documento_ext.read())

# 2 - creacion del contexto - fuarda el continido dinamico
# datos adiciolaes para el template (variable, funciones, etc)

ctx = Context()

# 3 - rendirizar el objeto template

document = plt.render()