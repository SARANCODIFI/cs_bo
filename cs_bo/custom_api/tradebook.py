from frappe import _

import frappe

@frappe.whitelist(allow_guest=True)
def trade_book(ucc,from_date = None, to_date = None):
    try:
        sql_query = """
            SELECT ucc, trade_time, branch, order_id, symbol, trade_id, segment, qty, exchange, price,
            trade_date, expiry_date, tags, type, value
            FROM `tabTradebook`
            WHERE trade_date BETWEEN %s AND %s
            AND ucc = %s
        """
        tradebooks = frappe.db.sql(sql_query, (from_date, to_date, ucc), as_dict=True)

        # tradebooks = frappe.db.get_all("Tradebook",
        #     filters={"trade_date": ["between", [from_date, to_date]],"ucc" :ucc},
        #     fields=["ucc", "trade_time", "branch", "order_id", "symbol", "trade_id", "segment", "qty", "exchange", "price", "trade_date", "expiry_date", "tags", "type", "value"])

        tot_data = tradebooks
        
        frappe.response["message"] = {
            "Success_key": 1,
            "data": tot_data
        }
    except Exception as e:
        frappe.local.response["message"] = {
            "error": "Trade book data not found"
        }