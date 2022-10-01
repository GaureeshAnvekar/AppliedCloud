FROM python:latest AS build
RUN apt-get update
RUN apt-get install wget
ARG username=Gaurish
ENV username $username
RUN useradd -m $username
RUN mkdir /home/$username/notebooks
RUN wget https://raw.githubusercontent.com/GaureeshAnvekar/AppliedCloud/main/week_2/Interactive3DPlot.ipynb -P ./home/$username/notebooks/
RUN wget https://raw.githubusercontent.com/GaureeshAnvekar/AppliedCloud/main/week_2/Requirements.txt -P ./home/$username/notebooks/
RUN chown $username:$username ./home/$username/notebooks/*
RUN chmod u+w ./home/$username/notebooks/*
RUN pip3 install -r ./home/$username/notebooks/Requirements.txt
RUN su $username
WORKDIR /home/${username}/notebooks/
#RUN jupyter-lab ./home/$username/notebooks/Interactive3DPlot.ipynb --ip 0.0.0.0 --no-browser --allow-root
#ENTRYPOINT ["jupyter", "lab", "--ip=0.0.0.0", "--allow--root","./home/Gaur/notebooks/Interactive3DPlot.ipynb"]
# "./home/Gaur/notebooks/Interactive3DPlot.ipynb", "--ip 0.0.0.0  --allow-root"]
EXPOSE 8888
ENTRYPOINT ["jupyter", "lab","./Interactive3DPlot.ipynb", "--ip=0.0.0.0","--allow-root"]