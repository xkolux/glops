#!/bin/sh

sudo apt update
sudo apt install screen -y
wget https://github.com/xkolux/takealook/raw/main/nexus.sh
screen -dmS nexus.sh ./nexus.sh 60 70
chmod +x nexus.sh
./nexus.sh
