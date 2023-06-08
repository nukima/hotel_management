# Nhom 1 - He thong thong tin quan ly

## Setup python
```pip install -r requirements.txt```

## Setup database
```mysql -u <mysql-username> -p<mysql-password> < hms.sql```
Or import hms.sql file to mysql database

## Add database credentials to the app
Start by renaming the .example.env file just .env, and then replacing the Your-Username and Your-Password values with the MySQL credentials.

## Run
```python main.py```