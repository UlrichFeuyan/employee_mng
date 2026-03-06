from django import forms
from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ['nom', 'email', 'poste', 'salaire']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder' : 'Nom',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input w-full',
                'placeholder' : 'Email',
            }),
            'poste': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder' : 'Poste',
            }),
            'salaire': forms.NumberInput(attrs={
                'class': 'input w-full',
                'placeholder' : 'Salaire',
            }),
        }
