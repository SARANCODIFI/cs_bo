import frappe
from frappe.utils import now_datetime
current_datetime = now_datetime()

@frappe.whitelist()
def post_opportunity1(mobile,smsverified,referral_by,otp,fsl_mode_of_application):
        
        frappe.errprint("referral_by000")
        frappe.errprint(referral_by)
     
    
        if smsverified == "1":
            # frappe.errprint("1")
            if otp:
                # frappe.errprint("2")
                try:
                    # frappe.errprint("3")
                    try:
                        customer = frappe.get_last_doc("Customer",filters = {"mobile_no":mobile})
                        if customer:
                            # frappe.errprint("Customer Already Exists")
                            frappe.errprint("Customer Already Exists")
                            frappe.local.response["message"] = {
                            "success_key": 1,
                            "message":"Customer Already Exists",
                            "data": 
                            {
                                # "opportunity_id":oppor_exists.name
                                "stage": customer.fsl_activation_status
                            } 
                            }
                    except: 
                        oppor_exists = frappe.get_last_doc("Opportunity",filters = {"fsl_mobile_num":mobile})
                       
                        if oppor_exists:
                            frappe.errprint("12345")
                            # frappe.errprint("4")
                            oppor_exists.fsl_referral_by = referral_by
                            oppor_exists.save()
                            # frappe.errprint("Opportunity Already Exists and Referral ID is Updated")
                            frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"Opportunity Already Exists and Referral ID is Updated",
                                "data": 
                                {
                                    "opportunity_id":oppor_exists.name,
                                    "stage":oppor_exists.fsl_stage,
                                    "Referral Id" : oppor_exists.fsl_referral_by
                                } 
                            } 
                    # else:

                    
                except:
                    # frappe.errprint("80")   
                    try :
                        lead_doc = frappe.get_last_doc("Lead",filters={"mobile_no":mobile})
                        # frappe.errprint(lead_doc)
                        # if lead_doc:
                        # frappe.errprint("8011") 
                        lead = lead_doc.name
                        if lead_doc:
                        ###############oppor
                            try:
                        
                                oppor_exists = frappe.get_last_doc("Opportunity",filters = {"fsl_mobile_num":mobile})
                                # frappe.errprint("12345")
                                # frappe.errprint("4")
                                oppor_exists.fsl_referral_by = referral_by
                                oppor_exists.save()
                                # frappe.errprint("Opportunity Already Exists and Referral ID is Updated")
                                frappe.local.response["message"] = {
                                    "success_key": 1,
                                    "message":"Opportunity Already Exists and Referral ID is Updated",
                                    "data": 
                                    {
                                        "opportunity_id":oppor_exists.name,
                                        "stage":oppor_exists.fsl_stage,
                                        "Referral Id" : oppor_exists.fsl_referral_by
                                    } 
                                } 
                            except:
                            
                                # frappe.errprint("22")
                                oppor = create_opportunity(mobile,referral_by,otp,lead,fsl_mode_of_application)
                                frappe.errprint("Lead Exists and Opportunity Created")
                                frappe.local.response["message"] = {
                                    "success_key": 1,
                                    "message":"Lead Exists and Opportunity Created",
                                    "data": 
                                    {
                                        "opportunity": oppor.name,
                                        "stage":oppor.fsl_stage,
                                        "fsl_mode_of_application": oppor.fsl_mode_of_application
                                        
                                    } 
                                } 
                            
                        # frappe.errprint("33")
                    except:
                        # frappe.errprint("10")
                        lead_doc = frappe.new_doc("Lead")
                        lead_doc.first_name = mobile
                        lead_doc.status = "Lead"
                        lead_doc.company_name  = mobile
                        lead_doc.mobile_no = mobile
                        lead_doc.insert()
                        try:
                            oppor_exists = frappe.get_last_doc("Opportunity",filters = {"fsl_mobile_num":mobile})
                           
                                
                            # frappe.errprint("4")
                            oppor_exists.fsl_referral_by = referral_by
                            oppor_exists.save()
                            # frappe.errprint("Opportunity Already Exists and Referral ID is Updated")
                            frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"Opportunity Already Exists and Referral ID is Updated",
                                "data": 
                                {
                                    "opportunity_id":oppor_exists.name,
                                    "stage":oppor_exists.fsl_stage,
                                    "Referral Id" : oppor_exists.fsl_referral_by
                                } 
                            } 
                        
                        except : 
                            # frappe.errprint("101")          
                            oppor = frappe.new_doc("Opportunity")
                            # oppor.fsl_active_status = 1
                            oppor.opportunity_from = "Lead"
                            oppor.party_name = lead_doc.name
                            oppor.fsl_stage = 0.5
                            oppor.fsl_user_name = mobile
                            oppor.fsl_mobile_num = mobile
                            oppor.status = "In-Progress"
                            oppor.fsl_mode_of_application = fsl_mode_of_application
                            oppor.fsl_sms_verified = 1
                            oppor.fsl_sms_otp = otp
                            oppor.append("fsl_stage_table", {
                                "stages": "0.5",
                                "timing": current_datetime.strftime('%Y-%m-%d %H:%M:%S')
                            })
                            oppor.insert()
                            frappe.errprint("Lead and Opportunity Created")
                            frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"Lead and Opportunity Created",
                                "data": 
                                {
                                    "opportunity": oppor.name,
                                    "stage":oppor.fsl_stage,
                                    "fsl_mode_of_application" : oppor.fsl_mode_of_application
                                } 
                            } 
                        
            else:
                frappe.local.response["message"] = {
                    "success_key": 0,
                    "message":"otp is Mandatory",
                            
                        } 

