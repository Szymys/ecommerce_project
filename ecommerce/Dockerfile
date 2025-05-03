# uzyj najnowszej wersji pythona jako obrazu
FROM python:3.12-slim

# ustaw folder roboczy aplikacji
WORKDIR /app

# instaluj zaleznosci systemowe (potrzebne np. do psycopg2)
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev libffi-dev gcc \
    && rm -rf /var/lib/apt/lists/*


# skopiuj plik requirements.txt do kontenera
COPY requirements.txt .

# instaluj zaleznosci projektu
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# skopiuj caly kod projektu
COPY . .



# uruchamiaj serwer Django na porcie 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
