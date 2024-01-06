from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from models import Usuario, Libro, Reseña, Anotacion


# Configuración de la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///club_de_lectura.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelos de la base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(80), nullable=False)

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(50), nullable=False)
    fecha_seleccion = db.Column(db.Date, nullable=False)

class Reseña(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('reseñas', lazy=True))
    id_libro = db.Column(db.Integer, db.ForeignKey('libro.id'), nullable=False)
    libro = db.relationship('Libro', backref=db.backref('reseñas', lazy=True))
    calificacion = db.Column(db.Integer, nullable=False)
    texto = db.Column(db.Text, nullable=False)

class Anotacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('anotaciones', lazy=True))
    id_libro = db.Column(db.Integer, db.ForeignKey('libro.id'), nullable=False)
    libro = db.relationship('Libro', backref=db.backref('anotaciones', lazy=True))
    anotacion = db.Column(db.Text, nullable=False)

# Inicializar la base de datos
@app.before_first_request
def create_tables():
    db.create_all()

# Rutas de ejemplo
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    nuevo_usuario = Usuario(nombre=data['nombre'], email=data['email'], contraseña=data['contraseña'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario agregado exitosamente'}), 201

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    nuevo_libro = Libro(titulo=data['titulo'], autor=data['autor'], fecha_seleccion=datetime.now())
    db.session.add(nuevo_libro)
    db.session.commit()
    return jsonify({'mensaje': 'Libro agregado exitosamente'}), 201

@app.route('/add_review', methods=['POST'])
def add_review():
    data = request.get_json()
    nueva_resena = Reseña(id_usuario=data['id_usuario'], id_libro=data['id_libro'], calificacion=data['calificacion'], texto=data['texto'])
    db.session.add(nueva_resena)
    db.session.commit()
    return jsonify({'mensaje': 'Reseña agregada exitosamente'}), 201

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
