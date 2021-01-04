FROM python:alpine3.7
COPY . /sbo
WORKDIR /sbo
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]