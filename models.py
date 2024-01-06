from app import db
from datetime import datetime

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(80), nullable=False)
    reseñas = db.relationship('Reseña', backref='usuario', lazy=True)
    anotaciones = db.relationship('Anotacion', backref='usuario', lazy=True)

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(50), nullable=False)
    fecha_seleccion = db.Column(db.Date, default=datetime.utcnow)
    reseñas = db.relationship('Reseña', backref='libro', lazy=True)
    anotaciones = db.relationship('Anotacion', backref='libro', lazy=True)

class Reseña(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_libro = db.Column(db.Integer, db.ForeignKey('libro.id'), nullable=False)
    calificacion = db.Column(db.Integer, nullable=False)
    texto = db.Column(db.Text, nullable=False)

class Anotacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_libro = db.Column(db.Integer, db.ForeignKey('libro.id'), nullable=False)
    anotacion = db.Column(db.Text, nullable=False)
