# Generated by Django 2.1.2 on 2019-01-13 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("bookings", "0020_bookingquestionanswer")]

    operations = [migrations.RemoveField(model_name="bookingrule", name="recurring")]