@frappe.whitelist()
def create_opportunity(mobile,referral_by,otp,lead,fsl_mode_of_application): 
    oppor = frappe.new_doc("Opportunity")
    oppor.opportunity_from = "Lead"
    oppor.party_name = lead
    oppor.fsl_active_status = 1
    oppor.fsl_stage = "0.5"
    oppor.fsl_user_name = mobile
    oppor.fsl_mobile_num = mobile
    oppor.fsl_referral_by = referral_by
    # frappe.errprint("referral_by")
    # frappe.errprint(referral_by)
    oppor.fsl_mode_of_application = fsl_mode_of_application
    oppor.fsl_sms_verified = 1
    oppor.status = "In-Progress"
    oppor.fsl_sms_otp = otp
    oppor.append("fsl_stage_table", {
                    "stages": "0.5",
                    "timing": current_datetime.strftime('%Y-%m-%d %H:%M:%S')
                })
    

    oppor.insert()
    oppor.db.commit()
    # frappe.errprint("oppor.fsl_referral_by")
    # frappe.errprint(oppor.fsl_referral_by)

    return oppor

# if smsverified == "0":
        #     try:
        #         try:
        #             # frappe.errprint("try1111")
        #             opportunity = frappe.get_last_doc("Opportunity",filters={'fsl_mobile_num':mobile})

        #             frappe.local.response["message"] = {
        #                     "success_key": 1,
        #                     "message":"Opportunity Already Exists",
        #                     "data":{
        #                         "opportunity_id":opportunity.name,
        #                         "stage":opportunity.fsl_stage
        #                     }
        #                 } 
        #         except:
        #             lead_doc = frappe.get_last_doc("Lead",filters={"mobile_no":mobile})
        #             if lead_doc:
        #             # oppor = create_opportunity(mobile)
        #                 frappe.local.response["message"] = {
        #                     "success_key": 1,
        #                     "message":"Lead Exists",
        #                     # "data":{
        #                     #     "lead":lead_doc.name
        #                     # }
        #                 }
        #     except:
        #         lead_doc = frappe.new_doc("Lead")
        #         lead_doc.first_name = mobile
        #         lead_doc.status = "Lead"
        #         lead_doc.company_name  = mobile
        #         lead_doc.mobile_no = mobile
        #         lead_doc.insert()
        #         frappe.local.response["message"] = {
        #             "success_key": 1,
        #             "message":"Lead Created Successfully",
        #             # "data":{
        #             #     "name":lead_doc.name
        #             # }
        #         }
    


