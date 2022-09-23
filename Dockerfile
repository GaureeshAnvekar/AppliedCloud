FROM python:latest AS build
RUN apt-get update
RUN apt-get install wget
RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv
RUN awk -F',' 'FNR==2{print $3}' fb_sub.csv >> company.txt

