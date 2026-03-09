from django.db import models

#modelo de departamento
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#modelo de empleado
class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE) # relacion con departamento ademas de eliminar el departamento se eliminan los empleados relacionados

    def __str__(self):
        return self.name
