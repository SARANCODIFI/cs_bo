import frappe

@frappe.whitelist()
def get_rm_details(mobile):
    try:
        lead = frappe.db.exists("Lead", {"mobile_no":mobile})
        
        if lead:
           
            oppr = frappe.db.exists("Opportunity",{"fsl_mobile_num":mobile})
            
            if oppr: 
                oppor = frappe.get_last_doc("Opportunity",filters = {"fsl_mobile_num":mobile})

                o_employee = frappe.db.exists("Employee",oppor.fsl_referral_by)
                

                if o_employee:
                    employee = frappe.get_doc("Employee",oppor.fsl_referral_by)
                    branch = frappe.get_doc("Branch",employee.branch)

                    frappe.local.response["message"] = {
                    "success_key": 1,
                    "message":"Employee Exists",
                    "data":
                    {
                        "referral_id" : employee.name,
                        "branch" : employee.branch,
                        "branch_name" : branch.branch,
                        "name" : employee.first_name
                    }
                    }
                else :
                    frappe.local.response["message"] = {
                    "success_key": 1,
                    "message":"Employee Is Not Found For This Customer"
                    }

            else :
                
                frappe.local.response["message"] = {
                "success_key": 0,
                "message":"Lead Exists But Opportunity Not Created"
                }
        else :
            frappe.local.response["message"] = {
                "success_key": 0,
                "message":"Lead Not Exists"
                }

    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }