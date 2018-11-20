# gwt_auth
Authentication server and database for groundwater Rapid Assessment Tool

## Installation
### install system requirements for geodjango
`sudo apt-get install binutils libproj-dev gdal-bin postgis`

### install source code requirements
`pip install -r requirements.txt`

### create database
`sudo -u postgres createuser <user> --interactive`\
`createdb gwt`\
`psql gwt`\
`gwt# create extension postgis;`\
`gwt# create extension postgis_topology;`\
`^D`

### secret keys
download or create gwtauth/secrets.py with the following keys:\
`SECRET_KEY`\
`DATABASES`\
`CORS_ORIGIN_ALLOW_ALL=True` or\
`CORS_ORIGIN_WHITELIST`

### initialize database
`python manage.py migrate`\
`python manage.py createsuperuser`\
`python manage.py loaddata wms.json`\
`python manage.py loaddata gwt.json`



