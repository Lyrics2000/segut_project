from django.db import models
from account.models import User
import os
import random


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "thumbnails/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Bus(BaseModel):
    bus_no_plate = models.CharField(max_length=255,unique=True)
    driver_name = models.CharField(max_length=255,blank=True,null=True)
    bus_type = models.CharField(max_length=255)
    number_of_passangers  = models.IntegerField(blank=True,null=True)
    bus_image = models.ImageField(upload_to=upload_image_path)

    def __str__(self):
        return self.bus_no_plate


class BusOtherImages(BaseModel):
    bus_id = models.ForeignKey(Bus,on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to=upload_image_path)

    def __str__(self):
        return str(self.bus_id)


class TravelSChedule(BaseModel):
    bus_id = models.ForeignKey(Bus,on_delete=models.CASCADE)
    starting_point =  models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    schedule_date = models.DateTimeField()
    estimated_arrival_time = models.DateTimeField()
    fare_amount = models.DecimalField(decimal_places=2,max_digits=20)
    remarks = models.TextField()
    VEHICLE_TYPE =(
    ("Express", "Express"),
    ("Inter-County", "Inter-County"),
   
)
    type = models.CharField(choices=VEHICLE_TYPE,default="",max_length=255)

    def __str__(self):
        return self.destination

class Booking(BaseModel):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(TravelSChedule,on_delete=models.CASCADE,blank=True,null=True)
    number_of_seats = models.IntegerField()
    seat_ids =  models.CharField(max_length=255,blank=True,null=True)
    fare_amount = models.DecimalField(decimal_places=2,max_digits=20)
    total_amount = models.DecimalField(decimal_places=2,max_digits=20)
    date_of_booking = models.DateTimeField(blank=True,null=True)
    booking_status = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to=upload_image_path,blank=True,null=True)

    def __str__(self):
        return str(self.schedule_id)

class Payment(BaseModel):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    booking_id = models.ForeignKey(Booking,on_delete=models.CASCADE)
    amount_paid = models.DecimalField(decimal_places=2,max_digits=20)
    payment_date = models.DateTimeField()
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_id)




class SLiderPanel(BaseModel):
    header = models.CharField(max_length=255)
    header2 =  models.CharField(max_length=255)

    def __str__(self):
        return self.header


class AboutUs(BaseModel):
    header =  models.CharField(max_length=255)
    body =  models.TextField()
    image =  models.ImageField(upload_to =  upload_image_path,blank = True,null =True)

    def __str__(self):
        return self.header

class AboutUsValues(BaseModel):
    values =  models.CharField(max_length=255)

    def __str__(self):
        return self.values

class OurServices(BaseModel):
    header =  models.CharField(max_length=255)
    body =  models.TextField()

    def __str__(self):
        return self.header


class BusStop(BaseModel):
    bus_name =  models.CharField(max_length=255)
    bus_stop_image  =  models.ImageField(upload_to =  upload_image_path)

    def __str__(self):
        return self.bus_name

class ContactUs(BaseModel):
    name =  models.CharField(max_length=255)
    email = models.EmailField()
    subject =  models.CharField(max_length=255)
    phone =  models.CharField(max_length=255)
    message =  models.TextField()

    def __str__(self):
        return self.name





        









