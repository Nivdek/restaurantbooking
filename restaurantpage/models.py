from django.conf import settings
from django.db import models
from customuser.models import CustomUser
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField


STATUS = ((0, "Pending"), (1, "Published"))
CustomUser = settings.AUTH_USER_MODEL


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    food_type = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    phone_number = PhoneNumberField(null=True)
    address = models.CharField(max_length=50, default='')
    about = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    
    # These attributes are for data handling and administrative operations
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="restaurant_posts",
        default=CustomUser
    )
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["city", "name"]

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
    The Booking model is defined and passed to BookingForm in forms.py
    """
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="bookings"
    )
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField(blank=True, null=True)
    date = models.DateTimeField()
    no_of_guests = models.IntegerField(default=1)
    additional_notes = models.TextField(blank=True, null=True)

    # These attributes are for data handling and administrative operations
    approved = models.BooleanField(default=False)
    booked_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-restaurant", "-booked_on"]

    def __str__(self):
        return f"Booking for {self.no_of_guests} at {self.restaurant}"