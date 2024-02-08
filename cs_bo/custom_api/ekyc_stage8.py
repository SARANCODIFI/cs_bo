import frappe
from datetime import datetime, date

@frappe.whitelist()
def get_opportunity_nominee_details(name):
    data = []
    try:
        customer_data = frappe.get_last_doc("Opportunity",filters={'name':name}) if frappe.db.exists("Opportunity",{'name':name}) else "This Session User can't Access This Opportunity"
        if customer_data != "This Session User can't Access This Opportunity":
            for custom in customer_data.fsl_nominee_table:
                custom_dic = {}
                custom_dic["nominee_number"] = custom.nominee_number
                custom_dic["nominee_fname"] = custom.nominee_fname
                custom_dic["nominee_lname"] = custom.nominee_lname
                custom_dic["relationship"] = custom.relationship
                custom_dic["date_of_birth"] = custom.date_of_birth
                custom_dic["percentage_allocation"] = custom.percentage_allocation
                custom_dic["mobile_number"] = custom.mobile_number
                # custom_dic["pan"] = custom.pan
                custom_dic["proof_id"] = custom.proof_id
                custom_dic["proof_type"] = custom.proof_type
                custom_dic["nominee_attch_url"] = custom.nominee_attch_url
                custom_dic["email_id"] = custom.email_id
                custom_dic["address"] = custom.address
                custom_dic["address_2"] = custom.address_2
                custom_dic["address_3"] = custom.address_3
                custom_dic["city"] = custom.city
                custom_dic["state"] = custom.state
                custom_dic["pincode"] = custom.pincode
                custom_dic["guardian_fname"] = custom.guardian_fname
                custom_dic["guardian_lname"] = custom.guardian_lname
                custom_dic["guardian_relationship"] = custom.guardian_relationship
                custom_dic["guardian_dob"] = custom.guardian_dob
                custom_dic["guardian_pan"] = custom.guardian_pan
                custom_dic["guardian_phone_no"] = custom.guardian_phone_no
                custom_dic["guardian_email_id"] = custom.guardian_email_id
                custom_dic["guardian_address1"] = custom.guardian_address1
                custom_dic["guardian_address2"] = custom.guardian_address2
                custom_dic["guardian_city"] = custom.guardian_city
                custom_dic["guardian_state"] = custom.guardian_state
                custom_dic["guardian_pincode"] = custom.guardian_pincode
                custom_dic["guardian_proof_id"] = custom.guardian_proof_id
                custom_dic["guardian_prooftype"] = custom.guardian_prooftype
                custom_dic["guardian_attachment_url"] = custom.guardian_attachment_url
                custom_dic["guardian_active_status"] = custom.guardian_active_status
                custom_dic["nominee_status"] = custom.nominee_status
                custom_dic["nominee_remarks"] = custom.nominee_remarks


                data.append(custom_dic)
        else:
            data= "This Session User can't Access This Opportunity"
    except Exception as e:
        data = f"An error occurred while processing the request: {str(e)}"
        
    frappe.local.response["message"] = {
        "success_key": 1,
        "data": {
            "fsl_nominee_details":data
        }        
    }

