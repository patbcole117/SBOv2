FROM python:alpine3.7
COPY . /sbo
WORKDIR /sbo
RUN pip install -r requirements.txt
RUN pip install gunicorn
CMD [ "gunicorn", "--workers", "1", "--bind", "0.0.0.0:80", "run:app" ]