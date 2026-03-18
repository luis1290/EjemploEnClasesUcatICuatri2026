from django.contrib.auth import authenticate, login, logout # Importa las funciones de autenticación, inicio de sesión y cierre de sesión de Django
from django.contrib.auth.forms import AuthenticationForm # Importa el formulario de autenticación de Django
from django.contrib.auth.decorators import login_required # Importa el decorador de inicio de sesión requerido de Django
from django.shortcuts import render, redirect # Importa las funciones de renderizado y redirección de Django
from .forms_auth import RegisterForm # Importa el formulario de registro personalizado desde forms_auth.py

#vista para el registro de usuarios
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST) # Crea una instancia del formulario de registro con los datos enviados por el usuario
        if form.is_valid(): # Verifica si el formulario es válido
            form.save() # Guarda el nuevo usuario en la base de datos
            return redirect('login') # Redirige al usuario a la página de inicio de sesión después de registrarse
    else:
        form = RegisterForm() # Crea una instancia vacía del formulario de registro para mostrarlo al usuario
    return render(request, 'management/register.html', {'form': form}) # Renderiza la plantilla de registro con el formulario

#vista para el inicio de sesión de usuarios
def login_view(request):
    if request.user.is_authenticated: # Verifica si el usuario ya está autenticado
        return redirect('employee_list') # Redirige al usuario a la lista de empleados si ya ha iniciado sesión
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) # Crea una instancia del formulario de autenticación con los datos enviados por el usuario
        if form.is_valid(): # Verifica si el formulario es válido
            user = form.get_user()
            login(request, user) # Inicia sesión al usuario
            return redirect('employee_list') # Redirige al usuario a la lista de empleados después de iniciar sesión
    else:
        form = AuthenticationForm() # Crea una instancia vacía del formulario de autenticación para mostrarlo al usuario
    return render(request, 'management/login.html', {'form': form}) # Renderiza la plantilla de inicio de sesión con el formulario

#vista para el cierre de sesión de usuarios
def logout_view(request):
    logout(request) # Cierra la sesión del usuario
    return redirect('login') # Redirige al usuario a la página de inicio de sesión después de cerrar sesión
