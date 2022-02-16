FROM python:latest
COPY . .
RUN pip3 install flask
RUN pip install requests
EXPOSE 8000
ENTRYPOINT [ "python3","Sample.py" ]
