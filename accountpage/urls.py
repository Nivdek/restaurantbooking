from . import views
from django.urls import path

urlpatterns = [
    path("accountlanding/", views.testindex, name="accountlanding"),
]