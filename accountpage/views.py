from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testindex(request):
    return render(
        request,
        "accountpage/accountlanding.html",
    )
