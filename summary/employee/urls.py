from django.urls import path
from .views import *

urlpatterns = [
    path('employees', get_employees),
    path('save', create_employee),
    path('salary/<int:employee_id>', get_salary)
]