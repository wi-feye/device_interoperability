FROM python:3.8
LABEL maintainer="Wi-Feye"
LABEL version="1.0"
LABEL description="Wi-Feye device interoperability microservice"

# copying the environment
COPY . /app

# setting the workdir
WORKDIR /app

# installing all requirements
RUN ["pip3", "install", "-r", "requirements.txt"]

# exposing the port
EXPOSE 10007/tcp

# main command
# CMD ["python3", "-m", "flask", "--app", "src", "run", "-p", "10001", "--host=0.0.0.0"]
CMD ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]