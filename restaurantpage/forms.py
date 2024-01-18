from django import forms
from django.contrib.admin import widgets
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Takes the Booking model in models.py and creates a form using
    the supplied fields.
    """
    class Meta:
        model = Booking
        fields = ['email', 'phone', 'date', 'no_of_guests', 'additional_notes',]

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S')
        
    
    