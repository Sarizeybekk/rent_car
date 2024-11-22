from django import forms
from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['vehicle', 'rental_date', 'return_date', 'rental_fee', 'damage_status']
