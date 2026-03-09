from django import forms
from .models import Employee, Department


# Formulario para el modelo Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "position", "salary", "department"]
        labels = {
            "name": "Nombre",
            "position": "Posición",
            "salary": "Salario",
            "department": "Departamento",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "position": forms.TextInput(attrs={"class": "form-control"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
            "department": forms.Select(attrs={"class": "form-control"}),
        }

# Formulario para el modelo Department
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name"]
        labels = {
            "name": "Nombre del Departamento",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }

#Metodo de validacion para el campo name, asegurando que no haya empleados con el mismo nombre 
def clean_name(self):
    name = self.cleaned_data.get('name')
    qs = Department.objects.filter(name__iexact=name)
    if self.instance.pk:
        qs = qs.exclude(pk = self.instance.pk)
    if qs.exists():
        raise forms.ValidationError("Ya existe un departamento con este nombre.")
    return name
