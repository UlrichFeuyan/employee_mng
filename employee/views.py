from django.shortcuts import redirect, render
from employee.models import Employee
from employee.forms import EmployeeForm


def list_employee(request):
    employees = Employee.objects.all()

    return render(request, "employee/list.html", {"employees": employees})

def add_employee(request):
    # On récupère le formulaire éventuellement passer dans la requête
    form = EmployeeForm(request.POST or None)

    # On vérifie si le fomulaire éventuellement récupérer en valide
    if form.is_valid():
        form.save()
        return redirect('employee:list_employee')

    # Si le programme arrive ici, cela signifie que le formulaire s'est avéré soit vide, soit invalide
    return render(request, "employee/form.html", {"form": form})
