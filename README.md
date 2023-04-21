# SAE ApiGateway

Proyecto Sistema de Acompañamiento Estudiantil (SAE) en la facultad de medicina de la Universidad Nacional de Colombia - Sede Bogotá

# Autor

Sebastián Hernández Cerón

# Variables de entorno Archivo Env

PORT = 80 #TCP

URI = 0.0.0.0

# Pasos

1 Crear un entorno de desarrollo virtual

    python -m venv virtualenv

    ./virtualenv/bin/activate
    source virtualenv/bin/activate  -- en linux

2 Instalar dependencias

    pip install -r requirements.txt

Para actualizar el archivo requirements.txt

    pip freeze > requirements.txt

3 Configurar variables de entorno y server

4 Para ejecutar usar

    python ./src/App.py

# Dockerizar - comandos

1 Construir imagen

    docker build --no-cache -t sae_ag .

2 Correr contenedor

    docker run -p 3121:80 --name sae_ag sae_ag


# Comandos de despliegue con docker-compose

1 Si no se ha creado la red de docker para los microservicios, ejecutar el siguiente comando:

    docker network create nodes-networks

2 Contruir y ejecutar el contenedor:

    docker-compose build --no-cache

    docker-compose up

3 Detener el contenedor:
    
    docker-compose down