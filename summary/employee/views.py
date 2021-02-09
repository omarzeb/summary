#from django.shortcuts import render

# Create your views here.
from django.http import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['GET'])
def get_employees(request):
    employee_obj = Employee.objects.all()
    employee_obj_serialized = EmployeeSerializer(employee_obj, many = True).data

    return Response(employee_obj_serialized, status = HTTP_200_OK)

@api_view(['Post'])
def create_employee(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    username = request.data.get('username')
    email = request.data.get("email")
    department = request.data.get("department")
    salary_per_day = request.data.get("salary_per_day")
    total_working_days = request.data.get("total_working_days")

    Employee(None, first_name, last_name, username, email, department, salary_per_day, total_working_days).save()
    
    response = {"STATUS": "SUCCESS"}

    return Response(response, status=HTTP_200_OK)

@api_view(['GET'])
def get_salary(request, employee_id):
    emp_obj = Employee.objects.get(pk = employee_id)
    monthly_salary = int(emp_obj.salary_per_day) * int(emp_obj.total_working_days)

    response = {"STATUS": "SUCCESS", "salary": monthly_salary}

    return Response(response, status=HTTP_200_OK)