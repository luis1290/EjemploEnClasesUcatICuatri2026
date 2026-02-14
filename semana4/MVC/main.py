
from controller.UserController import UserController # Importamos la clase UserController desde el módulo controller.UserController

# Punto de entrada del programa
if __name__ == "__main__":
    controller = UserController() # Creamos una instancia de UserController
    controller.createUser("Juan Perez", "juan@gmail.com") # Llamamos al método createUser para crear un nuevo usuario con el nombre "Juan Perez" y el correo electrónico   

