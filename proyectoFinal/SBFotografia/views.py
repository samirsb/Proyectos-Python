from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from SBFotografia.forms import *
from SBFotografia.models import *


def index(request):
    return render(request, "ProyectoFinal/index.html")

def about(request):
    return render(request, "ProyectoFinal/about.html")

def stock(request):
    return render(request, "ProyectoFinal/stock.html")

def signup(request):
    if request.method == "GET":
        return render(request, "ProyectoFinal/signup.html", {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('profile')
            except: 
                return render(request, "ProyectoFinal/signup.html", {
                    'form': UserCreationForm,
                    'error': "El usuario ingresado ya existe"
                       })
        else: 
            return render(request, "ProyectoFinal/signup.html", {
            'form': UserCreationForm,
            'error': "Las contraseñas no coinciden"
            })

def signout(request):
    logout(request)
    return redirect('index')

def signin(request):
    if request.method == "GET":
        return render(request, "ProyectoFinal/signin.html", {'form': AuthenticationForm})
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, "ProyectoFinal/signin.html", {'form': AuthenticationForm, 'error': "Usuario o contraseña incorrecta"})
        else: 
            login(request, user)
            return redirect('index')

def profile(request):
    return render(request, "ProyectoFinal/profile.html", {'form': UserData})

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
            contact = Contact(name = cleanData['name'], lastname = cleanData['lastname'], phone = cleanData['phone'], 
                              email = cleanData['email'], message = cleanData['message'], userServices = cleanData['userServices'])
            contact.save()
            return render(request, "ProyectoFinal/contact.html", {
                'form':form,
                'send': "Su mensaje ha sido enviado"
                })
    else:
        form = ContactForm()     
    return render(request, "ProyectoFinal/contact.html", {"form":form})

