# Generated by Django 4.2.9 on 2024-01-26 03:22

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='phone',
        ),
        migrations.AddField(
            model_name='booking',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]