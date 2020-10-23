# Generated by Django 3.1 on 2020-08-29 18:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_project', '0006_auto_20200829_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.IntegerField(default=100, help_text='Value must be in CM, between 120-250cm', validators=[django.core.validators.MaxValueValidator(250), django.core.validators.MinValueValidator(120)]),
        ),
    ]
