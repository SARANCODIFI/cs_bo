from datetime import datetime

import frappe
from frappe.query_builder import Interval, Order
from frappe.query_builder.functions import Date, Sum, UnixTimestamp
from frappe.utils import getdate

@frappe.whitelist()
def get_trade_book_heatmap_data(ucc = None):
    if ucc != None:
        tradebook_data = frappe.get_all(
                "Tradebook",
                fields=["ucc", "trade_date", "COUNT(*) as tradebook_count"],
                filters={"ucc": ucc},
                group_by="ucc, trade_date",
                order_by="trade_date ASC",
            )
        return tradebook_data

