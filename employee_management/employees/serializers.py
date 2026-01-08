from rest_framework import serializers
from datetime import date
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'employee_id',
            'name',
            'email',
            'department',
            'designation',
            'date_of_joining',
            'status',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'employee_id',
            'created_at',
            'updated_at',
        )

    def validate_email(self, email):
        return email.lower()

    def validate(self, data):
        joining_date = data.get("date_of_joining")
        status = data.get("status", Employee.Status.ACTIVE)

        if joining_date and joining_date > date.today():
            data["status"] = Employee.Status.INACTIVE

        return data

    class Meta:
        model = Employee
        fields = "__all__"