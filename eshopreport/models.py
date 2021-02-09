"""
models.py: Module containing the models required for the eshopreport app. Each class which extends db.Model
represents a unique table in the database. The final class, ReportForDate, generates the necessary report statistics
for this project.
"""

from datetime import datetime
from eshopreport import db
from sqlalchemy import func
import statistics


class Order(db.Model):
    __tablename__ = 'orders'

    id_ = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, nullable=False, default=datetime.utcnow().date())
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor_commissions.vendor_id'), nullable=False)
    customer_id = db.Column(db.Integer, nullable=False)  # Foreign key if a customer class is created in the future
    order_lines = db.relationship('OrderLine', backref='order', lazy=True)

    def __init__(self, id_, created_at, vendor_id, customer_id):
        self.id_ = id_
        self.created_at = created_at
        self.vendor_id = vendor_id
        self.customer_id = customer_id

    def __repr__(self):
        return f"Order('{self.id_}', '{self.created_at}', '{self.vendor_id}', '{self.customer_id}')"


class OrderLine(db.Model):
    __tablename__ = 'order_line'

    id_ = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id_'), db.ForeignKey('product_promotion.product_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id_'), nullable=False)
    product_description = db.Column(db.String(200), nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    product_vat_rate = db.Column(db.Float, nullable=False)
    discount_rate = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    full_price_amount = db.Column(db.Float, nullable=False)
    discounted_amount = db.Column(db.Float, nullable=False)
    vat_amount = db.Column(db.Float, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)

    def __init__(self, order_id, product_id, product_description, product_price, product_vat_rate, discount_rate,
                 quantity, full_price_amount, discounted_amount, vat_amount, total_amount):
        self.order_id = order_id
        self.product_id = product_id
        self.product_description = product_description
        self.product_price = product_price
        self.product_vat_rate = product_vat_rate
        self.discount_rate = discount_rate
        self.quantity = quantity
        self.full_price_amount = full_price_amount
        self.discounted_amount = discounted_amount
        self.vat_amount = vat_amount
        self.total_amount = total_amount

    def __repr__(self):
        return f"OrderLine({self.id_}, {self.order_id}, {self.product_id}, '{self.product_description}', " \
               f"{self.product_price}, {self.product_vat_rate}, {self.discount_rate}, {self.quantity}, " \
               f"{self.full_price_amount}, {self.discounted_amount}, {self.vat_amount}, {self.total_amount})"


class Product(db.Model):
    __tablename__ = 'products'

    id_ = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    order_lines = db.relationship('OrderLine', backref='product', lazy=True)
    promotion = db.relationship('ProductPromotion', backref='product', lazy=True)

    def __init__(self, id_, description):
        self.id_ = id_
        self.description = description

    def __repr__(self):
        return f"Product({self.id_}, '{self.description}')"


class Promotion(db.Model):
    __tablename__ = 'promotion'

    id_ = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    product_promotion = db.relationship('ProductPromotion', backref='promotion', lazy=True)

    def __init__(self, id_, description):
        self.id_ = id_
        self.description = description

    def __repr__(self):
        return f"Promotion({self.id_}, '{self.description}')"


class ProductPromotion(db.Model):
    __tablename__ = 'product_promotion'

    id_ = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id_'))
    date = db.Column(db.DATE, nullable=False)
    promotion_id = db.Column(db.Integer, db.ForeignKey('promotion.id_'), nullable=False)
    order_lines = db.relationship('OrderLine', backref='orderline', lazy=True)

    def __init__(self, product_id, date, promotion_id):
        self.product_id = product_id
        self.date = date
        self.promotion_id = promotion_id

    def __repr__(self):
        return f"ProductPromotion({self.product_id}, {self.date}, {self.promotion_id})"


class VendorCommissions(db.Model):
    __tablename__ = 'vendor_commissions'

    vendor_commissions_id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer)
    date = db.Column(db.DATE, nullable=False)
    rate = db.Column(db.FLOAT, nullable=False)
    order = db.relationship('Order', backref='vendor_commission', lazy=True)

    def __init__(self, vendor_id, date, rate):
        self.vendor_id = vendor_id
        self.date = date
        self.rate = rate

    def __repr__(self):
        return f"VendorCommissions({self.vendor_id}, {self.date}, {self.rate})"


