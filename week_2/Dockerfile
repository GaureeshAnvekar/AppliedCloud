FROM python:latest AS build
RUN apt-get update
RUN apt-get install wget
ARG username=root
RUN useradd $username
RUN mkdir notebooks
RUN wget https://raw.githubusercontent.com/GaureeshAnvekar/AppliedCloud/main/week_2/Interactive3DPlot.ipynb -P ./notebooks/
RUN chown $username:$username notebooks
RUN chmod u+w notebooks