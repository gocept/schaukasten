Backend
=======

Install postgres if needed and a new database:

$ createdb schaukasten

$ virtualenv3.5 .
$ source bin/activate
$ pip install -r requirements.txt
$ pserve development.ini

Frontend
========

$ npm install
$ grunt
$ grunt phantomjs
