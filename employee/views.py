from django.shortcuts import get_object_or_404, redirect, render
from employee.models import Employee
from employee.forms import EmployeeForm


def list_employee(request):
    # On récupère tous les employés en base de données
    employees = Employee.objects.all()

    # On les passe au template list.html prévue pour affichés tous ces derniers de façon détaillée
    return render(request, "employee/list.html", {"employees": employees})

def add_employee(request):
    # On récupère le formulaire éventuellement passer dans la requête
    form = EmployeeForm(request.POST or None)

    # On vérifie si le fomulaire éventuellement récupérer en valide
    if form.is_valid():
        # Si le formalaire est valide,
        form.save() # les informations sont enregistrées en base
        return redirect('employee:list_employee') # et au retourne à la page de list_employee

    # Si le programme arrive ici, cela signifie que le formulaire s'est avéré soit vide, soit invalide; on retourne donc l'objet form au template form.html
    return render(request, "employee/form.html", {"form": form})

def edit_employee(request, id):
    # On récupère l'employer correspondant à l'id passer en paramètre de requête
    employee = get_object_or_404(Employee, id=id)
    # On récupère ensuite les éventuelles changement apportés par le formulaire au donnée de l'instance
    form = EmployeeForm(request.POST or None, instance=employee)

    # On vérifie si ces informations sont valides
    if form.is_valid():
        # Si le formalaire est valide,
        form.save() # les informations sont enregistrées en base
        return redirect('employee:list_employee') # et au retourne à la page de list_employee
    
    # Si on parvient à niveau dans l'exécution du code, c'est que soit le formulaire est invalide, soit aucune modifications n'a été apportées; on retourne donc l'objet form (comportant les données de l'instance d'Employee) au template form.html
    return render(request, "employee/form.html", {"form": form})
