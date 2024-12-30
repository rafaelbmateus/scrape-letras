FROM python:3.10-slim

WORKDIR /app

COPY script.py /app/script.py

RUN pip install requests beautifulsoup4

ENTRYPOINT ["python", "script.py"]
