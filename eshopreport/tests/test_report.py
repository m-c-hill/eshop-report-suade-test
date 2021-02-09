"""
test_report.py: unit testing for static methods in class ReportForDate in module models
"""

import unittest
from datetime import datetime
from eshopreport.models import ReportForDate


class TestReportForDate(unittest.TestCase):
    test_date = datetime(2019, 8, 2).date()

    # Note: all expected values were manually calculated by hand and rounded to a suitable level of accuracy.

    def test_get_total_items(self):
        """
        Test: ReportForDate.get_total_items is called with test date 2-Aug-2019.
        Verification: Should return the value 3082.
        """
        total_items = ReportForDate.get_total_items(self.test_date)
        self.assertEqual(total_items, 3082)

    def test_get_total_customers(self):
        """
        Test: ReportForDate.get_total_customers is called with test date 2-Aug-2019.
        Verification: Should return the value 10.
        """
        total_customers = ReportForDate.get_total_customers(self.test_date)
        self.assertEqual(total_customers, 10)

    def test_get_total_discount(self):
        """
        Test: ReportForDate.get_total_discount is called with test date 2-Aug-2019.
        Verification: Should return the value 20061245.64 (accurate to 2DP).
        """
        total_items = ReportForDate.get_total_discount(self.test_date)
        self.assertEqual(round(total_items, 2), 20061245.64)

    def test_get_avg_discount_rate(self):
        """
        Test: ReportForDate.get_avg_discount_rate is called with test date 2-Aug-2019.
        Verification: Should return the value 0.12950211 (accurate to 8DP).
        """
        avg_discount_rate = ReportForDate.get_avg_discount_rate(self.test_date)
        self.assertEqual(round(avg_discount_rate, 8), 0.12950211)

    def test_get_avg_order_total(self):
        """
        Test: ReportForDate.get_avg_order_total is called with test date 2-Aug-2019.
        Verification: Should return the value 16499829.58 (accurate to 2DP).
        """
        avg_order_total = ReportForDate.get_avg_order_total(self.test_date)
        self.assertEqual(round(avg_order_total, 2), 16499829.58)

    def test_get_total_commissions(self):
        """
        Test: ReportForDate.get_total_commissions is called with test date 2-Aug-2019.
        Verification: Should return the value £22358623.33 (accurate to 2DP).
        """
        total_commissions = ReportForDate.get_total_commissions(self.test_date)
        self.assertEqual(round(total_commissions, 2), 22358623.33)

    def test_get_avg_commissions_per_order(self):
        """
        Test: ReportForDate.get_avg_commissions_per_order is called with test date 2-Aug-2019.
        Verification: Should return the value £2235862.33 (accurate to 2DP).
        """
        avg_commissions_per_order = ReportForDate.get_avg_commissions_per_order(self.test_date)
        self.assertEqual(round(avg_commissions_per_order, 2), 2235862.33)


if __name__ == '__main__':
    unittest.main()