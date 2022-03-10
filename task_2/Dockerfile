FROM python:3.10

RUN mkdir /usr/src/django_api 
WORKDIR /usr/src/django_api

COPY . /usr/src/django_api 

RUN pip install -r requirements.txt
ENV SECRET_KEY='JASLDKJKJDBVFJKVBFDJVBFDJHVBBAJVBLKJDFVJKSDFHGJK' DEBUG=False
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
