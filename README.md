# Seagull

Supervisor GUI App

# Deploy guide

1. Go to home directiory and clone repo:
```
cd ~
git clone https://github.com/rtplv/Seagull.git .seagull
```

2. Generate secret key and write into `.env`
```bash
python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

3. Run next commands:
```bash
# Project
python3 -m venv ./venv
./venv/bin/pip install -r requirements.txt
mkdir logs

# Warning. Change user into conf on your's
cp ./seagull-serv.conf /etc/supervisor/conf.d/seagull-serv.conf 
supervisorctl update all

# Nginx
cp ./nginx.conf /etc/nginx/sites-available/seagull-serv.conf 
ln -s /etc/nginx/sites-available/seagull-serv.conf /etc/nginx/sites-enabled/seagull-serv.conf 
sudo service nginx reload
```

4. It's all! App running on 0.0.0.0:9002
