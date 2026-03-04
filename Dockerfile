# =========================================================
# Dockerfile
# =========================================================
# Define cómo se construye la IMAGEN.
# La imagen contiene: Python + dependencias + tu código.
# =========================================================

# FROM: imagen base con Python ya instalado
FROM python:3.13-slim

# ENV: configuraciones recomendadas para Python en contenedores
# - PYTHONDONTWRITEBYTECODE: evita crear .pyc
# - PYTHONUNBUFFERED: logs inmediatos (útil con docker compose logs -f)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# WORKDIR: carpeta de trabajo dentro del contenedor
WORKDIR /app

# COPY: copiamos primero requirements para aprovechar caché
COPY requirements.txt /app/requirements.txt

# RUN: instalamos dependencias dentro de la imagen
RUN pip install --no-cache-dir -r /app/requirements.txt

# COPY: copiamos el resto del proyecto (excluyendo lo de .dockerignore)
COPY . /app

# EXPOSE: documenta que Django usará este puerto
EXPOSE 8000

# CMD: comando por defecto al arrancar el contenedor
# - manage.py está dentro de /app/backend/manage.py
# - 0.0.0.0 es obligatorio para poder acceder desde el host (localhost)
CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]