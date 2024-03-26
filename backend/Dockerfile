# Utiliza una imagen oficial de Python como imagen base
FROM python:3.12.2-bookworm

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Install a virtual environment
RUN apt-get update && apt-get install -y virtualenv
RUN virtualenv env
# Set the virtual environment as the current location
ENV PATH="/app/env/bin:$PATH"

# Instala las dependencias de Python
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copia el proyecto Django al directorio de trabajo en el contenedor
COPY manage.py /app/
COPY blog /app/blog/
COPY appBlog /app/appBlog/
COPY db.sqlite3 /app/

# Ejecuta el servidor de desarrollo de Django
# Nota: No usar en producción, en su lugar usar Gunicorn o uWSGI
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

