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
├── eshop-report-suade-test
    │   ├── README
    │   ├── run.py
    │   └── eshopreport
    │       ├── __init__.py
    │       ├── eshop.db
    │       ├── generate_data.py
    │       ├── models.py
    │       ├── routes.py
    │       ├── templates (contains html files to render)
    │       └── tests
    │           └── test_report.py


Testing
-------
To run the unit testing for this application, within the eshopreport driectory:

```sh
$ cd tests
$ python test_report.py
```

This will run seven tests for the date 02-Aug-2019. Each test compares a seperate stastics from the report (calculcated by a corresponding method from the class ReportForDate in models.py) and compares it to a value calculated by hand.
