from django.db import models
from django.contrib.auth.models import User

#Each field is specified as a class attribute, and each attribute maps to a database column.

class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        userName = models.CharField(max_length=30)
        userLastname = models.CharField(max_length=30)
        userPhone = models.CharField(max_length=10)
        userEmail = models.EmailField()
        about = models.CharField(max_length=1000)
        image = models.ImageField(null=True, blank=True, default='default.jpeg', upload_to='profilePics')
        

class Contact(models.Model):
        Cname = models.CharField(max_length=30)
        Clastname = models.CharField(max_length=30)
        Cphone = models.CharField(max_length=10)
        Cemail = models.EmailField() 
        message = models.CharField(max_length=1000)
        userServices = models.CharField(max_length=2, 
                                        choices = [
                                                ('ST', "Fotos de stock"),
                                                ('PH', "Servicio de fotografia"),
                                                ('AL', "Todos")
                                        ],
                                        default='AL')
        
class StockCategory(models.Model):
        category = models.CharField(max_length=40)
        
        def __str__(self):
                return self.category