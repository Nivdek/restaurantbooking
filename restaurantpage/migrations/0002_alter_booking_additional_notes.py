# Generated by Django 4.2.9 on 2024-01-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='additional_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
