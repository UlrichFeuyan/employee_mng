from django.db import models


class Employee(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    poste = models.CharField(max_length=255)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nom} - {self.poste}"