@frappe.whitelist()
def put_nominee_details(data):
    try :

        table = data.get("fsl_nominee_details")
       
        
        for i in table:
                        
            try:
                customer_data = frappe.get_last_doc("Opportunity", filters={'name': i["name"]})
            
                if not customer_data:
                    frappe.response["message"] = {
                        "error":"No Opportunity document found for this user"
                    }               
                else:
                    oppdatas = []
                    for j in customer_data.fsl_nominee_table:
                         
                 
                        if j.nominee_number != i["nominee_number"]:
                            
                            frappe.response["message"] = {
                                "error":"No Nominee document found for this user.",
                                "user" : i["nominee_number"],
                                "doc": j.nominee_number
                            } 

                        elif j.nominee_number == i["nominee_number"]:
                                                                            
                            # total_percentage = 0
                            
                            # for nominee in customer_data.fsl_nominee_table:
                                # if nominee.percentage_allocation is not None:
                                #     total_percentage += nominee.percentage_allocation

                            # if (total_percentage+i["percentage_allocation"]) > 100:
                            #     frappe.local.response["message"] = {
                            #     "error" : "Total percentage allocation cannot exceed 100%"
                            #     }
                            
                            # else:
                            #     if i["date_of_birth"] is not None:
            
                            #         if isinstance(i["date_of_birth"], date):
                            #             birth_date = i["date_of_birth"] 
                            #         else:
                            #             birth_date_str = i["date_of_birth"]  
                            #             birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()

                            #         today = datetime.now().date()
                            #         age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

                            #         if age < 18 :

                            #             if i["guardian_fname"] is None:
                            #                 frappe.local.response["error"] = {
                            #                     "error" : "Guardian is mandatory for age below 18 Nominee"
                            #                     }      
                                
                                        # else :  
                                            datas = {}   
                                            datas["opportunity_id"]  = i["name"]
                                            
                                            if "nominee_number" in i:
                                                j.nominee_number = i["nominee_number"]   
                                                datas["nominee_number"]  = i["nominee_number"] if "nominee_number" in i else None 
                                                                                         
                                            if "relationship" in i:
                                                j.relationship = i["relationship"]
                                                datas["relationship"]  = i["relationship"] if "relationship" in i else None
                                                
                                            if "date_of_birth" in i:
                                                j.date_of_birth = i["date_of_birth"]
                                                datas["date_of_birth"] = i["date_of_birth"] if "date_of_birth" in i else None
                                                
                                            if "percentage_allocation" in i:
                                                j.percentage_allocation = i["percentage_allocation"]
                                                datas["percentage_allocation"] = i["percentage_allocation"] if "percentage_allocation" in i else None
                                                
                                            if "guardian" in i:
                                                j.guardian = i["guardian"]
                                            if "mobile_number" in i:
                                                j.mobile_number = i["mobile_number"]
                                                datas["mobile_number"] = i["mobile_number"] if "mobile_number" in i else None
                                                
                                            if "pan" in i:
                                                j.pan = i["pan"]
                                                datas["pan"] = i["pan"] if "pan" in i else None
                                                
                                            if "email_id" in i:
                                                j.email_id = i["email_id"]
                                                datas["email_id"] = i["email_id"] if "email_id" in i else None
                                                
                                            if "address" in i:
                                                j.address = i["address"]
                                                datas["address"] = i["address"] if "address" in i else None
                                                
                                            if "address_2" in i:
                                                j.address_2 = i["address_2"]
                                                datas["address_2"] = i["address_2"] if "address_2" in i else None
                                                
                                            if "pincode" in i:
                                                i.pincode = i["pincode"]
                                                datas["pincode"] = i["pincode"] if "pincode" in i else None
                                                
                                            if "city" in i:
                                                j.city = i["city"]
                                                datas["city"] = i["city"] if "city" in i else None
                                                
                                            if "state" in i:
                                                j.state = i["state"]
                                                datas["state"] = i["state"] if "state" in i else None

                                            if "nominee_fname" in i:
                                                j.nominee_fname = i["nominee_fname"]
                                                datas["nominee_fname"] = i["nominee_fname"] if "nominee_fname" in i else None
                                                
                                            if "nominee_lname" in i:
                                                j.nominee_lname = i["nominee_lname"]
                                                datas["nominee_lname"] = i["nominee_lname"] if "nominee_lname" in i else None 
                                                
                                            if "proof_id" in i:
                                                j.state = i["proof_id"]
                                                datas["proof_id"] = i["proof_id"] if "proof_id" in i else None
                                                
                                            if "proof_type" in i:
                                                j.state = i["proof_type"]
                                                datas["proof_type"] = i["proof_type"] if "proof_type" in i else None
                                                
                                            if "nominee_attch_url" in i:
                                                j.nominee_attch_url = i["nominee_attch_url"]
                                                datas["nominee_attch_url"] = i["nominee_attch_url"] if "nominee_attch_url" in i else None

                                            if "guardian_fname" in i:
                                                j.guardian_fname = i["guardian_fname"]
                                                datas["guardian_fname"] = i["guardian_fname"] if "guardian_fname" in i else None
                                                
                                            if "guardian_lname" in i:
                                                j.guardian_lname = i["guardian_lname"]
                                                datas["guardian_lname"] = i["guardian_lname"] if "guardian_lname" in i else None

                                            if "guardian_relationship" in i:
                                                j.guardian_relationship = i["guardian_relationship"]
                                                datas["guardian_relationship"] = i["guardian_relationship"] if "guardian_relationship" in i else None
                                                
                                            if "guardian_dob" in i:
                                                j.guardian_dob = i["guardian_dob"]
                                                datas["guardian_dob"] = i["guardian_dob"] if "guardian_dob" in i else None
                                                
                                            if "guardian_pan" in i:
                                                j.guardian_pan = i["guardian_pan"]
                                                datas["guardian_pan"] = i["guardian_pan"] if "guardian_pan" in i else None
                                                
                                            if "guardian_phone_no" in i:
                                                j.guardian_phone_no = i["guardian_phone_no"]
                                                datas["guardian_phone_no"] = i["guardian_phone_no"] if "guardian_phone_no" in i else None
                                                
                                            if "guardian_email_id" in i:
                                                j.guardian_email_id = i["guardian_email_id"]
                                                datas["guardian_email_id"] = i["guardian_email_id"] if "guardian_email_id" in i else None
                                                
                                            if "guardian_address1" in i:
                                                j.guardian_address1 = i["guardian_address1"]
                                                datas["guardian_address1"] = i["guardian_address1"] if "guardian_address1" in i else None
                                                
                                            if "guardian_address2" in i:
                                                j.guardian_address2 = i["guardian_address2"]
                                                datas["guardian_address2"] = i["guardian_address2"] if "guardian_address2" in i else None
                                                
                                            if "guardian_city" in i:
                                                j.guardian_city = i["guardian_city"]
                                                datas["guardian_city"] = i["guardian_city"] if "guardian_city" in i else None
                                                
                                            if "guardian_state" in i:
                                                j.guardian_state = i["guardian_state"]
                                                datas["guardian_state"] = i["guardian_state"] if "guardian_state" in i else None
                                                
                                            if "guardian_pincode" in i:
                                                j.guardian_pincode = i["guardian_pincode"]
                                                datas["guardian_pincode"] = i["guardian_pincode"] if "guardian_pincode" in i else None
                                                
                                            if "guardian_proof_id" in i:
                                                j.guardian_proof_id = i["guardian_proof_id"]
                                                datas["guardian_proof_id"] = i["guardian_proof_id"] if "guardian_proof_id" in i else None
                                                
                                            if "guardian_prooftype" in i:
                                                j.guardian_prooftype = i["guardian_prooftype"]
                                                datas["guardian_prooftype"] = i["guardian_prooftype"] if "guardian_prooftype" in i else None
                                                
                                            if "guardian_attachment_url" in i:
                                                j.guardian_attachment_url = i["guardian_attachment_url"]
                                                datas["guardian_attachment_url"] = i["guardian_attachment_url"] if "guardian_attachment_url" in i else None
                                                
                                            if "guardian_active_status" in i:
                                                j.guardian_active_status = i["guardian_active_status"]
                                                datas["guardian_active_status"] = i["guardian_active_status"] if "guardian_active_status" in i else None

                                            
                                            oppdatas.append(datas)
                                            customer_data.save()
                                            
                                            frappe.response["message"] = {
                                                "Success key" : "1",
                                                "data appended":oppdatas
                                            }
                                            break
                                #     else :     
                                #             success = 1
                                #             if "nominee_number" in i:
                                #                 j.nominee_number = i["nominee_number"]
                                #             if "relationship" in i:
                                #                 j.relationship = i["relationship"]
                                #             if "date_of_birth" in i:
                                #                 j.date_of_birth = i["date_of_birth"]
                                #             if "percentage_allocation" in i:
                                #                 j.percentage_allocation = i["percentage_allocation"]
                                #             if "guardian" in i:
                                #                 j.guardian = i["guardian"]
                                #             if "mobile_number" in i:
                                #                 j.mobile_number = i["mobile_number"]
                                #             if "pan" in i:
                                #                 j.pan = i["pan"]
                                #             if "email_id" in i:
                                #                 j.email_id = i["email_id"]
                                #             if "address" in i:
                                #                 j.address = i["address"]
                                #             if "address_2" in i:
                                #                 j.address_2 = i["address_2"]
                                #             if "city" in i:
                                #                 j.city = i["city"]
                                #             if "state" in i:
                                #                 j.state = i["state"]
                                #             if "nominee_fname" in i:
                                #                 j.nominee_fname = i["nominee_fname"]
                                #             if "nominee_lname" in i:
                                #                 j.nominee_lname = i["nominee_lname"]
                                #             if "proof_id" in i:
                                #                 j.state = i["proof_id"]
                                #             if "proof_type" in i:
                                #                 j.state = i["proof_type"]
                                #             if "nominee_attch_url" in i:
                                #                 j.address_3 = i["nominee_attch_url"]

                                #             if "guardian_fname" in i:
                                #                 j.guardian_fname = i["guardian_fname"]
                                #             if "guardian_lname" in i:
                                #                 j.guardian_lname = i["guardian_lname"]
                                #             if "guardian_relationship" in i:
                                #                 j.guardian_relationship = i["guardian_relationship"]
                                #             if "guardian_dob" in i:
                                #                 j.guardian_dob = i["guardian_dob"]
                                #             if "guardian_pan" in i:
                                #                 j.guardian_pan = i["guardian_pan"]
                                #             if "guardian_phone_no" in i:
                                #                 j.guardian_phone_no = i["guardian_phone_no"]
                                #             if "guardian_email_id" in i:
                                #                 j.guardian_email_id = i["guardian_email_id"]
                                #             if "guardian_address1" in i:
                                #                 j.guardian_address1 = i["guardian_address1"]
                                #             if "guardian_address2" in i:
                                #                 j.guardian_address2 = i["guardian_address2"]
                                #             if "guardian_city" in i:
                                #                 j.guardian_city = i["guardian_city"]
                                #             if "guardian_state" in i:
                                #                 j.guardian_state = i["guardian_state"]
                                #             if "guardian_pincode" in i:
                                #                 j.guardian_pincode = i["guardian_pincode"]
                                #             if "guardian_proof_id" in i:
                                #                 j.guardian_proof_id = i["guardian_proof_id"]
                                #             if "guardian_prooftype" in i:
                                #                 j.guardian_prooftype = i["guardian_prooftype"]
                                #             if "guardian_attachment_url" in i:
                                #                 j.guardian_attachment_url = i["guardian_attachment_url"]
                                #             if "guardian_active_status" in i:
                                #                 j.guardian_active_status = i["guardian_active_status"]

                                #             customer_data.save()
                                #             result_data.append({ 
                                                
                                #                 "nominee_number": i["nominee_number"] if "nominee_number" in i else None,
                                #                 "nominee_fname": i["nominee_fname"] if "nominee_fname" in i else None,
                                #                 "nominee_lname": i["nominee_lname"] if "nominee_lname" in i else None,
                                #                 "relationship": i["relationship"] if "relationship" in i else None,
                                #                 "date_of_birth": i["date_of_birth"] if "date_of_birth" in i else None,
                                #                 "percentage_allocation": i["percentage_allocation"] if "percentage_allocation" in i else None,
                                #                 "mobile_number": i["mobile_number"] if "mobile_number" in i else None,
                                #                 "pan": i["pan"] if "pan" in i else None,
                                #                 "proof_id": i["proof_id"] if "proof_id" in i else None,
                                #                 "proof_type": i["proof_type"] if "proof_type" in i else None,
                                #                 "nominee_attch_url": i["nominee_attch_url"] if "nominee_attch_url" in i else None,
                                #                 "email_id": i["email_id"] if "email_id" in i else None,
                                #                 "address": i["address"] if "address" in i else None,
                                #                 "address_2": i["address_2"] if "address_2" in i else None,
                                #                 "city": i["city"] if "city" in i else None,
                                #                 "state": i["state"] if "state" in i else None,
                                #                 "pincode": i["pincode"] if "pincode" in i else None,
                                #                 "guardian_fname": i["guardian_fname"] if "guardian_fname" in i else None,
                                #                 "guardian_lname": i["guardian_lname"] if "guardian_lname" in i else None,
                                #                 "guardian_relationship": i["guardian_relationship"] if "guardian_relationship" in i else None,
                                #                 "guardian_dob": i["guardian_dob"] if "guardian_dob" in i else None,
                                #                 "guardian_pan": i["guardian_pan"] if "guardian_pan" in i else None,
                                #                 "guardian_phone_no": i["guardian_phone_no"] if "guardian_phone_no" in i else None,
                                #                 "guardian_email_id": i["guardian_email_id"] if "guardian_email_id" in i else None,
                                #                 "guardian_address1": i["guardian_address1"] if "guardian_address1" in i else None,
                                #                 "guardian_address2": i["guardian_address2"] if "guardian_address2" in i else None,
                                #                 "guardian_city": i["guardian_city"] if "guardian_city" in i else None,
                                #                 "guardian_state": i["guardian_state"] if "guardian_state" in i else None,
                                #                 "guardian_pincode": i["guardian_pincode"] if "guardian_pincode" in i else None,
                                #                 "guardian_proof_id": i["guardian_proof_id"] if "guardian_proof_id" in i else None,
                                #                 "guardian_prooftype": i["guardian_prooftype"] if "guardian_prooftype" in i else None,
                                #                 "guardian_attachment_url": i["guardian_attachment_url"] if "guardian_attachment_url" in i else None,
                                #                 "guardian_active_status": i["guardian_active_status"] if "guardian_active_status" in i else None,

                                #             })
                                #             frappe.response["message"] = {
                                #                 "Success key" : 1,
                                #                 "data appended":result_data
                                #             }
                                #             break
                                #  else:
                                #     frappe.local.response["error"] = {
                                #             "error" : "Error: Date of birth is None or empty"
                                #             }
            except Exception as e:
                frappe.local.response["message"] = {
                    "error": f"An error occurred: {str(e)}"
                }            
            # except Exception as e:
            #     frappe.local.response["message"] = {
            #         "error" : "Opportunity not found"
            #         }  
        
    except Exception as e:
        frappe.local.response["message"] = {
        "error" : "An errors occurred while processing the request"
            }


