# Generated by Django 3.1.5 on 2021-04-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0089_auto_20210411_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='designer_in_a_box_header_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
