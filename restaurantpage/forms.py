from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('email', 'phone', 'date', 'no_of_guests', 'additional_notes',)