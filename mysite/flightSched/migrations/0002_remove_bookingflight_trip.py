# Generated by Django 4.2 on 2023-06-25 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flightSched', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingflight',
            name='trip',
        ),
    ]