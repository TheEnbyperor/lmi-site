# Generated by Django 2.2.7 on 2019-11-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0066_auto_20191101_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='header_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='featured_on',
            field=models.CharField(blank=True, choices=[('', '---'), ('H', 'Home page'), ('A', 'About page'), ('S', 'Services page'), ('C', 'Contact page')], max_length=1, null=True),
        ),
    ]
