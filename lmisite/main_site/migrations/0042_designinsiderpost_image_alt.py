# Generated by Django 2.0.7 on 2018-08-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("main_site", "0041_auto_20180824_0909")]

    operations = [
        migrations.AddField(
            model_name="designinsiderpost",
            name="image_alt",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Image alt text"
            ),
        )
    ]
