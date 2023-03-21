from django.db import models

#Each field is specified as a class attribute, and each attribute maps to a database column.

class User(models.Model):
        name = models.CharField(max_length=30)
        lastname = models.CharField(max_length=30)
        phone = models.CharField(max_length=10)
        email = models.EmailField() 

class Contact(User):
        message = models.CharField(max_length=1000)

class UserPreference(User):
        stock = 'ST'
        photographer = 'PH'
        both = 'AL'

        services_choices = [
                (stock, "Fotos de stock"),
                (photographer, "Fotografo"),
                (both, "Todos")
        ]
        userServices = models.CharField(max_length=2, 
                                        choices = services_choices,
                                        default=both)
        
class StockCategory(models.Model):
        category = models.CharField(max_length=40)
        
        def __str__(self):
                return self.category