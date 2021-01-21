FROM python:3.9.0

WORKDIR /home/

RUN echo "test7"

RUN echo "test6"

RUN git clone https://github.com/PyungkangHong094/blogProject.git

WORKDIR /home/blogProject/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=3$!%244a&8y$d*dx!85id8%i8z_*00^ub@czh-*)3q+xa%xf_i" > .env

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]