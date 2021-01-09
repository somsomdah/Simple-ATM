from django.shortcuts import render,get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.core import serializers
from django.forms.models import model_to_dict
import datetime
import json
from .models import *


# Create your views here.
#class MyView(View):
#    def get(self,request):
#        return HttpResponse('result')

class RegisterView(View):
    def post(self,request):
        #print('*****',json.loads(request.body))
        data=json.loads(request.body)
        card_number=data['card_number']
        pin_number=data['pin_number']
        pin_encrypted=make_password(str(pin_number))

        card=Card.objects.create(number=card_number,pin=pin_encrypted)

        return HttpResponse(json.dumps(model_to_dict(card)))



class AuthenticationView(View):
    def get(self,request):
        data=json.loads(request.body)
        number=data['card_number']
        qs=Card.objects.filter(number=number)
        if qs and check_password(data['pin_number'],qs[0].pin):
            request.session['auth']=True
            request.session['card_num']=qs[0].number
            return HttpResponse(json.dumps({"auth":"success"}))
        else:
            request.session['auth']=False
            return HttpResponse(json.dumps({"auth":"failed"}))


class CreateAccountView(View):
    def post(self,request):

        if not request.session['auth']:
            return HttpResponse(json.dumps({"auth" : "failed"}),status=401)

        data=json.loads(request.body)
        card=get_object_or_404(Card,number=request.session['card_num'])
        account=Account.objects.create(card_id=card.id,name=data['name'],balance=0)
        return HttpResponse(json.dumps(model_to_dict(account)))


class DepositWithdrawalView(View):
    def post(self,request):
        data=json.loads(request.body)

        if not request.session['auth']:
            return HttpResponse(json.dumps({"auth":"failed"}),status=401)

        card=get_object_or_404(Card,number=request.session['card_num'])
        account=get_object_or_404(Account,name=data['account_name'],card_id=card.id)

        balance=account.balance+data['amount']

        history=History.objects.create(created_at=str(datetime.datetime.now()),account_id=account.id,amount=data['amount'],balance=balance)
        account.balance=balance
        account.save()

        return HttpResponse(json.dumps(model_to_dict(history)))


class GetAccountsView(View):
    def get(self,request):
        if not request.session['auth']:
            return HttpResponse(json.dumps({"auth":"failed"}),status=401)
        accounts=Account.objects.filter(card__number=request.session['card_num'])
        result=[]
        for account in accounts:
            result.append(model_to_dict(account))
        return HttpResponse(json.dumps(result))


class GetHistoryView(View):
    def get(self,request):
        if not request.session['auth']:
            return HttpResponse(json.dumps({"auth":"failed"}),status=401)
        data=json.loads(request.body)
        histories=History.objects.filter(account__card__number=request.session['card_num'],account__name=data['account_name'])
        result=[]
        for history in histories:
            result.append(model_to_dict(history))
        return HttpResponse(json.dumps(result),content_type="application/json")




