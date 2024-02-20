import frappe
from frappe.utils import getdate

@frappe.whitelist()
def get_customer_ledger_records(ucc=None, from_date=None, to_date=None):
    if ucc is None:
        frappe.response["success"] = 0  
        frappe.response["message"] = "UCC is required."
        return


    if not from_date:
        from_date = frappe.utils.data.get_first_day(getdate().replace(day=1))
    if not to_date:
        to_date = frappe.utils.data.get_last_day(getdate())

    filters = {
        "dtoftran": ["between", [from_date, to_date]],
        "tradingcode": ucc
    }
    fields = ["tradingcode", "dtoftran", "voucher", "drcr", "damount", "camount", "entrycode", "branchcode"]

    customer_ledger = frappe.get_list("customer_ledger", filters=filters, fields=fields)

    response = {
        "success": 1,
        "customer_ledger": customer_ledger
    }
    return response

