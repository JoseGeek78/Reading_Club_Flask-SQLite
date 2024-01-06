from app import app, db
from flask import request, jsonify, render_template
from datetime import datetime
from models import Usuario, Libro, Reseña, Anotacion

@app.route('/')
def index():
    # Puedes pasar datos adicionales a la plantilla si es necesario
    return render_template('index.html')

# Ejemplo de ruta para añadir un libro
@app.route('/add_book', methods=['POST'])
def add_book():
    if request.method == 'POST':
        # Aquí obtendrías los datos del formulario
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        # Crear y añadir el libro a la base de datos
        nuevo_libro = Libro(titulo=titulo, autor=autor, fecha_seleccion=datetime.now())
        db.session.add(nuevo_libro)
        db.session.commit()
        return jsonify({'mensaje': 'Libro agregado exitosamente', 'titulo': titulo})
    return jsonify({'mensaje': 'Error al añadir el libro'})

# Ejemplo de ruta para cargar reseñas
@app.route('/reseñas', methods=['GET'])
def cargar_reseñas():
    reseñas = Reseña.query.all()  # Obtener todas las reseñas, o filtrar según sea necesario
    reseñas_data = [{'titulo': r.libro.titulo, 'texto': r.texto} for r in reseñas]
    return jsonify(reseñas_data)

# Puedes añadir más rutas según sea necesario
