
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView,RetrieveAPIView
from .models import Flight, bookingFlight,Class, Trip
from .serializer import FlightSerializer, BookingFlightSerializer, ClassSerializer,TripSerializer
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny


from rest_framework.views import APIView
from rest_framework.response import Response

 
from django.middleware.csrf import get_token
from django.http import JsonResponse



class FlightListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def list(self, request, *args, **kwargs):
        flights = self.get_queryset()
        serializer = self.get_serializer(flights, many=True)
        serialized_flights = serializer.data

        choices = {
            'flight_status_choices': Flight.FLIGHT_STATUS_CHOICES,
            'to_location_choices': Flight.TO_LOCATION_CHOICES,            
        }

        data = {
            'flights': serialized_flights,
            'choices': choices,
        }

        return Response(data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)


class FlightRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]    
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    lookup_field = 'flight_number'
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class FlightListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

# ---------------------------------------------------------------------------------------
class ClassSerializerListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


    def list(self, request, *args, **kwargs):
        classes = self.get_queryset()
        serializer = self.get_serializer(classes, many=True)
        serialized_classes = serializer.data

        choices = {
            'class_choices': Class.CLASS_CHOICE,                      
        }

        data = {
            'classes': serialized_classes,
            'choices': choices,
        }

        return Response(data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)



class ClassSerializerRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'class_id'



class ClassListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ClassSerializer

    def get_queryset(self):
        flight_number = self.kwargs['flight_number']
        queryset = Class.objects.filter(flight__flight_number=flight_number)
        return queryset



# ---------------------------------------------------------------------------------------
class BookingFlightListCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = bookingFlight.objects.all()
    serializer_class = BookingFlightSerializer
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)


class BookingFlightListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookingFlightSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email')
        print("Email:", email)  # Debug statement
        queryset = bookingFlight.objects.filter(email=email)
        print("Queryset:", queryset)  # Debug statement
        return queryset
    
class BookingFlightRetrieveView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = bookingFlight.objects.all()
    serializer_class = BookingFlightSerializer
    lookup_field = 'id'

# -----------------------------------------------------------------------------------------

class TripListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Trip.objects.all()
    serializer_class = TripSerializer



    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)



class TripRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    lookup_field = 'trip_id'

class TripListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TripSerializer

    def get_queryset(self):
        class_id = self.kwargs['class_id']
        queryset = Trip.objects.filter(classes__class_id=class_id)
        return queryset




def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})





 