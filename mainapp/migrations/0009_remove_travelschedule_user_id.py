# Generated by Django 3.2.8 on 2021-11-26 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20211126_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travelschedule',
            name='user_id',
        ),
    ]
