from frappe import _

import frappe

@frappe.whitelist(allow_guest=True)

def get_withdraw(ucc):
    try:
        withdraw = frappe.get_all("withdraw",
            filters={'ucc': ucc},
            fields=["date", "time", "bank_account", "ucc", "withdraw_amount"])

        tot_data = withdraw  # Use the fetched data directly

        frappe.response["message"] = {
            "Success_key" : "1",
            "data": tot_data
        }
    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }


@frappe.whitelist(allow_guest=True)
def post_withdarw(data):
    # tot_data = []
    # table = data.get("deposit")
    
    # tradebook_data = data.get("data", {}).get("tradebook")
    # if tradebook_data:

    #  for i in table:   
    try:
            withdarw = frappe.new_doc("withdraw")
            withdarw.ucc = data["ucc"]
            withdarw.time = data["time"]
            withdarw.bank_account = data["bank_account"]
            withdarw.date = data["date"]
            withdarw.withdraw_amount = data["withdraw_amount"]
            withdarw.save()

            data1 = {
                "ucc" : withdarw.ucc,
                "time" : withdarw.time,
                "bank_account" : withdarw.bank_account,
                "date" : withdarw.date,
                "withdraw_amount" : withdarw.withdraw_amount,
            }
            # tot_data.append(data)
            
            frappe.response["message"] = {
                "success_key": 1,
                "data":data1
            }

    except Exception as e:
            frappe.local.response["message"] = {
                "error": f"An error occurred: {str(e)}"
            }
    