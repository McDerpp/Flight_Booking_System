# Generated by Django 4.2 on 2023-06-01 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number',
        ),
    ]