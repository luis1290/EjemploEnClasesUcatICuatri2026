from flask import Flask, jsonify, request # Importamos Flask, jsonify y request

app = Flask(__name__) # Creamos una instancia de Flask

@app.route('/saludo', methods=['GET']) # Definimos una ruta para el endpoint /saludo
def saludo(): # Definimos la función que se ejecutará cuando se acceda a la ruta /saludo
    return jsonify({'mensaje': '¡Hola, mundo API Flask!'}) # Devolvemos un mensaje de saludo en formato JSON

@app.route('/usuario/<nombre>', methods=['GET']) # Definimos una ruta para el endpoint /usuario/<nombre>
def usuario(nombre): # Definimos la función que se ejecutará cuando se acceda a la ruta /usuario/<nombre>
    return jsonify({'mensaje': f'¡Hola, {nombre}!'}) # Devolvemos un mensaje personalizado con el nombre proporcionado en formato JSON




if __name__ == '__main__': # Verificamos si el script se está ejecutando directamente
    app.run(debug=True) # Ejecutamos la aplicación Flask en modo debug