@frappe.whitelist()
def post_opportunity(mobile,smsverified,referral_by,otp,fsl_mode_of_application):
    if smsverified == "0":
        try:
            
            customer = frappe.get_last_doc("Customer",filters = {"mobile_no":mobile})
            if customer:
                # frappe.errprint("Customer Already Exists")
                # frappe.errprint("Customer Already Exists")
                frappe.local.response["message"] = {
                "success_key": 1,
                "message":"Customer Already Exists",
                "data": 
                {
                    # "opportunity_id":oppor_exists.name
                    "stage": customer.fsl_activation_status
                } 
                }
        except:
            try:
                lead_doc = frappe.get_last_doc("Lead",filters={"mobile_no":mobile})
                if lead_doc:
                    frappe.local.response["message"] = {
                    "success_key": 1,
                    "message":"Lead Already Exists",
                    }

            except:    
                lead_doc = frappe.new_doc("Lead")
                lead_doc.first_name = mobile
                lead_doc.status = "Lead"
                lead_doc.company_name  = mobile
                lead_doc.mobile_no = mobile
                lead_doc.insert()
                frappe.local.response["message"] = {
                    "success_key": 1,
                    "message":"Lead Created Successfully",
                    
                }
        


        
    if smsverified == "1":
        # frappe.errprint("1")
        if otp:
            # frappe.errprint("2")
            try:
                # frappe.errprint("3")
                # try:
                customer = frappe.get_last_doc("Customer",filters = {"mobile_no":mobile})
                if customer:
                    # frappe.errprint("Customer Already Exists")
                    # frappe.errprint("Customer Already Exists")
                    frappe.local.response["message"] = {
                    "success_key": 1,
                    "message":"Customer Already Exists",
                    "data": 
                    {
                        # "opportunity_id":oppor_exists.name
                        "stage": customer.fsl_activation_status
                    } 
                    }
                # except: 
                #     frappe.local.response["message"] = {
                #         "success_key": 1,
                #         "message":"Customer Not Exists",
                #         # "data": 
                #         # {
                #         #     # "opportunity_id":oppor_exists.name
                #         #     # "stage": customer.fsl_activation_status
                #         # } 
                #         }

            except:
                try:
                    oppor_exists = frappe.get_last_doc("Opportunity",filters = {"fsl_mobile_num":mobile})
                    
                    if oppor_exists:
                        # frappe.errprint("12345")
                        # frappe.errprint("4")
                        # oppor_exists.fsl_referral_by = referral_by
                        # oppor_exists.save()
                        # frappe.errprint("Opportunity Already Exists and Referral ID is Updated")
                        frappe.local.response["message"] = {
                            "success_key": 1,
                            "message":"Opportunity Already Exists",
                            "data": 
                            {
                                "opportunity_id":oppor_exists.name,
                                "stage":oppor_exists.fsl_stage,
                                "Referral Id" : oppor_exists.fsl_referral_by
                            } 
                        } 
                except: 
                    try:
                        lead_exists = frappe.db.exists("Lead",{"mobile_no":mobile})
                        # frappe.errprint(lead_exists)

                        if lead_exists:
                            lead_doc = frappe.get_last_doc("Lead",filters={"mobile_no":mobile})
                            oppor = frappe.new_doc("Opportunity")
                            # oppor.fsl_active_status = 1
                            oppor.opportunity_from = "Lead"
                            oppor.party_name = lead_doc.name
                            oppor.fsl_stage = 0.5
                            oppor.fsl_user_name = mobile
                            if lead_doc.fsl_referral_rm:
                                oppor.fsl_referral_by = lead_doc.fsl_referral_rm
                                oppor.fsl_mode_of_application = "Referral"
                            else :
                                oppor.fsl_referral_by = referral_by
                                oppor.fsl_mode_of_application = fsl_mode_of_application
                            oppor.fsl_mobile_num = mobile
                            oppor.status = "In-Progress"                            
                            oppor.fsl_sms_verified = 1
                            oppor.fsl_sms_otp = otp
                            oppor.append("fsl_stage_table", {
                                "stages": "0.5",
                                "timing": current_datetime.strftime('%Y-%m-%d %H:%M:%S')
                            })
                            oppor.insert()
                            # oppor.db.commit()
                            # frappe.errprint(oppor.fsl_referral_by)
                            frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"Opportunity Created",
                                "data": 
                                {
                                    "opportunity": oppor.name,
                                    "stage":oppor.fsl_stage,
                                    "fsl_mode_of_application" : oppor.fsl_mode_of_application
                                } 
                            } 
                    # except:
                    #     frappe.local.response["message"] = {
                    #         "success_key": 1,
                    #         "message":"Lead not Exists"
                            
                    #     } 
                    except Exception as e:
                        frappe.local.response["message"] = {
                            "error": f"An error occurred: {str(e)}"
                        }
        