# project/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    # ...
    # path('flight/', include('flightSched.urls')),
    # path('create/', views.create_flight, name='create_flight'),
    # path('flight/create/', views.create_flight, name='create_flight'),
    # path('class/create/', views.create_class, name='create_class'),
    # path("createflight/",views.create_flight, name="Create flight"),
    path("reactTest/",views.FlightRetrieveUpdateDestroyView, name="react_test")




    # ...


]


