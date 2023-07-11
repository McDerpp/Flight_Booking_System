from django import forms
from .models import Flight, Class
import string
import random


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['from_location', 'to_location', 'departure_date', 'departure_time',
                  'arrival_date', 'arrival_time', 'flight_status']
        

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['class_name', 'price', 'baggage_allowance']
