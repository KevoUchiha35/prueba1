FROM python:3.8

# set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code


COPY requirements.txt .
# install python dependencies
RUN pip install  -r requirements.txt

# Copia el contenido de tu proyecto al contenedor
COPY . .
