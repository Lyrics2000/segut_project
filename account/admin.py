from django.contrib import admin

# Register your models here.
from .models import User,Profile_pic

admin.site.register(User)
admin.site.register(Profile_pic)
