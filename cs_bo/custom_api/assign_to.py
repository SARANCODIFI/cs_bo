# import frappe
# from frappe.utils import now_datetime

# @frappe.whitelist(allow_guest=True)
# def assign_to(id,assign_to):
#     try:    
#         oppr=frappe.get_doc('Opportunity',id)
#         oppr.fsl_assign_to = assign_to
#         current_datetime = now_datetime()              
#         oppr.custom_assign_time = current_datetime.strftime('%H:%M:%S')
        
#         oppr.save()
        
#         frappe.local.response["message"] = {
#         "success_key": "01",
#         "message":oppr
#         }
        
        
#     except Exception as e:
#         frappe.local.response["message"] = {
#             "error": f"An error occurred: {str(e)}"
        # }

import frappe
from frappe.utils import now_datetime

@frappe.whitelist(allow_guest=True)
def assign_to(id, assign_to):
    try:
        oppr = frappe.get_doc('Opportunity', id)
        oppr.fsl_assign_to = assign_to
        current_datetime = now_datetime()
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')  # Use uppercase Y for 4-digit year

        oppr.fsl_custom_assign_time = formatted_datetime

        oppr.save()

        frappe.local.response["message"] = {
            "success_key": 1,
            # "message": oppr,
            "message": {
                "fsl_assign_to": oppr.fsl_assign_to,
                "custom_assign_time": oppr.fsl_custom_assign_time
            }
        }
    except Exception as e:
        frappe.local.response["message"] = {
            "success_key": 0,
            "message": f"Error: {str(e)}"
        }
