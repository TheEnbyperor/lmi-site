# Generated by Django 2.2.1 on 2019-07-22 12:49

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0056_service_button_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutsectionimage',
            name='section',
        ),
        migrations.RenameField(
            model_name='siteconfig',
            old_name='home_text',
            new_name='home_about_text',
        ),
        migrations.RemoveField(
            model_name='siteconfig',
            name='blog_subtitle',
        ),
        migrations.AddField(
            model_name='service',
            name='home_page_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='about_mission_statement',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='about_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='contact_text_1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='contact_text_2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='home_help_text',
            field=models.TextField(blank=True, verbose_name='Home how can I help text'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='newsletter_credentials',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.DeleteModel(
            name='AboutSection',
        ),
        migrations.DeleteModel(
            name='AboutSectionImage',
        ),
    ]
