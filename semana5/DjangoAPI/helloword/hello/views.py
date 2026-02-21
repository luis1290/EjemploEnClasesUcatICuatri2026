from django.http import HttpResponse # crear una respuesta HTTP

#funcion de hola mundo
def hello(request):
    return HttpResponse("Hola mundo Django") # devuelve una respuesta HTTP con el mensaje "Hello, World!"