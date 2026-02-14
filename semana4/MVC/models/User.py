
class User:
    # Constructor para inicializar los atributos del usuario
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    # Método para obtener la información del usuario en forma de diccionario
    def getInfo(self):
        return {
            'name': self.name,
            'email': self.email
        }