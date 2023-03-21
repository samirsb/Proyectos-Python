from django.contrib import admin
from SBFotografia.models import Contact, User, UserPreference, StockCategory

#Registrar las clases creadas en models que requieran de una base de datos

admin.site.register(Contact)

admin.site.register(User)

admin.site.register(UserPreference)

admin.site.register(StockCategory)