from django.contrib import admin
from django.contrib.admin import ModelAdmin

from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ('full_name', 'hire_date', 'position')
    search_fields = ('full_name', 'position')
