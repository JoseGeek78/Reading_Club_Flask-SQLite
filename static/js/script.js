document.addEventListener('DOMContentLoaded', () => {
    // Manejo de eventos para botones de eliminar
    const deleteButtons = document.querySelectorAll('.delete-book');
    deleteButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            if (!confirm('¿Estás seguro de que quieres eliminar este libro?')) {
                e.preventDefault();
            }
        });
    });

    // Validación de formularios
    const form = document.getElementById('formulario-libro');
    form.addEventListener('submit', (e) => {
        if (!validarFormulario()) {
            e.preventDefault(); // Evitar enviar el formulario si la validación falla
        }
    });

    // Cargar reseñas usando AJAX
    cargarReseñas();
});

function validarFormulario() {
    let titulo = document.getElementById('titulo-libro').value;
    if (titulo.length === 0) {
        alert('Por favor, ingresa el título del libro');
        return false;
    }
    // Añade más validaciones según sea necesario
    return true;
}

function cargarReseñas() {
    fetch('/reseñas')
        .then(response => response.json())
        .then(data => {
            const contenedorReseñas = document.getElementById('contenedor-reseñas');
            data.forEach(reseña => {
                // Suponiendo que 'reseña' tiene propiedades como 'titulo' y 'texto'
                let elemento = document.createElement('div');
                elemento.className = 'reseña';
                elemento.innerHTML = `<h4>${reseña.titulo}</h4><p>${reseña.texto}</p>`;
                contenedorReseñas.appendChild(elemento);
            });
        })
        .catch(error => console.error('Error:', error));
}

function mostrarFormularioReseña() {
    let form = document.getElementById('formulario-reseña');
    form.style.transition = 'opacity 0.5s ease-in-out';
    form.style.opacity = 1;
}

function añadirLibroAlListado(libro) {
    let lista = document.getElementById('lista-libros');
    let nuevoElemento = document.createElement('li');
    nuevoElemento.textContent = libro.titulo;
    lista.appendChild(nuevoElemento);
}

function buscarInformaciónLibro(isbn) {
    fetch(`https://api-libros.com/isbn/${isbn}`)
        .then(response => response.json())
        .then(data => {
            // Procesar y mostrar la información del libro
        })
        .catch(error => console.error('Error:', error));
}
