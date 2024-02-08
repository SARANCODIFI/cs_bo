import frappe

@frappe.whitelist()
def put_user_details(pan,id,firstname,middlename,lastname,username,aadharpanlink,stage,status,fsl_pan_confirm):
        try:
            oppor1 = frappe.get_doc("Opportunity",id)
            if oppor1.fsl_sms_verified == 1:
                if oppor1.fsl_email_verified == 1:
                    if fsl_pan_confirm == "1":
                        if firstname:
                            oppor1.fsl_first_name = firstname
                        if pan:
                            oppor1.fsl_pan_no = pan
                        if middlename:
                            oppor1.fsl_middle_name = middlename
                        if lastname:
                            oppor1.fsl_last_name = lastname
                        if username:
                            oppor1.fsl_user_name = username
                        if aadharpanlink:
                            oppor1.fsl_aadharpan_link = aadharpanlink
                        if stage:
                            oppor1.fsl_stage = stage
                        if status:
                            oppor1.status = status
                        oppor1.fsl_pan_confirm = fsl_pan_confirm

                        oppor1.save()
                        # success = 1

                        frappe.local.response["message"] = {
                            "success_key": 1,
                            "message":"Opportunity Updated",
                            "First Name" : oppor1.fsl_first_name,
                            "Middle Name" : oppor1.fsl_middle_name,
                            "Last Name" : oppor1.fsl_last_name,
                            "User Name" :  oppor1.fsl_user_name,
                            "Pan No" : oppor1.fsl_pan_no,
                            "aadharpanlink" : oppor1.fsl_aadharpan_link,
                            "status" : oppor1.status,
                            "stage" : oppor1.fsl_stage
                            } 
                    if fsl_pan_confirm == "0":
                        oppor = frappe.db.exists("Opportunity",{'fsl_pan_no':pan})
                        if oppor:
                            frappe.local.response["message"] = {
                                "success_key": 0,
                                "message":"This Pan Is Already Exists"
                            } 
                        else :
                            if firstname:
                                oppor1.fsl_first_name = firstname
                            if pan:
                                oppor1.fsl_pan_no = pan
                            if middlename:
                                oppor1.fsl_middle_name = middlename
                            if lastname:
                                oppor1.fsl_last_name = lastname
                            if username:
                                oppor1.fsl_user_name = username
                            if aadharpanlink:
                                oppor1.fsl_aadharpan_link = aadharpanlink
                            if stage:
                                oppor1.fsl_stage = stage
                            if status:
                                oppor1.status = status
                            oppor1.save()
                            # success = 1

                            frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"Opportunity Updated",
                                "First Name" : oppor1.fsl_first_name,
                                "Middle Name" : oppor1.fsl_middle_name,
                                "Last Name" : oppor1.fsl_last_name,
                                "User Name" :  oppor1.fsl_user_name,
                                "Pan No" : oppor1.fsl_pan_no,
                                "aadharpanlink" : oppor1.fsl_aadharpan_link,
                                "status" : oppor1.status,
                                "stage" : oppor1.fsl_stage
                                } 

                else :
                    frappe.local.response["message"] = {
                        "success_key": 0,
                        "message":"Email is not Verified"
                        } 

            else :
                frappe.local.response["message"] = {
                    "success_key": 0,
                    "message":"SMS is not Verified"
                    } 

        except :
            frappe.local.response["message"] = {
            "success_key": 0,
            "message":"This Opportunity Not Exists"
            }