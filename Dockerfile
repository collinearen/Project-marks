FROM python:3.10.13-bookworm

EXPOSE 8000

RUN apt update && apt install libmariadb-dev g++ -y

COPY share/reqi.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir /app && \
    mkdir /logs

COPY ./share /app 
WORKDIR /app 

RUN python3 manage.py collectstatic --noinput

CMD [ "gunicorn", "--env", "DJANGO_SETTINGS_MODULE=share.settings", "-b", "0.0.0.0:8000", "share.wsgi" ]
