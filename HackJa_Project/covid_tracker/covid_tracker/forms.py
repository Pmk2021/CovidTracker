from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="",max_length=12)

class NewPlaceForm(forms.Form):
    name = forms.CharField(label='name',max_length=12)
    email = forms.EmailField(label='company_email', max_length=254)
    phone_number = forms.CharField(label='phone number',max_length=12)

#python manage.py runserver 192.168.1.93:8000
