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
        return HttpResponseRedirect("/")
    else:
        return render(
            request,
            "accountpage/accountauth.html",
        )


