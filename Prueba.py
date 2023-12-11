from flask import Flask, jsonify
from flask_cors import CORS  # Importa la extensión

app = Flask(__name__)
CORS(app)  # Habilita CORS para toda la aplicación

@app.route('/api/microservicio', methods=['GET'])
def obtener_datos():
    datos = 'mensaje: Hola desde el microservicio'
    return jsonify(datos)

if __name__ == '__main__':
    app.run(port=5000)