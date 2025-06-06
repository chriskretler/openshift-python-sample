FROM python:3.13-alpine
LABEL maintainer="ckretler@umich.edu"

ENV build-date=06june2025

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN mkdir -p /app/staticfiles
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "-c", "guniconf.py", "sample-app.wsgi"]
