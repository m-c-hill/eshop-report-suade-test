eShop Report
==============================

What is this?
-------------
A basic Flask application to generate a report with the following statistics for an eshop on a given date:

* The total number of items sold on that day.
* The total number of customers that made an order that day.
* The total amount of discount given that day.
* The average discount rate applied to the items sold that day.
* The average order total for that day
* The total amount of commissions generated that day.
* The average amount of commissions per order for that day

The user has the option to input a date on the application's homepage, which then returns a table containing the above statistics.

How to run the application
--------------------------
In your terminal:
$ mkdir eshopreport
$ cd eshopreport
$ git clone git@github.com:m-c-hill/eshop-report-suade-test.git
$ python run.py

Open http://127.0.0.1:5000/ and enter a date to generate a report.

Requirements
------------
Python 3.9

Packages used in this project include:
* datetime
* flask
* flask_sqlalchemy
* sqlalchemy
* pandas
* statistics
* unittest

Please ensure all packages are installed in your environment before running the application.

Project Structure
-----------------


Testing
-------

