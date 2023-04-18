FROM python:3

#Creat app directory
RUN mkdir -p sae/sae_ag
WORKDIR /sae/sae_ag

#Install app dependencies
COPY requirements.txt /sae/sae_ag/
RUN pip install --no-cache-dir -r requirements.txt

#Bundle app source
COPY . /sae/sae_ag/

#Servidor
ENV PORT=80
ENV URI=0.0.0.0

EXPOSE 80

CMD ["python", "./src/App.py"]