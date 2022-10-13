from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy

from expenses.models import Expenses
from .models import *
from .forms import *


class SignUp(CreateView):
    model = User
    form_class = SignUpUserForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class LogIn(View):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form":form})

    def post(self, request):
        if request.method == "POST":
            form = LoginUserForm(request, data=request.POST)
            if form.is_valid():
                username =  form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('home')
                
        form = LoginUserForm()
        return render(request, 'login.html', {"form":form})


class Logout(View):
    def get(self, request):
        if request.method == 'GET':
            logout(request)
            return redirect('login')
