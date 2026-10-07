# Blog Django

Blog desarrollado con Django, con sistema de posts (CRUD completo) e imágenes asociadas.

## Funcionalidades

- Páginas estáticas: Inicio y Acerca de
- Listado de posts publicados
- Vista de detalle individual por post
- Crear nuevo post (con imagen opcional)
- Editar post existente (incluyendo cambio de imagen)
- Eliminar post (con página de confirmación previa)
- Panel de administración de Django

## Tecnologías

- Python
- Django
- SQLite (base de datos local)
- Pillow (procesamiento de imágenes)
- HTML / CSS

## Instalación

1. Cloná el repositorio

```bash
git clone https://github.com/fedeeelpz/Preentrega10-coder
cd Preentrega10-coder
```

2. Creá y activá un entorno virtual

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

3. Instalá las dependencias

```bash
pip install -r requirements.txt
```

4. Aplicá las migraciones

```bash
python manage.py migrate
```

5. Creá un superusuario (para acceder al panel de administración)

```bash
python manage.py createsuperuser
```

6. Corré el servidor

```bash
python manage.py runserver
```

7. Accedé a la aplicación

- Inicio: http://127.0.0.1:8000/inicio/
- Acerca de: http://127.0.0.1:8000/acerca/
- Posts: http://127.0.0.1:8000/posts/
- Panel de administración: http://127.0.0.1:8000/admin/

## Operaciones CRUD disponibles

| Operación | URL |
|---|---|
| Listar posts | `/posts/` |
| Ver detalle de un post | `/posts/<id>/` |
| Crear un post | `/posts/crear/` |
| Editar un post | `/posts/<id>/editar/` |
| Eliminar un post | `/posts/<id>/eliminar/` |

## Manejo de imágenes

- Cada post puede tener una imagen asociada (campo `imagen`, opcional)
- Se utiliza la librería **Pillow** para el procesamiento de imágenes (dependencia nueva instalada con `pip install Pillow`)
- Las imágenes se guardan en la carpeta `media/posts/`, configurada mediante `MEDIA_URL` y `MEDIA_ROOT` en `settings.py`
- Durante el desarrollo, las imágenes se sirven agregando la configuración de `static()` en `blog_project/urls.py`, activa solo cuando `DEBUG = True`

### Cómo probar la carga de imágenes

1. Entrá a `/posts/crear/` o editá un post existente desde `/posts/<id>/editar/`
2. Seleccioná una imagen desde el campo de archivo del formulario
3. Guardá el post
4. La imagen debería verse correctamente en el listado y/o en la vista de detalle del post

## Estructura del proyecto

```
blog_consola/
├── manage.py
├── blog_project/          # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── posts/                 # App principal
│   ├── models.py          # Modelo Post
│   ├── views.py           # Lógica del CRUD
│   ├── forms.py           # Formulario de posts (con soporte de imágenes)
│   ├── urls.py             # Rutas de la app
│   ├── admin.py            # Configuración del panel admin
│   ├── templates/posts/    # Templates HTML
│   └── static/posts/       # Archivos CSS
└── media/posts/            # Imágenes subidas por los usuarios
```