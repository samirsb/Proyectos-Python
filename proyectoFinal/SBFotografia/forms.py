from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=10)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)
    userServices = forms.ChoiceField(choices=[
                                       ('ST', "Fotos de stock"),
                                       ('PH', "Fotografo"),
                                       ('AL', "Todos")
                                   ])
    
class StockCategory(forms.Form):
    category = forms.CharField(max_length=40)