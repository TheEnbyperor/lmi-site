# Generated by Django 2.0.4 on 2018-05-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("main_site", "0006_auto_20180506_1733")]

    operations = [
        migrations.AlterField(
            model_name="mainsliderimage",
            name="name",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="siteconfig",
            name="facebook_url",
            field=models.URLField(default=""),
        ),
        migrations.AlterField(
            model_name="siteconfig", name="houzz_url", field=models.URLField(default="")
        ),
        migrations.AlterField(
            model_name="siteconfig",
            name="instagram_url",
            field=models.URLField(default=""),
        ),
        migrations.AlterField(
            model_name="siteconfig",
            name="linkedin_url",
            field=models.URLField(default=""),
        ),
        migrations.AlterField(
            model_name="siteconfig",
            name="pintrest_url",
            field=models.URLField(default=""),
        ),
        migrations.AlterField(
            model_name="testimonial",
            name="client",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="testimonial", name="text", field=models.TextField(default="")
        ),
    ]
