# Generated by Django 2.0.7 on 2018-07-29 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0034_auto_20180722_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutsection',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='designinsiderpost',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]