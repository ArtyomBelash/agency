from django import forms
from .models import Employee

POSITION_CHOICES = [
    ('', ''),
    ('Manager', 'Manager'),
    ('Senior Developer', 'Senior Developer'),
    ('Developer', 'Developer'),
    ('Junior Developer', 'Junior Developer')
]


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('full_name', 'position', 'salary', 'manager')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

    position = forms.TypedChoiceField(choices=POSITION_CHOICES,
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      initial='')
