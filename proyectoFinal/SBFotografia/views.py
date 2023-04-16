from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == "POST": 
        profileData = ProfileForm(request.POST)
        if profileData.is_valid():
            data = Profile( userName = request.POST['userName'], 
                            userLastname = request.POST['userLastname'], 
                            userPhone = request.POST['userPhone'], 
                            userEmail = request.POST['userEmail'], 
                            about = request.POST['about'], 
                            user_id = request.user.id )
            data.save()
            return render(request, "ProyectoFinal/profile.html", {'form': profileData})
    else:
        profileData = ProfileForm()
        return render(request, "ProyectoFinal/profile.html", {'form': profileData, 'error': "Debe estar registrado para ingresar a esta pagina"})

def update_profile(request):
    current_user = get_object_or_404(Profile, id = request.user.id)
    form = ProfileForm(request.POST or None, instance=current_user) 
    if request.method == "POST":
        if form.is_valid():
           form.save()
    return render(request, "ProyectoFinal/update_profile.html", {'form': form})

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
            cleanContactForm = form.cleaned_data
            contact = Contact(Cname = cleanContactForm['Cname'], Clastname = cleanContactForm['Clastname'], Cphone = cleanContactForm['Cphone'], 
                              Cemail = cleanContactForm['Cemail'], message = cleanContactForm['message'], userServices = cleanContactForm['userServices'])
            contact.save()
            return render(request, "ProyectoFinal/contact.html", {
                'form': form,
                'send': "Su mensaje ha sido enviado"
                })
    else:
        form = ContactForm()     
    return render(request, "ProyectoFinal/contact.html", {"form":form})

# def profileImage(request):
#     if request.method == 'POST':
#         userImage = ImageForm(request.POST)
#         if userImage.is_valid():
#             picture = Profile(image = ['image'])
#             picture.save()
#             img_obj = userImage.instance
#             return render(request, "ProyectoFinal/profile.html", {'form': userImage, 'img_obj': img_obj})
#         else:
#             return render(request, "ProyectoFinal/profile.html", {'form': userImage})
#     else:
#         userImage = ImageForm()
#         return render(request, "ProyectoFinal/profile.html", {'form': userImage})