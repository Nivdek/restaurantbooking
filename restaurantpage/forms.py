from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    """
    Takes the Booking model in models.py and creates a form using
    the supplied fields.
    """
    class Meta:
        model = Booking
        fields = ('email', 'phone', 'date', 'no_of_guests', 'additional_notes',)