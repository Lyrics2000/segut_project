# Generated by Django 3.2.8 on 2021-11-26 09:04

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_booking_schedule_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to=mainapp.models.upload_image_path),
        ),
    ]