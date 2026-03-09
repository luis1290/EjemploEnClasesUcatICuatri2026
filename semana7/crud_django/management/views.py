from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Department
from .forms import EmployeeForm, DepartmentForm

# vista de empleados
def employee_list(request): # listar los empleados
    employee = Employee.objects.select_related('department').all() # se utiliza select_related para optimizar la consulta y evitar consultas adicionales a la base de datos al acceder a los departamentos relacionados
    add_form = EmployeeForm()
    edit_form = [(emp, EmployeeForm(instance=emp)) for emp in employee] # se crea una lista de tuplas que contiene cada empleado y su formulario de edición correspondiente, utilizando el parámetro instance para prellenar el formulario con los datos del empleado
    return render(request, 'management/employee_list.html', {'employee': employee, 'add_form': add_form, 'edit_form': edit_form})

def employee_create(request): # crear un nuevo empleado
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')

def employee_update(request, pk): # actualizar un empleado existente
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    form = EmployeeForm(instance=employee)
    return render(request, 'management/employee_update.html', {'form': form, 'employee': employee})

def employee_delete(request, pk): # eliminar un empleado
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete() 
        return redirect('employee_list')
    return render(request, 'management/employee_confirm_delete.html', {'employee': employee})

# Vista para listar departamentos y mostrar formularios de agregar y editar
def department_list(request):
    department = Department.objects.all() # Obtenemos todos los departamentos
    add_form = DepartmentForm() # Creamos una instancia del formulario para agregar departamentos
    return render(request, 'management/department_list.html', {
        'departments': department, # Pasamos la lista de departamentos al contexto
        'add_form': add_form # Pasamos el formulario de agregar al contexto
    })

# Vista para crear un nuevo departamento
def department_create(request):
    form = DepartmentForm(request.POST or None) # Creamos una instancia del formulario con los datos enviados por POST o None si no hay datos
    if form.is_valid(): # Verificamos si el formulario es válido
        form.save() # Guardamos el nuevo departamento en la base de datos
        return redirect('department_list') # Redirigimos a la vista de lista de departamentos después de guardar
    department = Department.objects.all() # Si el formulario no es válido, obtenemos todos los departamentos para mostrar la lista actualizada
    return render(request, 'management/department_list.html', {
        'departments': department, # Pasamos la lista de departamentos al contexto
        'add_form': form, # Pasamos el formulario con errores al contexto para mostrar los mensajes de error
        'show_errors': True # Indicamos que se deben mostrar los errores en la plantilla
    })




