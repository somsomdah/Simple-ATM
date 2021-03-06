# Generated by Django 3.0.8 on 2021-01-09 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16, verbose_name='card number')),
                ('pin', models.PositiveIntegerField(verbose_name='card pin number')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='deposit/withdrawal time')),
                ('amount', models.IntegerField(verbose_name='deposit/withdrawal amount,negative with withdrawal')),
                ('balance', models.IntegerField(verbose_name='balance after deposit/withdrawl')),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='histories', to='atm.Account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accounts', to='atm.Card'),
        ),
    ]
