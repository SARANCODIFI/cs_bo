import frappe


@frappe.whitelist()
def get_pan_status(pan,id):
    
    data = []
    try:
        cus = frappe.db.exists("Customer",{'fsl_pan_card':pan})
        
        if cus:
            
            frappe.local.response["message"] = {
                "success_key": 1,
                "pan_status": "This Pan Already Exists in Customer"
                }
        else:
            
            if frappe.db.exists("Opportunity",{'fsl_pan_no':pan}):
                
                opportunity = frappe.get_last_doc("Opportunity",filters={'fsl_pan_no':pan})
                
                if id == opportunity.name:
                    
                
                    frappe.local.response["message"] = {
                    "success_key": 1,
                    "pan_status": "This Pan Already Exists For this ID"
                    }
                else:
                    frappe.local.response["message"] = {
                    "success_key": 0,
                    "pan_status": "Pan Already Exists For Another ID"
                    }
                
            else :
                
                frappe.local.response["message"] = {
                "success_key": 1,
                "pan_status": "Pan Not Exists"
            }
        
    except:
        frappe.local.response["message"] = {
        "success_key": 1,
        "pan_status": "Pan Not Exists"
    }