from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    path("signin/", signin, name="signin"),
    # path("fotoPerfil/", profileImage, name="profileImg")
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


