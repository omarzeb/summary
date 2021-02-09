from rest_framework import serializers
from .models import Employee, Department

class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = ('employee_id', 'first_name', 'last_name', 'department', 'salary_per_day', 'total_working_days')
