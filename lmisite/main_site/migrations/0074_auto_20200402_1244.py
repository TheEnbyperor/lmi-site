# Generated by Django 3.0.4 on 2020-04-02 12:44

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


def migrate_buttons(apps, schema_editor):
    Service = apps.get_model('main_site', 'Service')
    ServiceButton = apps.get_model('main_site', 'ServiceButton')
    for service in Service.objects.all():
        button = ServiceButton(service=service, button_text=service.button_text, button_url=service.button_url)
        button.save()

    OnlineDesignStep = apps.get_model('main_site', 'OnlineDesignStep')
    OnlineDesignStepButton = apps.get_model('main_site', 'OnlineDesignStepButton')
    for step in OnlineDesignStep.objects.all():
        button = OnlineDesignStepButton(step=step, button_text=step.button_text, button_url=step.button_url)
        button.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0073_auto_20200327_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceButton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_text', models.CharField(blank=True, default='', max_length=255)),
                ('button_url', models.URLField(blank=True, null=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.Service')),
            ],
        ),
        migrations.CreateModel(
            name='OnlineDesignStepButton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_text', models.CharField(blank=True, default='', max_length=255)),
                ('button_url', models.URLField(blank=True, null=True)),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.OnlineDesignStep')),
            ],
        ),
        migrations.RunPython(migrate_buttons),
        migrations.RemoveField(
            model_name='onlinedesignstep',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='onlinedesignstep',
            name='button_url',
        ),
        migrations.RemoveField(
            model_name='service',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='service',
            name='button_url',
        ),
        migrations.AlterField(
            model_name='siteconfig',
            name='services_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
