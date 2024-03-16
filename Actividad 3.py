from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de ejemplo para libros y autores
libros = []
autores = []

# Operaciones CRUD para el recurso Libro

@app.route('/libros', methods=['GET'])
def obtener_libros():
    return jsonify(libros)

@app.route('/libros/<int:id>', methods=['GET'])
def obtener_libro(id):
    libro = next((libro for libro in libros if libro['id'] == id), None)
    return jsonify(libro) if libro else ('Libro no encontrado', 404)

@app.route('/libros', methods=['POST'])
def crear_libro():
    nuevo_libro = request.json
    libros.append(nuevo_libro)
    return jsonify(nuevo_libro), 201

@app.route('/libros/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    libro_actualizado = request.json
    libro_existente = next((libro for libro in libros if libro['id'] == id), None)
    if libro_existente:
        libro_existente.update(libro_actualizado)
        return jsonify(libro_existente)
    else:
        return 'Libro no encontrado', 404

@app.route('/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    global libros
    libros = [libro for libro in libros if libro['id'] != id]
    return '', 204

# Operaciones CRUD para el recurso Autor

@app.route('/autores', methods=['GET'])
def obtener_autores():
    return jsonify(autores)

@app.route('/autores/<int:id>', methods=['GET'])
def obtener_autor(id):
    autor = next((autor for autor in autores if autor['id'] == id), None)
    return jsonify(autor) if autor else ('Autor no encontrado', 404)

@app.route('/autores', methods=['POST'])
def crear_autor():
    nuevo_autor = request.json
    autores.append(nuevo_autor)
    return jsonify(nuevo_autor), 201

@app.route('/autores/<int:id>', methods=['PUT'])
def actualizar_autor(id):
    autor_actualizado = request.json
    autor_existente = next((autor for autor in autores if autor['id'] == id), None)
    if autor_existente:
        autor_existente.update(autor_actualizado)
        return jsonify(autor_existente)
    else:
        return 'Autor no encontrado', 404

@app.route('/autores/<int:id>', methods=['DELETE'])
def eliminar_autor(id):
    global autores
    autores = [autor for autor in autores if autor['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
