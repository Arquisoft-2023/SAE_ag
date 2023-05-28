#!/bin/bash
cd /home/jordan_esc/Proyectos/1d_ag/SAE_ag
source virtualenv/bin/activate
sudo docker compose down
sudo docker rmi sae_ag:latest
sudo docker compose up