class ReportForDate:
    """Class to represent an eshop report which analyses the orders for a given date.

          Attributes:
              date (datetime): input date for the requested report
              total_items (int): total items sold for the input date
              total_discount (float): total discount given for the input date
              avg_discount_rate (float): average discount rate given for the input date(0<= avg_discount_rate < 1)
              avg_order_total: average order total for the input date
              total_commissions: total commissions for the input date
              avg_commissions_per_order: average commissions per order for the input date
        """

    def __init__(self, date: datetime):
        self.date = date

        self.total_items = self.get_total_items(self.date)
        self.total_customers = self.get_total_customers(self.date)
        self.total_discount = self.get_total_discount(self.date)
        self.avg_discount_rate = self.get_avg_discount_rate(self.date)
        self.avg_order_total = self.get_avg_order_total(self.date)
        self.total_commissions = self.get_total_commissions(self.date)
        self.avg_commissions_per_order = self.get_avg_commissions_per_order(self.date)

    def __str__(self):
        return f'eShop Report for {self.date}\n' \
               f'Total Number of Items Sold: {self.total_items:,}\n' \
               f'Total Number of Customers: {self.total_customers}\n' \
               f'Total Discount Given: £{round(self.total_discount, 2):,}\n' \
               f'Average Discount Rate: {round(self.avg_discount_rate * 100, 2)}%\n' \
               f'Average Order Total: £{round(self.avg_order_total, 2):,}\n' \
               f'Total Commissions: £{round(self.total_commissions, 2):,}\n' \
               f'Average Commissions per Order: £{round(self.avg_commissions_per_order, 2):,}'

    def get_all_results(self):
        "dict: returns a dictionary containing all report statistics."
        results_dict = {"date": self.date,
                        "total_items": self.total_items,
                        "total_customers": self.total_customers,
                        "total_discount": self.total_discount,
                        "avg_discount_rate": self.avg_discount_rate,
                        "avg_order_total": self.avg_order_total,
                        "total_commissions": self.total_commissions,
                        "avg_commissions_per_order": self.avg_commissions_per_order
                        }
        return results_dict

    @staticmethod
    def get_total_items(date):
        result = db.session.query(
            Order.created_at,
            func.sum(OrderLine.quantity).label('total')
            ).join(OrderLine
            ).filter(Order.created_at == date
            ).group_by(Order.created_at).all()[0][-1]
        return result

    @staticmethod
    def get_total_customers(date):
        result = db.session.query(Order.customer_id
                                ).filter(Order.created_at == date
                                ).distinct().all()
        return len(result)

    @staticmethod
    def get_total_discount(date):
        result = db.session.query(
            Order.created_at,
            func.sum(OrderLine.full_price_amount - OrderLine.discounted_amount).label('discount_total')
            ).join(OrderLine
            ).filter(Order.created_at == date
            ).group_by(Order.created_at).all()[0][-1]
        return result

    @staticmethod
    def get_avg_discount_rate(date):
        result = db.session.query(
            Order.created_at,
            func.avg(OrderLine.discount_rate).label('avg_discount_rate')
            ).join(OrderLine
            ).filter(Order.created_at == date
            ).group_by(Order.created_at
            ).all()[0][-1]
        return result

    @staticmethod
    def get_avg_order_total(date):
        result = db.session.query(
            Order.created_at,
            Order.id_,
            func.sum(OrderLine.total_amount).label('order_total'),
            ).join(OrderLine
            ).filter(Order.created_at == date
            ).group_by(Order.id_).all()

        order_avg = statistics.mean([element[2] for element in result])

        return order_avg

    @staticmethod
    def get_total_commissions(date):
        result = db.session.query(
                Order.id_,
                Order.created_at,
                VendorCommissions.vendor_id,
                func.sum(VendorCommissions.rate * OrderLine.total_amount)
            ).join(VendorCommissions
            ).join(OrderLine
            ).filter(Order.created_at == date
            ).filter(VendorCommissions.date == Order.created_at
            ).group_by(Order.id_
            ).all()

        com_tot = sum((element[-1] for element in result))

        return com_tot

    @staticmethod
    def get_avg_commissions_per_order(date):
        result = db.session.query(
                Order.id_,
                Order.created_at,
                VendorCommissions.vendor_id,
                func.sum(VendorCommissions.rate * OrderLine.total_amount)
            ).join(VendorCommissions
            ).join(OrderLine
            ).filter(Order.created_at == date
            ).filter(VendorCommissions.date == Order.created_at
            ).group_by(Order.id_).all()

        order_avg = statistics.mean([element[-1] for element in result])
        return order_avg