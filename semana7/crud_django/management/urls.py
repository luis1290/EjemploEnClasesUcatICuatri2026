from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'), # ruta para listar empleados
    path('employees/create/', views.employee_create, name='employee_create'), # Ruta para crear un nuevo empleado
    path('employees/<int:pk>/update/', views.employee_update, name='employee_update'), # Ruta para editar un empleado existente, con el ID del empleado como parámetro
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'), # Ruta para eliminar un empleado, con el ID del empleado como parámetro
    path('departments/', views.department_list, name='department_list'), # Ruta para listar departamentos
    path('departments/create/', views.department_create, name='department_create'), # Ruta para crear un nuevo departamento
]