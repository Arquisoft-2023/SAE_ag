# SAE ApiGateway
Proyecto Sistema de Acompañamiento Estudiantil (SAE) en la facultad de medicina de la Universidad Nacional de Colombia - Sede Bogotá

# Autor
Sebastián Hernández Cerón

# Variables de entorno Archivo Env
PORT = 8001 #TCP

URI = 127.0.0.1

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
