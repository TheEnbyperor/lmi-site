# Generated by Django 2.0.7 on 2018-07-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0016_config_google_credentials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrule',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
