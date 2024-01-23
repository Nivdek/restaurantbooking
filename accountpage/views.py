from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from restaurantpage.models import Restaurant, Booking
from cloudinary.models import CloudinaryField
import logging


logger = logging.getLogger(__name__)


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


def accountoverview(request, tab=None):
    """
    The account view is for handling and displaying all user-related information.
    Users can view and manage their account and their bookings/restaurants.
    """
    tab = request.GET.get('tab', 'profile')

    if request.user.is_authenticated:
        if tab == 'bookings':
            return render(request, "accountpage/accountbookings.html",)
        elif tab == 'restaurant':
            return render(request, "accountpage/accountrestaurant.html",)
        else:
            return render(request, "accountpage/accountprofile.html",)
    else:
        return HttpResponseRedirect("/accountpage/accountauth")


# def accountprofile(request, tab=None):
#     queryset = User.ojects.filter(user=request.user)
#     template_name = "accountpage/accountprofile.html"
#     logger.info(f"Received request for tab: {tab}")

#     context = {
#         'user': queryset,
#         'active_tab': 'tab',
#     }

#     return render(request, template_name, context)


# def accountbookings(request, tab=None):
#     queryset = Booking.objects.filter(user=request.user).order_by("booked_on")
#     template_name = "accountpage/accountbookings.html"
#     logger.info(f"Received request for tab: {tab}")

#     context = {
#         'bookings': queryset,
#         'active_tab': 'tab',
#     }

#     return render(request, template_name, context)


# def accountrestaurant(request, tab=None):
#     queryset = Restaurant.objects.filter(user=request.user).order_by("status")
#     template_name = "accountpage/accountrestaurant.html"
#     logger.info(f"Received request for tab: {tab}")

#     context = {
#         'restaurant': queryset,
#         'active_tab': 'tab',
#     }

#     return render(request, template_name, context)