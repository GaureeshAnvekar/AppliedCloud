FROM python:3.8-slim-buster

#WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#COPY . .

VOLUME /app
WORKDIR /app
EXPOSE ${API_PORT}
ENTRYPOINT [ "python3" ]
CMD ["api1.py" ]
# CMD ["python3"]
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]