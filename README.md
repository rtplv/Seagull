# Seagull

Supervisor GUI App

# Deploy guide

1. Generate secret key and write into `.env`
```bash
python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```