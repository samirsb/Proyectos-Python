from django.http import HttpResponse
from django.shortcuts import render
from SBFotografia.forms import *
from SBFotografia.models import *


def index(request):
    return render(request, "ProyectoFinal/index.html")

def about(request):
    return render(request, "ProyectoFinal/about.html")

def stock(request):
    return render(request, "ProyectoFinal/stock.html")

def stockSearch(request):
    if request.GET['inputStock']:
        category = request.GET['inputStock']
        search = StockCategory.objects.filter(category__icontains=category)
        print(search)
        if not search.exists():
            response = "No es una categoria valida"
        else:
            response = search.get()
        return render(request, "ProyectoFinal/stock.html", {"category": response})
    else:
        response = "No se ingresaron datos"
    
    return HttpResponse(response)

def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            cleanData = form.cleaned_data
            print(cleanData)
            contact = Contact(name = cleanData['name'], lastname = cleanData['lastname'], phone = cleanData['phone'], email = cleanData['email'], message = cleanData['message'], userServices = cleanData['userServices'])
            contact.save()
            return render(request, "ProyectoFinal/index.html")
    else:
        form = ContactForm()
        
    return render(request, "ProyectoFinal/contact.html", {"form":form})
