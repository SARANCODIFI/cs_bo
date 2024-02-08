import frappe
from frappe.utils import now_datetime
current_datetime = now_datetime()

@frappe.whitelist(allow_guest=True)
def rm_refer(rm_id, mobile,emailid = None, name = None):
        try:
            # frappe.errprint("hiii")
            customer = frappe.db.exists("Customer", {"mobile_no": mobile})
            # frappe.errprint(customer)
            oppor_exists = frappe.db.exists("Opportunity", {"fsl_mobile_num": mobile})
            # frappe.errprint(oppor_exists)
            lead_exists = frappe.db.exists("Lead", {"mobile_no": mobile})
            # frappe.errprint(lead_exists)

            if customer:
                # frappe.errprint("hioiuhgbnii")
                # frappe.errprint("1")
                frappe.local.response["message"] = {
                "success_key": 1,
                "message":"Customer Already Exists"
                }

            elif oppor_exists:
                # frappe.errprint("11")
                frappe.local.response["message"] = {
                "success_key": 1,
                "message":"Opportunity Already Exists"
                }

            elif lead_exists:
                # frappe.errprint("111")
                frappe.local.response["message"] = {
                "success_key": 1,
                "message":"Lead Already Exists"
                }

            else :
                # frappe.errprint("11011")
                lead_doc = frappe.new_doc("Lead")
                if name:
                    lead_doc.lead_name = name
                    # frappe.errprint("nnamexx11011")
                lead_doc.status = "Lead"
                lead_doc.company_name  = mobile
                # frappe.errprint("nnxsdfghjkuytresdfgh11011")
                emp = frappe.db.exists("Employee",{"user_id" : rm_id})
                # frappe.errprint(emp)
                lead_doc.fsl_referral_rm = emp
                # frappe.errprint(lead_doc.fsl_referral_rm)
                lead_doc.mobile_no = mobile
                
                lead_doc.insert()
               
                frappe.db.commit()
                
                frappe.local.response["message"] = {
                     
                "success_key": 1,
                "message":"Lead Created",
                "data": 
                        {
                            "lead_id":lead_doc.name,
                            "referral_rm" : lead_doc.fsl_referral_rm
                        } 
                }
        
        except Exception as e:
            frappe.local.response["message"] = {
                "error": f"An error occurred: {str(e)}"
            }