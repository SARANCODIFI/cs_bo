import frappe
import json

@frappe.whitelist()
def get_positions(ucc_code):
    positions = frappe.get_all("positions",filters= {"ucc":ucc_code},fields=["ucc","symbol","type","date","qty","avg_price","pdc","pnl","pnl_change"]) if frappe.db.exists("positions",{"ucc":ucc_code}) else "Positions Not Exists"
    frappe.response["message"] = {
        "data": {
            "positions": positions
        }
    }

@frappe.whitelist(allow_guest=True)
def create_positions(data):
    positions =  frappe.new_doc("positions") if not frappe.db.exists("positions",{"ucc":data["ucc"]}) else "Position Already Exists"
    if positions != "Position Already Exists":
        positions.update({
            "ucc": data["ucc"],
            "symbol": data["symbol"],
            "type": data["type"],
            "date": data["date"],
            "qty": data["qty"],
            "avg_price": data["avg_price"],
            "pdc": data["pdc"],
            "pnl": data["pnl"],
            "pnl_change": data["pnl_change"]
        }) 
        positions.save()
    frappe.response["message"] = {
        "data": {
            positions
        }
    }

@frappe.whitelist(allow_guest=True)
def update_positions(data):
    positions = frappe.get_last_doc("positions",filters={"ucc":data["ucc"]}) if frappe.db.exists("positions",{"ucc":data["ucc"]}) else "Position Not Exists"
    if positions != "Position Not Exists":
        for datas in data:
            positions.update({
                datas : data[datas]
            })
        positions.save()
        positions = "Positions Updated Successfully"
    
    frappe.response["message"] = {
        "data": {
            positions
        }
    }

@frappe.whitelist(allow_guest=True)
def delete_positions(ucc_code):
    positions = frappe.db.delete("positions",{"ucc":ucc_code}) if frappe.db.exists("positions",{"ucc":ucc_code}) else "Position Not Exists"
    positions = "Position Deleted Successfully" if positions != "Position Not Exists" else "Position Not Exists"
    frappe.response["message"] = {
        "data": {
            positions
        }
    }
        
    