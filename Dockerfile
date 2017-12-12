FROM python:2.7.14
MAINTAINER Chris Kretler "ckretler@umich.edu"

RUN apt-get update -y

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

#RUN chown -R www-data:www-data /app

EXPOSE 8000

#USER www-data

CMD ["gunicorn", "-c", "guniconf", "wsgi:application"]
