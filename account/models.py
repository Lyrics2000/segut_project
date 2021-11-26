from django.db import models
from django.contrib.auth.models import AbstractUser
# from courses.models import upload_image_path
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



class User(AbstractUser):
    email = models.EmailField(verbose_name='email',max_length=255,unique=True)
    phone = models.CharField(null=True,max_length=255)
  
    REQUIRED_FIELDS = ['username','phone','first_name','last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


class Profile_pic(models.Model):
    user_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    image =  models.ImageField(upload_to =  upload_image_path)
    image_filled =  models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_id)

