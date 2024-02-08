from frappe import _

import frappe

@frappe.whitelist(allow_guest=True)

def get_deposit(customer):
    try:
        deposits = frappe.get_all("deposit",
            filters={'ucc': customer},
            fields=["date", "time", "bank_account", "customer", "deposit_amount"])

        tot_data = deposits  # Use the fetched data directly

        frappe.response["message"] = {
            "Success_key" : "1",
            "data": tot_data
        }
    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }


@frappe.whitelist(allow_guest=True)
def post_deposit(data):
    # tot_data = []
    # table = data.get("deposit")
    
    # tradebook_data = data.get("data", {}).get("tradebook")
    # if tradebook_data:

    #  for i in table:   
    try:
            deposit = frappe.new_doc("deposit")
            deposit.customer = data["customer"]
            deposit.time = data["time"]
            deposit.bank_account = data["bank_account"]
            deposit.date = data["date"]
            deposit.deposit_amount = data["deposit_amount"]
            deposit.save()

            data1 = {
                "customer" : deposit.customer,
                "time" : deposit.time,
                "bank_account" : deposit.bank_account,
                "date" : deposit.date,
                "deposit_amount" : deposit.deposit_amount,
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
    