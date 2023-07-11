from rest_framework import serializers
from .models import Flight, Class, bookingFlight,Trip
# from register import User
from django.contrib.auth.models import User


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    flight_status = serializers.ChoiceField(choices=Flight.FLIGHT_STATUS_CHOICES)
    to_location = serializers.ChoiceField(choices=Flight.TO_LOCATION_CHOICES)

    class Meta:
        model = Flight
        fields = '__all__'


    def get_flight_status_choices(self, obj):
        return dict(Flight.FLIGHT_STATUS_CHOICES)

    def get_location_choices(self, obj):
        return dict(Flight.TO_LOCATION_CHOICES)


class BookingFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookingFlight
        fields = '__all__'

    def get_trip_choice(self, obj):
        return dict(Flight.TRIP_CHOICE)


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    age = serializers.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'age')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.customuser.age = validated_data['age']
        user.customuser.save()
        return user