#!/usr/bin/env bash
#this script sets up the web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

sudo echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#sudo ln -sf /data/web_static/releases/test current

sudo chown -R ubuntu:ubuntu /data/

#sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;' /etc/nginx/sites-available/default
sudo sed -i '/listen 80 default_server/a\    location \/hbnb_static {\n        alias \/data\/web_static\/current\/;\n    }' /etc/nginx/sites-available/default

sudo service nginx restart
