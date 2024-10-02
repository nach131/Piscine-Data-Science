# Especificar la imagen base
FROM python:3.12.4-alpine3.19
LABEL maintainer="42Barcelona"

# Establecer variables de entorno
ENV PYTHONUNBUFFERED=1

# Crear directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requerimientos al contenedor
COPY ./requirements.txt /tmp/requirements.txt

# Instalar dependencias y eliminar las librerías temporales
RUN pip install --upgrade pip setuptools && \
	apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev \
	postgresql-dev \
	# Dependencias para compilar psycopg2 y otras librerías \
	&& pip install -r /tmp/requirements.txt \
	&& apk del .build-deps  # Eliminar las dependencias de compilación para reducir tamaño \
	&& rm -rf /var/cache/apk/* /tmp/requirements.txt

# Copiar todo el contenido del proyecto al directorio de trabajo en el contenedor
# COPY . .


# Mantener el contenedor en ejecución para desarrollo (este comando puede cambiar en producción)
CMD ["tail", "-f", "/dev/null"]
