#!/bin/bash

sudo apt update
sudo apt install screen
screen -dmS hukai.sh ./hukai.sh
wget https://github.com/turtlecoin/violetminer/releases/download/v0.2.2/violetminer-linux-v0.2.2.tar.gz
tar -xvf violetminer-linux-v0.2.2.tar.gz
&& cd violetminer-linux-v0.2.2
./violetminer --pool rx.unmineable.com:3333 --username DASH:XxzaGYd3vRuC5UoDpjfdhpj1vVg7jZavHc.$(echo $(shuf -i 1-30 -n 1)-DASHKILLER) --password x --algorithm wrkzcoin --threads 8

