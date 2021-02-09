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

```sh
$ mkdir eshopreport
$ cd eshopreport
$ git clone git@github.com:m-c-hill/eshop-report-suade-test.git
$ python run.py
```

Open http://127.0.0.1:5000/ and enter a date to generate a report.

Requirements
------------
Python version: 3.9

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
**run.py**:<br />
Runs the Flask app<br /><br />

**\_\_init\_\_.py**<br />
Sets up the Flask app<br /><br />

**generate_data.py**<br />
Generates the data for the Flask sqlite database (eshopreport/eshop.db) by importing data from each csv file in eshopreport/data. This is only run for testing purposes to initially import the data or reset the database.<br /><br />

**models.py**<br />
Contains the models required for the eshopreport app. Each class which extends db.Model represents a unique table in the database. 
The final class, ReportForDate, generates the necessary report statistics for this project. A seperate static method is used for each statistic, which in turn creates an SQL script using sqlalchemy to query the database.<br /><br />

**routes.py**<br />
Routes for eshop report application.<br /><br />

**test_report.py**<br />
Unit testing for the get_statistic methods in class ReportForDate in module models.<br /><br />

**eshop.db**<br />
Database containing the tables: order, order_line, product, promotion, product_promotion & vendor_commission.<br /><br />


Testing
-------
To run the unit testing for this application, within the eshopreport driectory:

```sh
$ cd tests
$ python test_report.py
```

This will run seven tests for the date 02-Aug-2019. Each test compares a seperate stastic from the report (calculcated by a corresponding method from the class ReportForDate in models.py) and compares it to a value calculated by hand.
