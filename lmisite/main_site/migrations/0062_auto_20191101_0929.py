# Generated by Django 2.2.6 on 2019-11-01 09:29

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0061_siteconfig_home_help_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='about_image_2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='about_text_2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]