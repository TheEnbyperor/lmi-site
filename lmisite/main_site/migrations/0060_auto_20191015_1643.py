# Generated by Django 2.2.6 on 2019-10-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0059_auto_20190722_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='about_header_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='contact_header_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='portfolio_header_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='services_header_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='testimonials_header_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
