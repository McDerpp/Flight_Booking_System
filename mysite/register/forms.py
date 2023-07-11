from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import date, datetime
from .models import CustomUser

import random
from django.contrib.auth.models import AbstractUser



# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     age = forms.IntegerField()


#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'age')









        
# class AdminRegistrationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password1', 'password2')


# class CustomUser2(AbstractUser):
#     # your custom fields and methods

#     class Meta:
#         verbose_name_plural = 'Custom Users'        

# class BookingForm(forms.Form):
#     booking_id = forms.IntegerField(label='Booking ID')
#     user = forms.ModelChoiceField(queryset=User.objects.all(), label='User')
#     booking_date = forms.DateField(label='Booking Date')
#     trip_type = forms.ChoiceField(choices=[('One-way', 'One-way'), ('Round-trip', 'Round-trip')], label='Trip Type')
#     total_amount = forms.DecimalField(label='Total Amount to Pay')
