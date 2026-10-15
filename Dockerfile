# Vulnerability 6: Using latest tag instead of a specific SHA or version
FROM python:latest

# Vulnerability 7: Running as root (No USER instruction provided)
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

# Vulnerability 8: Exposing sensitive ports without explicit need (contextual warning)
EXPOSE 5000

CMD ["python", "app.py"]
