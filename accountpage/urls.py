from . import views
from django.urls import path

urlpatterns = [
    path("accountauth/", views.accountauth, name="accountauth"),
    path("accountoverview/", views.accountoverview, name="accountoverview"),
    path('booking/<slug:slug>/', views.booking_detail, name='booking_detail'),
]
