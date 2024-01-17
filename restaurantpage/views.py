from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Restaurant, Booking
from .forms import BookingForm

# Create your views here.
class RestaurantList(generic.ListView):
    queryset = Restaurant.objects.filter(status=1).order_by("city")
    template_name = "restaurantpage/index.html"

def restaurant_detail(request, slug):
    queryset = Restaurant.objects.filter(status=1)
    restaurant = get_object_or_404(queryset, slug=slug)

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.post = post
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Booking receieved and awaiting confirmation.'
            )

    booking_form = BookingForm()

    return render(
        request,
        "restaurantpage/restaurant_detail.html",
        {"restaurant": restaurant,
        "booking_form": booking_form,
        },
    )
