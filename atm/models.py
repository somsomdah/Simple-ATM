from django.db import models

# Create your models here.

class Card(models.Model):
    number=models.CharField(max_length=16,verbose_name='card number',unique=True)
    pin=models.CharField(max_length=500,verbose_name='card pin number')

class Account(models.Model):
    card=models.ForeignKey('Card',on_delete=models.SET_NULL,null=True,blank=True,related_name='accounts')
    name=models.CharField(max_length=30,verbose_name="account name")
    balance=models.IntegerField(verbose_name="total balance")

class History(models.Model):
    account=models.ForeignKey('Account',on_delete=models.SET_NULL,null=True,blank=True,related_name='histories')
    created_at=models.CharField(max_length=30,verbose_name='deposit/withdrawal time')
    amount=models.IntegerField(verbose_name='deposit/withdrawal amount,negative with withdrawal')
    balance=models.IntegerField(verbose_name='balance after deposit/withdrawl')
