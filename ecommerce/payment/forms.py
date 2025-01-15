
from django import forms

from . models import ShippingAddress

class ShippingForm(forms.ModelForm):

    class Mera:

        model = ShippingAddress

        fields = ['full_name', 'email', 'adress1', 'address2', 'city','state' ,'zipcode', ]

        exclude = ['user',]



























