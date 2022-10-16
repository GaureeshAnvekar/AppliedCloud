FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#COPY . .

VOLUME /app
WORKDIR /app

#ENTRYPOINT [ "python3" ]

EXPOSE ${API_PORT}

CMD ["python3", "api.py" ]
# CMD ["python3"]
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]