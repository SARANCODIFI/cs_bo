import frappe

@frappe.whitelist()
def get_oppor(mobile):
    try:
        oppr = frappe.get_last_doc("Opportunity",filters={"fsl_mobile_num":mobile})
        if oppr:
            # frappe.errprint("in")
            return oppr
    except:
        frappe.local.response["data"] = {
            "success_key": 0,
            "message":"Opportunity not Exists"      
        }
