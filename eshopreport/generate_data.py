"""
generate_date.py: Module to generate the data for the Flask sqlite database (eshopreport/eshop.db) by importing data
from each csv file in eshopreport/data.
"""

from datetime import datetime
from eshopreport.models import Order, OrderLine, Promotion, ProductPromotion, Product, VendorCommissions
from eshopreport import db
import pandas as pd


def main():
    reset_database()

    import_orders()
    import_order_lines()
    import_products()
    import_promotions()
    import_product_promotions()
    import_commissions()


def import_products():
    """None: Imports all items from data/products.csv to database"""
    products = []
    df = pd.read_csv('eshopreport/data/products.csv')

    for index, row in df.iterrows():
        product_i = Product(row['id'], row['description'])
        products.append(product_i)
    db.session.add_all(products)
    db.session.commit()


def import_promotions():
    """None: Imports all items from data/promotions.csv to database"""
    promotions = []
    df = pd.read_csv('eshopreport/data/promotions.csv')

    for index, row in df.iterrows():
        promotion_i = Promotion(row['id'], row['description'])
        promotions.append(promotion_i)

    db.session.add_all(promotions)
    db.session.commit()


def import_product_promotions():
    """None: Imports all items from data/product_promotions.csv to database"""
    product_promotions = []
    df = pd.read_csv('eshopreport/data/product_promotions.csv')

    for index, row in df.iterrows():
        date = datetime.strptime(row['date'], '%Y-%m-%d').date()
        product_promotion_i = ProductPromotion(row['product_id'], date, row['promotion_id'])
        product_promotions.append(product_promotion_i)

    db.session.add_all(product_promotions)
    db.session.commit()


def import_commissions():
    """None: Imports all items from data/commissions.csv to database"""
    commissions = []
    df = pd.read_csv('eshopreport/data/commissions.csv')

    for index, row in df.iterrows():
        date = datetime.strptime(row['date'], '%Y-%m-%d').date()
        commission_i = VendorCommissions(row['vendor_id'], date, row['rate'])
        commissions.append(commission_i)

    db.session.add_all(commissions)
    db.session.commit()


def import_orders():
    """None: Imports all items from data/orders.csv to database"""
    orders = []
    df = pd.read_csv('eshopreport/data/orders.csv')

    for index, row in df.iterrows():
        date = datetime.strptime(row['created_at'], '%Y-%m-%d %H:%M:%S.%f').date()
        order_i = Order(row['id'], date, row['vendor_id'], row['customer_id'])
        orders.append(order_i)

    db.session.add_all(orders)
    db.session.commit()


def import_order_lines():
    """None: Imports all items from data/order_lines.csv to database"""
    order_lines = []
    df = pd.read_csv('eshopreport/data/order_lines.csv')

    for index, row in df.iterrows():
        order_line_i = OrderLine(row['order_id'],
                                 row['product_id'],
                                 row['product_description'],
                                 row['product_price'],
                                 row['product_vat_rate'],
                                 row['discount_rate'],
                                 row['quantity'],
                                 row['full_price_amount'],
                                 row['discounted_amount'],
                                 row['vat_amount'],
                                 row['total_amount'])
        order_lines.append(order_line_i)

    db.session.add_all(order_lines)
    db.session.commit()


def reset_database():
    """None: Empties and removes each table in the database, then recreates each table. This is used in testing to
    quickly reset the database if required."""
    db.create_all()
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())
    db.session.commit()

    db.create_all()


if __name__ == "__main__":
    main()