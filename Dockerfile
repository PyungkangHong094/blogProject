FROM python:3.9.0

WORKDIR /home/

RUN echo "django_image_cube15"

RUN git clone https://github.com/PyungkangHong094/blogProject.git

WORKDIR /home/blogProject/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput && python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]