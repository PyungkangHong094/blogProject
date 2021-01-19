FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/PyungkangHong094/blogProject.git

WORKDIR /home/blogProject/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=3$!%244a&8y$d*dx!85id8%i8z_*00^ub@czh-*)3q+xa%xf_i" > .env

RUN echo "test1"

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "blogProject.wsgi", "--bind", "0.0.0.0:8000"]