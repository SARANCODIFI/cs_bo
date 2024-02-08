# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def execute():
    # List of fields to hide
    fields_to_hide = ["default_price_list", "default_currency","default_bank_account","is_internal_customer",
                      "market_segment","industry","website","language","customer_details","tax_withholding_category",
                      "payment_terms","credit_limits","loyalty_program","sales_team","default_sales_partner","default_commission_rate",
                      "settings_tab","tax_tab","accounting_tab",]

    # Fetch and update each field from the Customer doctype
    for field in fields_to_hide:
        docfield = frappe.get_doc("DocField", {"parent": "Customer", "fieldname": field})
        if docfield:
            # Set the hidden property to 1 (true) to hide the field
            docfield.hidden = 1
            docfield.save()

    # Clear the cache to reflect the changes
    frappe.clear_cache(doctype="Customer")
