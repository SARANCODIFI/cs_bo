
import frappe
import json

@frappe.whitelist(allow_guest=True)
def get_withdrawal_req(ucc_code):
    withdraw_req = frappe.get_all("withdrawal_request",filters= {"ucc":ucc_code},fields=["ucc","bank_account","time","date","amount","reference_number","withdrawal_status_code"]) if frappe.db.exists("withdrawal_request",{"ucc":ucc_code}) else "Withdrawel Requests Not Exists"
    frappe.response["message"] = {
        "data": {
            "withdrawel_requests": withdraw_req
        }
    }

@frappe.whitelist(allow_guest=True)
def create_withdrawal_req(data):
    withdrawel_req =  frappe.new_doc("withdrawal_request")if not frappe.db.exists("Withdrawel Request",{"date":data["date"],"bank_account":data["bank_account"],"ucc":data["ucc"],"amount":data["amount"],"time":data["time"]}) else "withdrawal_request Already Exists"
    withdrawel_req.update({
        "date": data["date"],
        "bank_account": data["bank_account"],
        "ucc": data["ucc"],
        "amount": data["amount"],
        "time": data["time"],
        "reference_number":data["reference_number"],
        "withdrawal_status_code":data["withdrawal_status_code"]
    })
    withdrawel_req.save()
    frappe.response["message"] = {
        "data": {
            withdrawel_req
        }
    }