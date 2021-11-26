from django.contrib import admin
from .models import (Bus,
BusOtherImages,
TravelSChedule,
Booking,Payment,
SLiderPanel,
AboutUs,
AboutUsValues,
OurServices,
BusStop,
ContactUs)

# Register your models here.
admin.site.register(Bus)
admin.site.register(BusOtherImages)
admin.site.register(TravelSChedule)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(SLiderPanel)
admin.site.register(AboutUs)
admin.site.register(AboutUsValues)
admin.site.register(OurServices)
admin.site.register(BusStop)
admin.site.register(ContactUs)

