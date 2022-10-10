 - To build the database admin image from Docker local. docker build -t mydba .

 - To run the database admin container docker run --name mydba --network mynetwork -p 8080:81 -d mydba

 - To build the database image from Docker local docker build -t mydb .

 - To run the database container from the local docker run --name mydb --network mynetwork -itd -p5432:5432 mydb

 - To build the django app image from docker local docker build -t mydjango .

 - To run the django app conaitner docker run -it -p8000:8000 -v "$(pwd)/app:/app" mydjango /bin/bash



//App docker file\
FROM python\
COPY requirements.txt /tmp/\
RUN pip3 install -r /tmp/requirements.txt\
VOLUME /app\
WORKDIR /app\

EXPOSE 8000\


//db docker file\
FROM postgres:12.12\
ENV POSTGRES_USER=root\
ENV POSTGRES_PASSWORD=pass\
ENV POSTGRES_DB=web\
EXPOSE 5432\

//dba docker file\
FROM dpage/pgadmin4\
ENV PGADMIN_DEFAULT_EMAIL=admin@admin.com\
ENV PGADMIN_DEFAULT_PASSWORD=pass\
EXPOSE 80\
