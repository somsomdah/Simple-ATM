# Generated by Django 3.0.8 on 2021-01-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='pin',
            field=models.CharField(max_length=4, verbose_name='card pin number'),
        ),
    ]