from django.contrib import admin
from .models import Restaurant, Booking
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Restaurant)
class RestaurantAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'author', 'status')
    search_fields = ['name', 'author__username']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('name', 'address',)}
    summernote_fields = ('about',)

# Register your models here.
admin.site.register(Booking)