from django import forms
from SBFotografia.models import *

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'userName',
            'userLastname',
            'userPhone',
            'userEmail',            
            'about',
            'image'
        ]


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