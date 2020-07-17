FROM python:3.8-slim
LABEL maintainer="ckretler@umich.edu"

#RUN apt-get update -y

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /src .
RUN chmod g+r -R wsgi.py ./welcome

EXPOSE 8000

CMD ["gunicorn", "-c", "guniconf.py", "wsgi:application"]
