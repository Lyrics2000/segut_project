from django.contrib import admin
from .models import (Bus,
BusOtherImages,
TravelSChedule,
Booking,Payment)

# Register your models here.
admin.site.register(Bus)
admin.site.register(BusOtherImages)
admin.site.register(TravelSChedule)
admin.site.register(Booking)
admin.site.register(Payment)

