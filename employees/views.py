from django.db.models import Q
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from .forms import EmployeeForm
from .models import Employee


class EmployeeListView(generic.ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'employees/employee_list.html'
    paginate_by = 5


class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'

    def get_object(self, queryset=None):
        return get_object_or_404(Employee, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subordinates'] = self.object.subordinates.all()
        return context


class SearchEmployeeView(generic.ListView, generic.FormView):
    model = Employee
    template_name = 'employees/searched_employee_list.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('search_employee')
    context_object_name = 'employees_list'

    def get_queryset(self):
        queryset = None
        if self.request.POST:
            form = self.get_form()
            if form.is_valid():
                full_name = form.cleaned_data.get('full_name', '')
                position = form.cleaned_data.get('position', '')
                salary = form.cleaned_data.get('salary', None)
                manager = form.cleaned_data.get('manager', '')
                filters = Q()
                if full_name:
                    filters &= Q(full_name__icontains=full_name)
                if position:
                    filters &= Q(position__icontains=position)
                if salary:
                    filters &= Q(salary__icontains=salary)
                if manager:
                    filters &= Q(manager__icontains=manager)
                queryset = Employee.objects.filter(filters)
        return queryset or Employee.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

