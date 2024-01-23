from . import views
from django.urls import path

urlpatterns = [
    path("accountauth/", views.accountauth, name="accountauth"),
    path("accountoverview/", views.accountoverview, name="accountoverview"),
    #path("accountoverview/<str:tab>/", views.accountoverview, name="accountoverview_tab"),
]