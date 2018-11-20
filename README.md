# gwt_auth
Authentication server and database for groundwater Rapid Assessment Tool

## Installation
### install system requirements for geodjango
`sudo apt-get install binutils libproj-dev gdal-bin postgis`

### install source code
`pip install -r requirements.txt`

### create database
`sudo -u postgres createuser <user> --interactive`\
`createdb gwt`\
`psql gwt`\
`gwt# create extension postgis;`\
`gwt# create extension postgis_topology;`\
`^D`

### initialize database
`python manage.py migrate`\
`python manage.py createsuperuser`\
`python manage.py loaddata wms.json`\
`python manage.py loaddata gwt.json`\



