from django.http import HttpResponse, JsonResponse # crear una respuesta HTTP y una respuesta JSON
from django.views.decorators.csrf import csrf_exempt # para deshabilitar la protección CSRF en esta vista

# Simulación de base de datos en memoria

USERS = {
    1: {
        'id': 1,
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    },
    2: {
        'id': 2,
        'name': 'Jane Smith',
        'age': 25,
        'email': 'jane.smith@example.com'
    }
}

#funcion de hola mundo
@csrf_exempt # deshabilita la protección CSRF para esta vista, lo que permite que se pueda acceder a ella sin necesidad de un token CSRF válido
def hello(request):
    return HttpResponse("Hola mundo Django") # devuelve una respuesta HTTP con el mensaje "Hello, World!"


# funcion para obtener usuarios
@csrf_exempt
def user_info(request):
    if request.method == 'GET':
       return JsonResponse(USERS)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)