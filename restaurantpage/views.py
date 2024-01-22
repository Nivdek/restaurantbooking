from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Restaurant, Booking
from .forms import BookingForm

# Create your views here.
class RestaurantList(generic.ListView):
    """
    The "home" view of the project, it lists any approved restaurants
    and sorts them by what city they are located in.
    """
    queryset = Restaurant.objects.filter(status=1).order_by("city")
    template_name = "restaurantpage/index.html"



def restaurant_detail(request, slug):
    """
    This view handles both the detailed restaurant view when a restaurant item is clicked
    and the booking form which populates the same view.
    """
    queryset = Restaurant.objects.filter(status=1)
    restaurant = get_object_or_404(queryset, slug=slug)
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.restaurant = restaurant
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Booking receieved and awaiting confirmation.'
            )
        else:
            print(booking_form.errors.as_data())
            
    booking_form = BookingForm()
    
    return render(
        request,
        "restaurantpage/restaurant_detail.html",
        {
            "restaurant": restaurant,
            "booking_form": booking_form,
        },
    )
