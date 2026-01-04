# 1. imagen de python
FROM python:3.10-slim

# 2. directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. archivo de requerimientos
COPY requirements.txt .

# 4. instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. copiamos todo el código de nuestro proyecto al contenedor
COPY . .

# 6. exponemos el puerto que usará FastAPI
EXPOSE 8000

# 7. comando para iniciar la API con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]