#!/bin/bash
bash
python3 -m venv ./venv
./venv/bin/pip install -r requirements.txt
mkdir ./logs
cp ./seagull-serv.conf /etc/supervisor/conf.d/seagull-serv.conf
supervisorctl update all
