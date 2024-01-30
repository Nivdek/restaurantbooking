from django.contrib.auth.forms import UserChangeForm
from customuser.models import CustomUser
from django import forms

class UserForm(forms.ModelForm):
    """
    Takes the Booking model in models.py and creates a form using
    the supplied fields.
    """
    class Meta:
        model = CustomUser
        fields = ("email", "phone_number", "first_name", "last_name", "address",)
