# Generated by Django 3.2.8 on 2021-11-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmimeasurement',
            name='result',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('underweight', 'underweight'), ('normal', 'normal'), ('overweight', 'overweight'), ('obese', 'obese')], verbose_name='result'),
        ),
    ]
