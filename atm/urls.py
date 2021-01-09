from django.urls import path, include
from .views import *






urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('authenticate/',AuthenticationView.as_view()),
    path('create-account/',CreateAccountView.as_view()),
    path('deposit-withdrawal/',DepositWithdrawalView.as_view()),
    path('accounts/',GetAccountsView.as_view()),
    path('history/',GetHistoryView.as_view()),
]