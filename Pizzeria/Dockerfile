FROM python:3.9.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

# Define environment variables
ENV DJANGO_SETTINGS_MODULE=myproject.settings


# Run server
CMD ["./start.sh"]
