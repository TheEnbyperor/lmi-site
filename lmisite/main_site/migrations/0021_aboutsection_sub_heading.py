# Generated by Django 2.0.6 on 2018-06-29 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0020_auto_20180629_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutsection',
            name='sub_heading',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
