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
ENV PORT=3121
ENV URI=127.0.0.8
EXPOSE 3121

CMD [ "python", "./src/App.py" ]