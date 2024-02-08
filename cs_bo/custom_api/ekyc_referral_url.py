import frappe

@frappe.whitelist()
def get_referral_url(phone_no):
    data = []
    
    try:     
        document= frappe.get_last_doc('Customer', filters={"mobile_no":phone_no}) #or frappe.get_last_doc('Employee', filters={"cell_number":phone_no})
        url = frappe.get_doc('EKYC Settings', 'ekyc')
        
        frappe.local.response["message"] = {
            "success_key": 1,
            "url": f"{url.referral_url}customer/{document.name}"
        }
        
    except :
        try:
            document = frappe.get_last_doc('Employee', filters={"cell_number":phone_no})
            url = frappe.get_doc('EKYC Settings', 'ekyc')
            
            frappe.local.response["message"] = {
            "success_key": 1,
            "url": f"{url.referral_url}employee/{document.name}"
        }
                   
        except Exception as e:
            frappe.local.response["message"] = {
                "error": "No User Found"
            }             