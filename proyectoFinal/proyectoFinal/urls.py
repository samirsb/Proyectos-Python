from django.contrib import admin
from django.urls import path
from SBFotografia.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"), 
    path("sobremi/", about, name="about"),
    path("stock/", stock, name="stock"),
    path("contacto/", contact, name="contact"),
    path("stockSearch/", stockSearch, name="stockSearch"),
    path("signup/", signup, name="signup"),
    path("perfil/", profile, name="profile"),
    path("logout/", signout, name="logout"),
    path("signin/", signin, name="signin")
]
