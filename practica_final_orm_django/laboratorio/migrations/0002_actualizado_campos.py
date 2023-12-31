# Generated by Django 4.2.3 on 2023-07-21 21:18

import datetime
from django.db import migrations, models
import laboratorio.models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorgeneral',
            name='especialidad',
            field=models.CharField(default='blank', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='ciudad',
            field=models.CharField(default='blank', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='pais',
            field=models.CharField(default='blank', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='f_fabricacion',
            field=models.DateField(default=datetime.date(2015, 1, 1), validators=[laboratorio.models.validate_year]),
        ),
    ]
