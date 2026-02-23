from django.urls import path # importar la función de vista hello desde el archivo views.py
from .views import hello, user_info # importar la función de vista user_info desde el archivo views.py

urlpatterns = [
    path('', hello, name='hello'),
    path('users-info/', user_info, name='user_info') # agregar la ruta para la vista user_info
]