@frappe.whitelist()
def post_opportunity_nominee_details(data):
    
    table = data.get("fsl_nominee_details")
        
    result_data = [] 
    method = 0
    
    for i in table: 
            try:
                customer_data = frappe.get_last_doc("Opportunity", filters={'name': i["name"]})

                for j in customer_data.fsl_nominee_table:
                     
                    method = 1
                    if not customer_data:
                        frappe.local.response["error"] = {
                        "error" : "No Opportunity document found for this user",                        
                        }                        
                    else:                                               
                            if len(customer_data.fsl_nominee_table)<3:  
                                Success = 1
                                create_nominee(result_data,i,customer_data)
                                break
                            else:
                                frappe.local.response["error"] = {
                                    "error" : "Maximum 3 Nominee is Allowed to Add"
                                    }
                if  method == 0:
                    create_nominee(result_data,i,customer_data)                            
            except Exception as e:
                frappe.local.response["message"] = {
                    "error": "An errors occurred while processing the request"
                }
    


def create_nominee(result_data,i,customer_data):
    total_percentage = 0
    Success = 1
                                
    for nominee in customer_data.fsl_nominee_table:
        if nominee.percentage_allocation is not None:
            total_percentage += nominee.percentage_allocation

    if (total_percentage+i["percentage_allocation"]) > 100:
        frappe.local.response["error"] = {
        "error" : "Total percentage allocation cannot exceed 100%"
        }

    else:
       
        if i["date_of_birth"] is not None:

            if isinstance(i["date_of_birth"], date):
                birth_date = i["date_of_birth"]
            else:
                birth_date_str = i["date_of_birth"] 
                birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()

            today = datetime.now().date()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
            if age < 18 :
                if i["guardian_fname"] is None:
                    frappe.local.response["error"] = {
                        "error" : "Guardian is mandatory for age below 18 Nominee"
                        }      
        
                else :
                    
                    customer_data.append("fsl_nominee_table", {
                        "opportunity_id": i["name"],
                        "nominee_number": i["nominee_number"] if "nominee_number" in i else None,
                        "nominee_fname": i["nominee_fname"] if "nominee_fname" in i else None,
                        "nominee_lname": i["nominee_lname"] if "nominee_lname" in i else None,
                        "relationship": i["relationship"] if "relationship" in i else None,
                        "date_of_birth": i["date_of_birth"] if "date_of_birth" in i else None,
                        "percentage_allocation": i["percentage_allocation"] if "percentage_allocation" in i else None,
                        "mobile_number": i["mobile_number"] if "mobile_number" in i else None,
                        "pan": i["pan"] if "pan" in i else None,
                        "proof_id": i["proof_id"] if "proof_id" in i else None,
                        "proof_type": i["proof_type"] if "proof_type" in i else None,
                        "nominee_attch_url": i["nominee_attch_url"] if "nominee_attch_url" in i else None,
                        "email_id": i["email_id"] if "email_id" in i else None,
                        "address": i["address"] if "address" in i else None,
                        "address_2": i["address_2"] if "address_2" in i else None,
                        "city": i["city"] if "city" in i else None,
                        "state": i["state"] if "state" in i else None,
                        "pincode": i["pincode"] if "pincode" in i else None,
                        "guardian_fname": i["guardian_fname"] if "guardian_fname" in i else None,
                        "guardian_lname": i["guardian_lname"] if "guardian_lname" in i else None,
                        "guardian_relationship": i["guardian_relationship"] if "guardian_relationship" in i else None,
                        "guardian_dob": i["guardian_dob"] if "guardian_dob" in i else None,
                        "guardian_pan": i["guardian_pan"] if "guardian_pan" in i else None,
                        "guardian_phone_no": i["guardian_phone_no"] if "guardian_phone_no" in i else None,
                        "guardian_email_id": i["guardian_email_id"] if "guardian_email_id" in i else None,
                        "guardian_address1": i["guardian_address1"] if "guardian_address1" in i else None,
                        "guardian_address2": i["guardian_address2"] if "guardian_address2" in i else None,
                        "guardian_city": i["guardian_city"] if "guardian_city" in i else None,
                        "guardian_state": i["guardian_state"] if "guardian_state" in i else None,
                        "guardian_pincode": i["guardian_pincode"] if "guardian_pincode" in i else None,
                        "guardian_proof_id": i["guardian_proof_id"] if "guardian_proof_id" in i else None,
                        "guardian_prooftype": i["guardian_prooftype"] if "guardian_prooftype" in i else None,
                        "guardian_attachment_url": i["guardian_attachment_url"] if "guardian_attachment_url" in i else None,
                        "guardian_active_status": i["guardian_active_status"] if "guardian_active_status" in i else None,

                    })
                    customer_data.save()
                    result_data.append({    
                        "opportunity_id": i["name"],
                        "nominee_number": i["nominee_number"] if "nominee_number" in i else None,
                        "nominee_fname": i["nominee_fname"] if "nominee_fname" in i else None,
                        "nominee_lname": i["nominee_lname"] if "nominee_lname" in i else None,
                        "relationship": i["relationship"] if "relationship" in i else None,
                        "date_of_birth": i["date_of_birth"] if "date_of_birth" in i else None,
                        "percentage_allocation": i["percentage_allocation"] if "percentage_allocation" in i else None,
                        "mobile_number": i["mobile_number"] if "mobile_number" in i else None,
                        "pan": i["pan"] if "pan" in i else None,
                        "proof_id": i["proof_id"] if "proof_id" in i else None,
                        "proof_type": i["proof_type"] if "proof_type" in i else None,
                        "nominee_attch_url": i["nominee_attch_url"] if "nominee_attch_url" in i else None,
                        "email_id": i["email_id"] if "email_id" in i else None,
                        "address": i["address"] if "address" in i else None,
                        "address_2": i["address_2"] if "address_2" in i else None,
                        "city": i["city"] if "city" in i else None,
                        "state": i["state"] if "state" in i else None,
                        "pincode": i["pincode"] if "pincode" in i else None,
                        "guardian_fname": i["guardian_fname"] if "guardian_fname" in i else None,
                        "guardian_lname": i["guardian_lname"] if "guardian_lname" in i else None,
                        "guardian_relationship": i["guardian_relationship"] if "guardian_relationship" in i else None,
                        "guardian_dob": i["guardian_dob"] if "guardian_dob" in i else None,
                        "guardian_pan": i["guardian_pan"] if "guardian_pan" in i else None,
                        "guardian_phone_no": i["guardian_phone_no"] if "guardian_phone_no" in i else None,
                        "guardian_email_id": i["guardian_email_id"] if "guardian_email_id" in i else None,
                        "guardian_address1": i["guardian_address1"] if "guardian_address1" in i else None,
                        "guardian_address2": i["guardian_address2"] if "guardian_address2" in i else None,
                        "guardian_city": i["guardian_city"] if "guardian_city" in i else None,
                        "guardian_state": i["guardian_state"] if "guardian_state" in i else None,
                        "guardian_pincode": i["guardian_pincode"] if "guardian_pincode" in i else None,
                        "guardian_proof_id": i["guardian_proof_id"] if "guardian_proof_id" in i else None,
                        "guardian_prooftype": i["guardian_prooftype"] if "guardian_prooftype" in i else None,
                        "guardian_attachment_url": i["guardian_attachment_url"] if "guardian_attachment_url" in i else None,
                        "guardian_active_status": i["guardian_active_status"] if "guardian_active_status" in i else None,
                                
                    })
                    frappe.response["message"] = {
                        "Success key" : 1,
                        "data appended":result_data
                    }
            else :
                
                    
                new_id = frappe.generate_hash(length=2)
                customer_data.append("fsl_nominee_table", {
                        
                    "nominee_number": i["nominee_number"] if "nominee_number" in i else None,
                    "nominee_fname": i["nominee_fname"] if "nominee_fname" in i else None,
                    "nominee_lname": i["nominee_lname"] if "nominee_lname" in i else None,
                    "relationship": i["relationship"] if "relationship" in i else None,
                    "date_of_birth": i["date_of_birth"] if "date_of_birth" in i else None,
                    "percentage_allocation": i["percentage_allocation"] if "percentage_allocation" in i else None,
                    "mobile_number": i["mobile_number"] if "mobile_number" in i else None,
                    "pan": i["pan"] if "pan" in i else None,
                    "proof_id": i["proof_id"] if "proof_id" in i else None,
                    "proof_type": i["proof_type"] if "proof_type" in i else None,
                    "nominee_attch_url": i["nominee_attch_url"] if "nominee_attch_url" in i else None,
                    "email_id": i["email_id"] if "email_id" in i else None,
                    "address": i["address"] if "address" in i else None,
                    "address_2": i["address_2"] if "address_2" in i else None,
                    "city": i["city"] if "city" in i else None,
                    "state": i["state"] if "state" in i else None,
                    "pincode": i["pincode"] if "pincode" in i else None,
                    "guardian_fname": i["guardian_fname"] if "guardian_fname" in i else None,
                    "guardian_lname": i["guardian_lname"] if "guardian_lname" in i else None,
                    "guardian_relationship": i["guardian_relationship"] if "guardian_relationship" in i else None,
                    "guardian_dob": i["guardian_dob"] if "guardian_dob" in i else None,
                    "guardian_pan": i["guardian_pan"] if "guardian_pan" in i else None,
                    "guardian_phone_no": i["guardian_phone_no"] if "guardian_phone_no" in i else None,
                    "guardian_email_id": i["guardian_email_id"] if "guardian_email_id" in i else None,
                    "guardian_address1": i["guardian_address1"] if "guardian_address1" in i else None,
                    "guardian_address2": i["guardian_address2"] if "guardian_address2" in i else None,
                    "guardian_city": i["guardian_city"] if "guardian_city" in i else None,
                    "guardian_state": i["guardian_state"] if "guardian_state" in i else None,
                    "guardian_pincode": i["guardian_pincode"] if "guardian_pincode" in i else None,
                    "guardian_proof_id": i["guardian_proof_id"] if "guardian_proof_id" in i else None,
                    "guardian_prooftype": i["guardian_prooftype"] if "guardian_prooftype" in i else None,
                    "guardian_attachment_url": i["guardian_attachment_url"] if "guardian_attachment_url" in i else None,
                    "guardian_active_status": i["guardian_active_status"] if "guardian_active_status" in i else None,
    
                    
                })
                customer_data.save()
                result_data.append({    
                    "opportunity_id": i["name"],
                    "nominee_number": i["nominee_number"] if "nominee_number" in i else None,
                    "nominee_fname": i["nominee_fname"] if "nominee_fname" in i else None,
                    "nominee_lname": i["nominee_lname"] if "nominee_lname" in i else None,
                    "relationship": i["relationship"] if "relationship" in i else None,
                    "date_of_birth": i["date_of_birth"] if "date_of_birth" in i else None,
                    "percentage_allocation": i["percentage_allocation"] if "percentage_allocation" in i else None,
                    "mobile_number": i["mobile_number"] if "mobile_number" in i else None,
                    "pan": i["pan"] if "pan" in i else None,
                    "proof_id": i["proof_id"] if "proof_id" in i else None,
                    "proof_type": i["proof_type"] if "proof_type" in i else None,
                    "nominee_attch_url": i["nominee_attch_url"] if "nominee_attch_url" in i else None,
                    "email_id": i["email_id"] if "email_id" in i else None,
                    "address": i["address"] if "address" in i else None,
                    "address_2": i["address_2"] if "address_2" in i else None,
                    "city": i["city"] if "city" in i else None,
                    "state": i["state"] if "state" in i else None,
                    "pincode": i["pincode"] if "pincode" in i else None,
                    "guardian_fname": i["guardian_fname"] if "guardian_fname" in i else None,
                    "guardian_lname": i["guardian_lname"] if "guardian_lname" in i else None,
                    "guardian_relationship": i["guardian_relationship"] if "guardian_relationship" in i else None,
                    "guardian_dob": i["guardian_dob"] if "guardian_dob" in i else None,
                    "guardian_pan": i["guardian_pan"] if "guardian_pan" in i else None,
                    "guardian_phone_no": i["guardian_phone_no"] if "guardian_phone_no" in i else None,
                    "guardian_email_id": i["guardian_email_id"] if "guardian_email_id" in i else None,
                    "guardian_address1": i["guardian_address1"] if "guardian_address1" in i else None,
                    "guardian_address2": i["guardian_address2"] if "guardian_address2" in i else None,
                    "guardian_city": i["guardian_city"] if "guardian_city" in i else None,
                    "guardian_state": i["guardian_state"] if "guardian_state" in i else None,
                    "guardian_pincode": i["guardian_pincode"] if "guardian_pincode" in i else None,
                    "guardian_proof_id": i["guardian_proof_id"] if "guardian_proof_id" in i else None,
                    "guardian_prooftype": i["guardian_prooftype"] if "guardian_prooftype" in i else None,
                    "guardian_attachment_url": i["guardian_attachment_url"] if "guardian_attachment_url" in i else None,
                    "guardian_active_status": i["guardian_active_status"] if "guardian_active_status" in i else None,
                            
                })
                frappe.response["message"] = {
                        "Success key" : 1,
                        "data appended":result_data
                    }
        else:
            frappe.local.response["error"] = {
                    "error" : "Error: Date of birth is None or empty"
                    }
    return result_data,Success


@frappe.whitelist(allow_guest=True)
def delete_opportunity_nominee_details(name,nominee_number):
        
    customer_data = frappe.get_last_doc("Opportunity", filters={'name':name})

    for entry in customer_data.get("fsl_nominee_table"):
        if entry.get("nominee_number") == nominee_number:
            customer_data.get("fsl_nominee_table").remove(entry)
            customer_data.save()
            
    frappe.local.response["message"] = {
        "success_key": 1,
    }
