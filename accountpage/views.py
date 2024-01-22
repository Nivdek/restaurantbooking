from django.shortcuts import render
from django.http import HttpResponseRedirect

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
    """
    The account view is for handling and displaying all user-related information.
    Users can view and manage their account and their bookings/restaurants.
    """
    if request.user.is_authenticated:
        return render(
            request,
            "accountpage/accountoverview.html",
        )
    else:
        return HttpResponseRedirect("/accountpage/accountauth")
