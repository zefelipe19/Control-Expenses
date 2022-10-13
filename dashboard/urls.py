from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('home/', Home.as_view(), name='home'),
    path('home/list-expenses/', ListUserExpenses.as_view(), name='list_expenses'),
    #path('home/list-receivers/', ListUserReceivers.as_view(), name='list_receivers'),
    path('home/new-expense/', CreateUserExpense.as_view(), name='new_expense'),
    #path('home/new-receiver/', CreateUserReceiver.as_view(), name='new_receiver')
]
