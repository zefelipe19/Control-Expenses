from django.contrib import admin
from .models import *


class AllExpensesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name']
    list_display_links = ['id', 'user', 'name']


admin.site.register(Expenses, AllExpensesAdmin,)