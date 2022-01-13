FROM python:latest
COPY . .
EXPOSE 6001
ENTRYPOINT [ "python3","app.py" ]