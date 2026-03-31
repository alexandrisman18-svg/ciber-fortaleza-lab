FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install .
CMD ["python", "src/main/python/inventory.py"]
