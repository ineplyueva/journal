Journal
=======

Requirements
------------

  django
  mysql
  mysql-python
  uwsgi

Install
------------
  mysql:
  CREATE DATABASE journal;
  GRANT ALL PRIVILEGES ON journal.* TO 'journal'@'localhost' IDENTIFIED BY 'journal';
  
  pip install -U -r requirements.txt
  python ./manage.py makemigrations
  python ./manage.py migrate
