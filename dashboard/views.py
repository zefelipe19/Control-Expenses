from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from expenses.models import *
from expenses.forms import NewExpenseForm
import pandas as pd


class Index(TemplateView):
    template_name = 'index.html'


class Home(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard.html')
    

# Expenses Area
class ListUserExpenses(LoginRequiredMixin, ListView):
    template_name = 'expenses/expenses.html'
    model = Expenses
    #context_object_name = 'expenses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        expenses = Expenses.objects.filter(
            user=self.request.user
        )

        # receivers_exists = Receivers.objects.filter(
        #     user=self.request.user
        # )
        # context['receivers'] = receivers_exists
        context['expenses'] = expenses
        return context


class CreateUserExpense(LoginRequiredMixin, CreateView):
    template_name = 'expenses/create_expense.html'
    model = Expenses
    form_class = NewExpenseForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Receivers Area
# class CreateUserReceiver(LoginRequiredMixin, CreateView):
#     model = Receivers
#     template_name = 'receivers/receivers_form.html'
#     form_class = NewReceiverForm
#     success_url = reverse_lazy('home')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)


# class ListUserReceivers(LoginRequiredMixin, ListView):
#     template_name = 'receivers/receivers.html'
#     model = Receivers
#     #context_object_name = 'receivers'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         receivers = Receivers.objects.filter(
#             user=self.request.user
#         )
#         context['receivers'] = receivers
#         return context