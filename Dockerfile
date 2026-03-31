FROM python:3.13-slim

WORKDIR /app

# Copiamos todo el código al contenedor
COPY . .

# Instalamos Flask (si tu app lo usa) o cualquier dependencia necesaria
# Si no usas librerías externas, puedes comentar la siguiente línea
# RUN pip install flask 

# Ejecutamos el validador para demostrar que el código está ahí
CMD ["python", "src/main/python/validator.py"]
