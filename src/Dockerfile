FROM python:3.10-slim
LABEL maintainer="ckretler@umich.edu"

ENV build-date 24apr2023a

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN chmod g+r -R sample-app/wsgi.py ./welcome

EXPOSE 8000

CMD ["gunicorn", "-c", "guniconf.py", "sample-app.wsgi"]
