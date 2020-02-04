FROM python:3.8
LABEL maintainer="ckretler@umich.edu"

#RUN apt-get update -y

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

#RUN chown -R www-data /app
#USER www-data
RUN chmod g+r -R wsgi.py ./welcome

EXPOSE 8000

CMD ["gunicorn", "-c", "guniconf.py", "wsgi:application"]
