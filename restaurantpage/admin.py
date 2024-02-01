from django.contrib import admin
from .models import Restaurant, Booking
from django_summernote.admin import SummernoteModelAdmin
from phonenumber_field.modelfields import PhoneNumberField

@admin.register(Restaurant)
class RestaurantAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'author', 'status')
    search_fields = ['name', 'author__username']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('name', 'address',)}
    summernote_fields = ('about',)


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('restaurant', 'date', 'no_of_guests', 'slug')
    search_fields = ['restaurant', 'date',]
    list_filter = ('approved',)
    summernote_fields = ('additional_notes',)