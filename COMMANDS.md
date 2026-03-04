# Proyecto todoapp - Comandos de referencia

Este documento describe los comandos necesarios para ejecutar y manejar el proyecto.

## Conceptos clave

- Imagen: plantilla construida a partir del Dockerfile.
- Contenedor: instancia en ejecucion de una imagen.
- Contenedores son efimeros: si se recrean, su sistema de archivos interno se pierde.
- Volumenes: almacenamiento persistente fuera del contenedor.
- En este proyecto, el volumen sqlite_data guarda la base de datos SQLite.

---

## Opcion 1: Correr localmente (desarrollo)

### Comandos Django

Aplicar migraciones:
```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

Crear superusuario:
```bash
python manage.py createsuperuser
```

Iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

Acceder en el navegador: http://127.0.0.1:8000

---

## Opcion 2: Correr con Docker (recomendado para entregar)

### IMPORTANTE: Docker tiene su propia base de datos separada
Cuando corres el proyecto con Docker por primera vez, la base de datos del contenedor
esta vacia. Debes aplicar migraciones DENTRO del contenedor.

### Paso 1: Levantar el contenedor

Desde la carpeta raiz del proyecto (donde esta docker-compose.yml):
```bash
docker compose up --build
```

Esperar hasta ver este mensaje en la terminal:
```
web-1 | Starting development server at http://0.0.0.0:8000/
```

### Paso 2: Aplicar migraciones (en una segunda terminal)
```bash
docker compose exec web python backend/manage.py migrate
```

### Paso 3: Crear superusuario dentro del contenedor
```bash
docker compose exec web python backend/manage.py createsuperuser
```

### Paso 4: Abrir en el navegador
```
http://localhost:8000/api/todos/
http://localhost:8000/admin/
```

### Otros comandos utiles con Docker

Correr cualquier comando de Django dentro del contenedor:
```bash
docker compose exec web python backend/manage.py <comando>
```

Ver los logs del contenedor en tiempo real:
```bash
docker compose logs -f
```

Detener el contenedor:
```bash
docker compose down
```

Detener el contenedor Y borrar los volumenes (reset total de BD):
```bash
docker compose down -v
```
```

---

**`.gitignore`** (en la raíz de `todoapp/`):
```
# Virtual environment
.venv/

# Python cache
__pycache__/
*.pyc

# Local database
db.sqlite3

# Environment variables
.env