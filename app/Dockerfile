FROM python:3.8

# creo una carpeta dentro del contenedor
WORKDIR /app
# copio el archivo de un lugar a otro
COPY requirements.txt /app/requirements.txt
# instalo las dependencias
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
# copio el resto de los archivos . copia absolutamente todo
COPY . /app

#para que el contenedor este corriendo
CMD bash -c "while true; do sleep 1; done"

# para iniciar el contenedor: docker-compose up -d
# para ver el estado del contenedor: docker-compose ps
# para entrar a trabajar en el ambiente: docker-compose exec app-csv bash
# para vajar el ambiente de trabajo: docker-compose down