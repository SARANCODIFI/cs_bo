
import frappe

@frappe.whitelist(allow_guest=True)
def get_pnl_log(ucc_code):
    pnl_logs = frappe.get_all("PnL Log",filters= {"ucc":ucc_code},fields=["ucc","exchange","segment","date","qty","pnl"]) if frappe.db.exists("PnL Log",{"ucc":ucc_code}) else "Pnl Logs Not Exists"
        
    frappe.response["message"] = {
        "data": {
            "pnl_logs":pnl_logs
        }
    }



@frappe.whitelist(allow_guest=True)
def get_opp(opp_name):
    oppr = frappe.get_doc("Opportunity",name=opp_name)
    frappe.response["message"] = {
        "data": {
            "pnl_logs":oppr.opportunity_from
        }
    }