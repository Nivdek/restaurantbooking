from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Pending"), (1, "Published"))

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    food_type = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50, default='')
    about = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    
    # These attributes are for data handling and administrative operations
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="restaurant_posts",
        default=User
    )
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["city", "name"]

    def __str__(self):
        return self.name


class Booking(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="bookings"
    )
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    date = models.DateTimeField()
    no_of_guests = models.IntegerField(default=1)
    additional_notes = models.TextField(blank=True)

    # These attributes are for data handling and administrative operations
    approved = models.BooleanField(default=False)
    booked_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-restaurant", "-booked_on"]

    def __str__(self):
        return f"Booking for {self.no_of_guests} at {self.restaurant}"