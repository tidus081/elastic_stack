#!/bin/bash

# Install elasticsearch, kibana and logstash.
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

apt install logstash

TARGET="logstash-simple.conf"
LOG_LOCATION="$(pwd)"/"logFile.txt"
sed -i "s#temp_path#$LOG_LOCATION#" $TARGET
cp "logstash-simple.conf" "/etc/logstash/conf.d/logstash-client.conf"

-u logstash /usr/share/logstash/bin/logstash --path.settings /etc/logstash -f /etc/logstash/conf.d/logstash-simple.conf --config.test_and_exit
