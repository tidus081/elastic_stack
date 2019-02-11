#!/bin/bash

# Statics
aot update
apt install python3-pip
pip3 install python-logstash
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list
apt-get update && sudo apt-get install logstash

cp "logstash-simple.conf" "/etc/logstash/conf.d/logstash-client.conf"

-u logstash /usr/share/logstash/bin/logstash --path.settings /etc/logstash -f /etc/logstash/conf.d/logstash-client.conf --config.test_and_exit
