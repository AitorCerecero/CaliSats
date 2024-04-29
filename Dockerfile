FROM python:latest
WORKDIR /app
COPY . .
CMD ["python", "CalicoSat.py"]
