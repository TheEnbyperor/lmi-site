# Generated by Django 3.0.4 on 2020-04-22 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0023_booking_last_notification_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingtype',
            name='hidden',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
