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

3. Run `install.sh` as `sudo`:
```
sudo ./install.sh
```

4. It's all! App running on 0.0.0.0:9002
