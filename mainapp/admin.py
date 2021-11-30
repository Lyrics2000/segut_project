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


class BookingAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'user_id','number_of_seats','seat_ids','total_amount','date_of_booking','booking_status','qr_code']
    list_filter = ['created_at']
    class Meta:
        model = Booking


class TravelScheduleAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'bus_id','starting_point','schedule_date','estimated_arrival_time','fare_amount','type']
    list_filter = ['created_at']
    class Meta:
        model = TravelSChedule

# Register your models here.
admin.site.register(Bus)
admin.site.register(BusOtherImages)
admin.site.register(TravelSChedule,TravelScheduleAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(Payment)
admin.site.register(SLiderPanel)
admin.site.register(AboutUs)
admin.site.register(AboutUsValues)
admin.site.register(OurServices)
admin.site.register(BusStop)
admin.site.register(ContactUs)
