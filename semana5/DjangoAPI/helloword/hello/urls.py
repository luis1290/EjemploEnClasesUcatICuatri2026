from django.urls import path # importar la función de vista hello desde el archivo views.py
from .views import hello

urlpatterns = [
    path('', hello, name='hello'),
]