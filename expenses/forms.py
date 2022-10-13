from django import forms
from .models import *


# class NewReceiverForm(forms.ModelForm):
#     class Meta():
#         model = Receivers
#         exclude = ('user', 'slug', 'date')


class NewExpenseForm(forms.ModelForm):
    class Meta():
        model = Expenses
        exclude = ('user','date' ,'slug', 'payed', 'payment_date',)
