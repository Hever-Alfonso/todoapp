# todoapp

Tutorial 04 - Django REST Framework | Arquitectura de Software EAFIT

Aplicación ToDo con API REST construida con Django y Django REST Framework.

## Estructura del proyecto
```
todoapp/
├── backend/
│   ├── backend/          # Configuración del proyecto Django
│   │   ├── settings.py
│   │   └── urls.py
│   ├── todo/             # App con el modelo ToDo
│   │   ├── models.py
│   │   └── admin.py
│   ├── api/              # App con la API REST
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   └── manage.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── COMMANDS.md
└── README.md
```

## Endpoints disponibles

| Método | URL | Descripción | Auth |
|--------|-----|-------------|------|
| POST | /api/signup/ | Registrar usuario, retorna token | No |
| POST | /api/login/ | Autenticar usuario, retorna token | No |
| GET | /api/todos/ | Listar tareas del usuario | Token |
| POST | /api/todos/ | Crear nueva tarea | Token |
| GET | /api/todos/<pk> | Detalle de una tarea | Token |
| PUT | /api/todos/<pk> | Actualizar una tarea | Token |
| DELETE | /api/todos/<pk> | Eliminar una tarea | Token |
| PUT | /api/todos/<pk>/complete | Invertir estado completed | Token |

## Autenticación

La API usa autenticación por token. Incluye el token en el header:
```
Authorization: Token <tu_token>
```

## Correr con Docker
```bash
docker compose up --build
```

En segunda terminal:
```bash
docker compose exec web python backend/manage.py migrate
docker compose exec web python backend/manage.py createsuperuser
```

Ver COMMANDS.md para más detalles.