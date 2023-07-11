"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from register import views as v
from flightSched import views as fv
from django.contrib.auth import views as auth_views





urlpatterns = [
    # path('admin_register/', v.admin_registration, name='admin_registration'),
    # path('admin_register/', v.admin_registration, name='admin_registration'),
    # path("createflight/flight_list/", fv.show_flight, name="Show flight")
    # path('profile/', fv.show_profile_details),
    # path("login/",v.login, name="register"),


    path('admin/', admin.site.urls),


    path("reactTest/",fv.FlightListCreateView.as_view(), name="react_test"),
    path("reactTestClass/",fv.ClassSerializerListCreateView.as_view(), name="react_test"),
    path("reactTestTrip/",fv.TripListCreateView.as_view(), name="react_test"),
    path("reactRenderList/",fv.FlightListAPIView.as_view(), name="react_render_test"),
    path('flights/<str:flight_number>/', fv.FlightRetrieveUpdateDestroyView.as_view(), name='flight-detail'),
    path('class/<str:flight_number>/', fv.ClassListView.as_view(), name='class-detail'),
    path('trip/<str:class_id>/', fv.TripListView.as_view(), name='trip-detail'),
    path('bookflight/', fv.BookingFlightListCreateView.as_view(), name='booked-detail'),
    path('bookflight/<str:email>/', fv.BookingFlightListAPIView.as_view(), name='get-booked-detail'),

    path('flights/<str:flight_number>/', fv.FlightRetrieveUpdateDestroyView.as_view(), name='update-flight'),
    path('class_update/<str:class_id>/', fv.ClassSerializerRetrieveUpdateDestroyView.as_view(), name='update-class'),
    path('trip_update/<str:trip_id>/', fv.TripRetrieveUpdateDestroyView.as_view(), name='update-trip'),

    path('get-csrf-token/',fv.get_csrf_token, name='get-csrf-token'),


    path('register/', v.UserRegister.as_view(), name='register'),
	path('login/', v.UserLogin.as_view(), name='login'),
	path('logout/', v.UserLogout.as_view(), name='logout'),
	path('user/', v.UserView.as_view(), name='user'),
    path('check_admin/', v.AdminView.as_view(), name='user'),

    
]
