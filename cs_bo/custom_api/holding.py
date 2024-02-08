from frappe import _

import frappe

@frappe.whitelist(allow_guest=True)

def get_holdings(ucc):
    try:
        holding = frappe.get_all("holdings",
            filters={'ucc': ucc},
            fields=["ucc", "qty", "buy_avg", "buy_value", "present_value","pnl","pnl_change"])

        tot_data = holding  # Use the fetched data directly

        frappe.response["message"] = {
            "Success_key" : "new code",
            "data": tot_data
        }
    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }

@frappe.whitelist(allow_guest=True)
def update_holdings(data):
    holdings = frappe.get_last_doc("holdings",filters={"ucc":data["ucc"]}) if frappe.db.exists("holdings",{"ucc":data["ucc"]}) else "holding Not Exists"
    if holdings != "holding Not Exists":
        for datas in data:
            holdings.update({
                datas : data[datas]
            })
    holdings.save()
    frappe.response["message"] = {
        "data": {
            holdings
        }
    }


@frappe.whitelist(allow_guest=True)
def post_holdings(data):  
    try:
            holdings = frappe.new_doc("holdings")
            holdings.ucc = data["ucc"]
            holdings.qty = data["qty"]
            holdings.buy_avg = data["buy_avg"]  
            holdings.present_value = data["present_value"]
            holdings.pnl = data["pnl"]
            holdings.pnl_change = data["pnl_change"]
            holdings.save()

            data1 = {
                "ucc" : holdings.ucc,
                "qty" : holdings.qty,
                "buy_avg" : holdings.buy_avg,
                "date" : holdings.date,
                "pnl" : holdings.pnl,
                "pnl_change" :holdings.pnl_change
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


@frappe.whitelist(allow_guest=True)
def delete_holdings(ucc_code):
    holding= frappe.db.delete("holdings",{"ucc":ucc_code})
    if frappe.db.exists("holdings", {"ucc": ucc_code}):
        frappe.db.delete("holdings", {"ucc": ucc_code})
        message = "Holding Deleted Successfully"
    else:
        message = "Holding Not Exists"
    holding = "holding Deleted Successfully" if holding != "holding Not Exists" else "holding Not Exists"
    frappe.response["message"] = {
        "data": {
            holding
        }
    }
        