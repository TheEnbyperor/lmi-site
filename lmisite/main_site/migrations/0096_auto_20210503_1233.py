# Generated by Django 3.2 on 2021-05-03 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0095_quizvariables_initial_vale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizvariables',
            old_name='initial_vale',
            new_name='initial_value',
        ),
        migrations.AlterField(
            model_name='quizvariables',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variables', to='main_site.quiz'),
        ),
    ]
