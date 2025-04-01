# Usa una imagen base de Python 3.9 (o la versión que prefieras)
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia todo el código fuente al contenedor
COPY . .

# Instala las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que FastAPI estará escuchando (por defecto FastAPI usa el puerto 8000)
EXPOSE 8000

# Comando para iniciar la aplicación FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]