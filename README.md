## production settings ⬇️

### Installation Packages

```bash
pip install requirements.txt
```

###requirements
```
mysql   =====> main database
```

### ALLOWED_HOSTS
```
change ALLOWED_HOSTS list in core/settings.py
```

###env
```bash
# django DEBUG
$DEBUG = 'False' or 'True'

# postgresql database config
$DATABASE_NAME = ...
$DATABASE_USER = ...
$DATABASE_PASSWORD = ...
$DATABASE_URL = ...

```

### Migrate
```bash
python3 manage.py migrate
```

