//App docker file
FROM python
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
VOLUME /app
WORKDIR /app

EXPOSE 8000


//db docker file
FROM postgres:12.12
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=pass
ENV POSTGRES_DB=web
EXPOSE 5432

//dba docker file
FROM dpage/pgadmin4
ENV PGADMIN_DEFAULT_EMAIL=admin@admin.com
ENV PGADMIN_DEFAULT_PASSWORD=pass
EXPOSE 80
