from django import forms
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
        super().__init__(*args, **kwargs)
        # Add the 'datetimepicker-input' class to the widget for the DateTimeField
        self.fields['date'].widget.attrs['class'] = 'form-control datetimepicker-input'
    