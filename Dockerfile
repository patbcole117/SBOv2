FROM python:alpine3.7
COPY . /SBO
WORKDIR /SBO
RUN pip install -r requirements.txt
EXPOSE 50100
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]