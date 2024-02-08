import frappe
from frappe.utils import now_datetime

@frappe.whitelist()
def post_email(id,email,otp):
    # if email_verified:
    oppor1 = frappe.get_doc("Opportunity",id)
    if oppor1.fsl_sms_verified == 1:
        # try:
        # if email_verified == "0":
        #     oppor = frappe.db.exists("Customer",{'email_id':email})
        #     if oppor:
        #         frappe.local.response["error"] = {
        #             "success_key": 0,
        #             "message":"This Email id Already Exists"
        #         } 
        #     else:
        #         oppor1.fsl_email_verified = 1
        #         oppor1.fsl_email_id = email
        #         oppor1.fsl_email_verified = 1
        #         oppor1.fsl_stage = 0.5
        #         oppor1.save()
        #         frappe.local.response["message"] = {
        #         "success_key": 1,
        #         "message":"Email not verified , opportunity is updated",
        #         "id":oppor1.name,
        #         "stage":oppor1.fsl_stage 
        #         }

        
        oppor = frappe.db.exists("Customer",{'email_id':email})
        if oppor:
            frappe.local.response["error"] = {
                "success_key": 0,
                "message":"This Email id Already Exists"
            }
        else: 
            if otp:
                oppor1.fsl_email_verified = 1
                oppor1.fsl_email_id = email
                oppor1.fsl_email_otp=otp
                oppor1.fsl_email_verified = 1
                oppor1.fsl_stage = 1
                current_datetime = now_datetime()
                oppor1.append("fsl_stage_table", {
                    "stages": 1,
                    "timing": current_datetime.strftime('%Y-%m-%d %H:%M:%S')
                })
                oppor1.save()
                frappe.local.response["message"] = {
                "success_key": 1,
                "message":"Email Verified and opportunity is updated",
                "data":{
                    "opportunity_id":oppor1.name,
                    "stage":oppor1.fsl_stage
                }
                }
            else: 
                frappe.local.response["error"] = {
                "success_key": 0,
                "message":"otp is Mandatory",
                        
            }
        

            
            
        # except:
        #     frappe.local.response["message"] = {
        #         "success_key": 0,
        #         "message":"This Opportunity is Not Exists "
        #         } 

    else:
            frappe.local.response["error"] = {
            "success_key": 0,
            "message":"SMS Not Verified for this Mobile Number"
            }

    # else:

        # frappe.local.response["message"] = {
        #     "success_key": 0,
        #     "message":"otp is Mandatory",
                    
        # } 
