
from models.User import User # Importamos la clase User desde el módulo models.User
from views.userView import showUserInfo # Importamos la función showUserInfo desde el módulo views.userView

class UserController:
    def createUser(self, username, email):
        user = User(username, email) # Creamos una instancia de User con el nombre de usuario y el correo electrónico proporcionados
        date = user.getInfo() # Obtenemos la información del usuario en forma de diccionario
        showUserInfo(date) # Llamamos a la función showUserInfo para mostrar la información del usuario
