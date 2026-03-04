from django.shortcuts import render
from employee.models import Employee


def list_employee(request):
    employees = Employee.objects.all()

    return render(request, "employee/list.html", locals())
