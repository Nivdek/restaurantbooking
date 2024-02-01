from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.db import models
from django.contrib import messages
from django.conf import settings
from customuser.models import CustomUser
from .forms import UserForm
from restaurantpage.models import Restaurant, Booking
from cloudinary.models import CloudinaryField

# Create your views here.

def accountauth(request):
    """
    This view handles the user request of going to the accountpage.
    If the user is already authenticated the view will redirect to the account page,
    if not, the view will render the accountlanding template for Login / Signup.
    """
    if request.user.is_authenticated:
        return HttpResponseRedirect("/accountpage/accountoverview")
    else:
        return render(
            request,
            "accountpage/accountauth.html",
        )


def accountoverview(request):
    if request.user.is_authenticated:
        user_instance = request.user
        if request.method == 'POST':
            form = UserForm(request.POST, instance=user_instance)
            if form.is_valid():
                form.save()
                return redirect('accountoverview')
        else:
            form = UserForm(instance=user_instance)

        queryset_bookings = Booking.objects.filter(restaurant__author=request.user).order_by("booked_on")
        queryset_restaurants = Restaurant.objects.filter(author=request.user).order_by("status")
    
        context = {
            'user_instance': user_instance,
            'form': form,
            'bookings': queryset_bookings,
            'restaurants': queryset_restaurants,
        }

        return render(request, "accountpage/accountoverview.html", context)
    else:
        return HttpResponseRedirect("/accountpage/accountauth")


def booking_detail(request, slug):
    """
    This view handles the detailed booking view when a booking item is clicked
    """
    booking = get_object_or_404(Booking, slug=slug)
    return render(request, 'accountpage/bookingdetail.html', {'booking': booking})