#!/bin/bash

# Statics
# Install elasticsearch and kibana.
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch |  apt-key add -
echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" |  tee -a /etc/apt/sources.list.d/elastic-6.x.list
apt update
apt install elasticsearch

# Remove # to open localhost
TARGET="/etc/elasticsearch/elasticsearch.yml"
sed -i 's/#network: localhost/network: localhost/' $TARGET
sed -i 's/#http.port: 9200/http.port: 9200/' $TARGET

systemctl start elasticsearch
systemctl enable elasticsearch

apt install kibana
systemctl start kibana
systemctl enable kibana

systemctl restart elasticsearch kibana