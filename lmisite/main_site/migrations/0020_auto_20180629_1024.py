# Generated by Django 2.0.6 on 2018-06-29 10:24

from django.db import migrations, models


def reorder(apps, schema_editor):
    models = ['AboutSection', 'AboutSectionImage', 'MainSliderImage', 'Project', 'ProjectAfterImage',
              'ProjectBeforeImage', 'Service', 'ServiceSummary', 'Testimonial']

    for m in models:
        model = apps.get_model("main_site", m)
        order = 0
        for item in model.objects.all():
            order += 1
            item.order = order
            item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0019_siteconfig_calendly_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutsection',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='aboutsectionimage',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='mainsliderimage',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='projectafterimage',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='projectbeforeimage',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='servicesummary',
            options={'ordering': ['order'], 'verbose_name_plural': 'Serivce Summaries'},
        ),
        migrations.AlterModelOptions(
            name='testimonial',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='aboutsection',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aboutsectionimage',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mainsliderimage',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projectafterimage',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projectbeforeimage',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='service',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servicesummary',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RunPython(reorder),
    ]