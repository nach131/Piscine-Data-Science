# Especificar la imagen base
FROM jupyter/minimal-notebook:x86_64-ubuntu-22.04
# FROM jupyter/minimal-notebook:latest
LABEL maintainer="42BarcelonaJupyter"

WORKDIR /home/jovyan/work

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip setuptools && \
    pip install -r /tmp/requirements.txt
# rm -rf /tmp/requirements.txt
