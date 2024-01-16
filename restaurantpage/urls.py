from . import views
from django.urls import path

urlpatterns = [
    path("", views.RestaurantList.as_view(), name="home"),
    path('<slug:slug>/', views.restaurant_detail, name='restaurant_detail'),
]