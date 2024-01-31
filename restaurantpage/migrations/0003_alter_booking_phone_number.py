# Generated by Django 4.2.9 on 2024-01-31 12:44

from django.db import migrations
import phonenumber_field.modelfields
import restaurantpage.models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantpage', '0002_remove_booking_phone_booking_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
