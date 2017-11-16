FROM python:2.7.14-slim
MAINTAINER Chris Kretler "ckretler@umich.edu"

RUN apt-get update -y

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN chown -R www-data:www-data /app

# Mount sqllite database as a (file) volume
# VOLUME [ "/app/db.sqlite3" ]

EXPOSE 8000

USER www-data

# simple but dumb
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# simple but wiser
CMD ["gunicorn", "-c", "guniconf", "wsgi:application"]
