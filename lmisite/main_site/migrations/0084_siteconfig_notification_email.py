# Generated by Django 3.1.5 on 2021-02-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0083_siteconfig_contact_form_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='notification_email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
    ]