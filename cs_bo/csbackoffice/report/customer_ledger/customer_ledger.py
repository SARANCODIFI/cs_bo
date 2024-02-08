# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data

def execute(filters=None):
    # frappe.throw(filters)
    columns = get_columns(filters)
    data = get_data(filters)
    return columns, data

def get_columns(filters=None):
    columns = [
        {"fieldname": "tradingcode","fieldtype": "Link","label": "UCC","options": "Customer"},
        {"fieldname": "dtoftran","fieldtype": "Date","in_filter": 1,"label": "Dtoftran"},
        {"fieldname": "voucher","fieldtype": "Data","label": "Voucher"}, 
        {"fieldname": "drcr","fieldtype": "Data","label": "DrCr"},
        {"fieldname": "damount","fieldtype": "Float","label": "damount"},
        {"fieldname": "camount","fieldtype": "Float","label": "camount"},
        {"fieldname": "entrycode","fieldtype": "Data","label": "entrycode"},
        {"fieldname": "branchcode","fieldtype": "Data","label": "branchcode"},
        {"fieldname": "exchange","fieldtype": "Data","label": "exchange"},
        {"fieldname": "booktype","fieldtype": "Data","label": "booktype"},
        {"fieldname": "vallan","fieldtype": "Data","label": "vallan"},
        {"fieldname": "bankreco","fieldtype": "Data","label": "bankreco"},
        {"fieldname": "cheque","fieldtype": "Data","label": "cheque"},
        {"fieldname": "nproductcode","fieldtype": "Data","label": "nproductcode"},
        {"fieldname": "descript","fieldtype": "Data","label": "DESCRIPT"},
        {"fieldname": "created_on","fieldtype": "Date","label": "created_on"},
    ]
    return columns
    

def get_data(filters=None):
    conditions = {}
    if filters.get("ucc"):
        conditions["tradingcode"]= filters.ucc
    if filters.from_date and filters.to_date:
        conditions["dtoftran"] = ["between", [filters.from_date, filters.to_date]]
    data = frappe.get_all(
        "Customer Ledger",
        fields=["tradingcode", "dtoftran", "voucher", "drcr", "damount", "camount","entrycode","branchcode","exchange","booktype","vallan",
                "bankreco","cheque","nproductcode","descript","created_on"],
                filters = conditions,order_by="name"
        # filters={"tradingcode":filters.get("ucc")},
        # order_by="Dtoftran"
		
    )

    return  data

