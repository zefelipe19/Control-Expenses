from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('home/', Home.as_view(), name='home'),
    path('home/list-expenses/', ListUserExpenses.as_view(), name='list_expenses'),
    path('home/new-expense/', CreateUserExpense.as_view(), name='new_expense'),
    path('home/detail/<slug>', UserExpensesDetail.as_view(), name='detail'),
    path('home/update/<slug>', UpdateUserExpense.as_view(), name='update'),
    path('home/delete/<slug>', DeleteUserExpense.as_view(), name='delete'),
]
