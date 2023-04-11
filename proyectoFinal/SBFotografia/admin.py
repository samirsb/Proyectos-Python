from django.contrib import admin
from SBFotografia.models import Contact, Profile, StockCategory

#Registrar las clases creadas en models que requieran de una base de datos

admin.site.register(Contact)

admin.site.register(Profile)

admin.site.register(StockCategory)