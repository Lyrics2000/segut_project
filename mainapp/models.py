from django.db import models
from authentification.models import User
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
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    bus_no = models.IntegerField(unique=True)
    bus_no_plate = models.CharField(max_length=255,unique=True)
    bus_type = models.CharField(max_length=255)
    bus_image = models.ImageField(upload_to=upload_image_path)

    def __str__(self):
        return self.bus_no_plate


class BusOtherImages(BaseModel):
    bus_id = models.ForeignKey(Bus,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image_path)

    def __str__(self):
        return str(self.bus_id)


class TravelSChedule(BaseModel):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    bus_id = models.ForeignKey(Bus,on_delete=models.CASCADE)
    starting_point =  models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    schedule_date = models.DateTimeField()
    departure_time = models.DateTimeField()
    estimated_arrival_time = models.DateTimeField()
    fare_amount = models.DecimalField(decimal_places=2,max_digits=20)
    remarks = models.TextField()

    def __str__(self):
        return self.destination

class Booking(BaseModel):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    schedule_id : models.ForeignKey(TravelSChedule,on_delete=models.CASCADE)
    number_of_seats = models.IntegerField()
    fare_amount = models.DecimalField(decimal_places=2,max_digits=20)
    total_amount = models.DecimalField(decimal_places=2,max_digits=20)
    date_of_booking = models.DateTimeField()
    booking_status = models.BooleanField(default=False)

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

        









