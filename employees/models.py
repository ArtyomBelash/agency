from django.db import models
from django.urls import reverse_lazy


class Employee(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.CharField(max_length=100, verbose_name='Должность')
    hire_date = models.DateField(verbose_name='Дата рождения')
    salary = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Зарплата')
    manager = models.ForeignKey(to='self', on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='subordinates', verbose_name='Начальник')

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse_lazy('employees_detail', kwargs={'pk': self.pk})

