from frappe import _

import frappe

@frappe.whitelist(allow_guest=True)
def get_trade_log(ucc):
    try:
        tradelog = frappe.get_all("tradelog",
            filters={'ucc': ucc},
            fields=["ucc","segment","trade_date","qty","trade_segment"])

        tot_data = tradelog  # Use the fetched data directly

        frappe.response["message"] = {
            "Success_key" : "1",
            "data": tot_data
        }
    except Exception as e:
        frappe.local.response["message"] = {
            "error": "No trade log found"
        }

