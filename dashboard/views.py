from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Case

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        expenses = Expenses.objects.filter(
            user=self.request.user
        )
        context['expenses'] = expenses
        return context
    
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id')
        return qs


class CreateUserExpense(LoginRequiredMixin, CreateView):
    template_name = 'expenses/create_expense.html'
    model = Expenses
    form_class = NewExpenseForm
    success_url = reverse_lazy('list_expenses')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserExpensesDetail(LoginRequiredMixin, DetailView):
    model = Expenses
    context_object_name = 'expense'
    slug_url_kwarg = 'slug'
    template_name = 'expenses/detail_expense.html'


class UpdateUserExpense(LoginRequiredMixin, UpdateView):
    model = Expenses
    context_object_name = 'expense'
    form_class = NewExpenseForm
    slug_url_kwarg = 'slug'
    template_name = 'expenses/update_expense.html'
    success_url = reverse_lazy('detail')


class DeleteUserExpense(LoginRequiredMixin, DeleteView):
    model = Expenses
    context_object_name = 'expense'
    slug_url_kwarg = 'slug'
    template_name = 'expenses/delete_expense.html'
    success_url = reverse_lazy('list_expenses')
