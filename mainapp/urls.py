
from django.urls import path

from .views import (
    index,
    car_book,
    detailed_page,
    booking,
    mpesa_pay
)

app_name = "mainapp"
urlpatterns = [
    path('', index,name="index"),
    path('vehicle_detailed/',detailed_page,name="vehicle_detailed"),
    path('booking/',car_book,name="car_booking"),
    path('booking_busses/',booking,name="boooking"),
    path('mpesa_pay/',mpesa_pay,name="mpesa_pay")
    
]
