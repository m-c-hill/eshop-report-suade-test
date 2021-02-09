"""
routes.py: routes for eshop report application
"""

from flask import render_template, request
from eshopreport import app
from eshopreport import models
from datetime import datetime


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Convert the user input string to datetime date object
            date = datetime.strptime(request.form["dt"], "%Y-%m-%d").date()
            try:
                # Create a report for this date and assign variables for the table in "results.html"
                report_results = models.ReportForDate(date).get_all_results()
                return render_template('results.html',
                                       date=date,
                                       total_items=report_results["total_items"],
                                       total_customers=report_results["total_customers"],
                                       total_discount=round(report_results["total_discount"],2),
                                       avg_discount_rate=round(report_results["avg_discount_rate"] * 100, 2),
                                       avg_order_total=round(report_results["avg_order_total"], 2),
                                       total_commissions=round(report_results["total_commissions"], 2),
                                       avg_commissions_per_order=round(report_results["avg_commissions_per_order"], 2))
            except IndexError:
                # If no data exists for this date, this error message is generated:
                message = "No data for this date."
                return render_template('home.html', msg=message)
        except ValueError:
            # If the submit button is hit without a date having been entered, this error message is generated:"
            message = "Please enter a date before submitting"
            return render_template('home.html', msg=message)
    else:
        return render_template('home.html')
