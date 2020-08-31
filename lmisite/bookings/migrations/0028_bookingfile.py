# Generated by Django 3.1 on 2020-08-31 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0027_config_booking_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.URLField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_files', to='bookings.booking')),
            ],
        ),
    ]
