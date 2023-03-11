from django.http import HttpResponse
from datetime import datetime as dt
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Django funcionando")

def today(request):
    day = dt.now()
    return HttpResponse(day)

def name(request, name):
    text = f"Tu nombre es {name}"
    return HttpResponse(text)

def frontend(request):
    html = open("./templates/template1.html")
    plantilla = Template(html.read())
    html.close()
    context = Context()
    document = plantilla.render(context)
    return HttpResponse(document)