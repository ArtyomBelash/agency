from django.urls import path
from . import views
urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employees_list'),
    path('emlpoyee/<int:pk>', views.EmployeeDetailView.as_view(), name='employees_detail'),
    path('search_employee', views.SearchEmployeeView.as_view(), name='search_employee'),
]
