# Generated by Django 3.0.8 on 2021-01-09 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0003_auto_20210109_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.CharField(max_length=16, unique=True, verbose_name='card number'),
        ),
    ]
