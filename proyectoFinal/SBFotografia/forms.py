from django import forms
from .models import Profile

class ProfileForm(forms.Form):
        userName = forms.CharField(max_length=30)
        userLastname = forms.CharField(max_length=30)
        userPhone = forms.CharField(max_length=10)
        userEmail = forms.EmailField()
        about = forms.CharField(max_length=1000)

# class ImageForm(forms.ModelForm):
#       class Meta: 
#            model = Profile
#            fields = ('image', )

class ContactForm(forms.Form):
    Cname = forms.CharField(max_length=30)
    Clastname = forms.CharField(max_length=30)
    Cphone = forms.CharField(max_length=10)
    Cemail = forms.EmailField()
    message = forms.CharField(max_length=1000)
    userServices = forms.ChoiceField(choices=[
                                       ('ST', "Fotos de stock"),
                                       ('PH', "Fotografo"),
                                       ('AL', "Todos")
                                   ])
    
class StockCategory(forms.Form):
    category = forms.CharField(max_length=40)