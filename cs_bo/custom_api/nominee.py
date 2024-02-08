import frappe
from datetime import datetime, date

@frappe.whitelist(allow_guest=True)
def get_customer_nominee_details(id):
    data = []
    try:
        customer_data = frappe.get_last_doc("Customer",filters={'fsl_ucc_code':id})

        for custom in customer_data.fsl_nominee_details:
            custom_dic = {}
            custom_dic["nominee_number"] = custom.nominee_number
            custom_dic["nominee_name"] = custom.nominee_name
            custom_dic["relationship"] = custom.relationship
            custom_dic["date_of_birth"] = custom.date_of_birth
            custom_dic["percentage_allocation"] = custom.percentage_allocation
            custom_dic["guardian"] = custom.guardian
            custom_dic["mobile_number"] = custom.mobile_number
            custom_dic["pan"] = custom.pan
            custom_dic["email_id"] = custom.email_id
            custom_dic["address"] = custom.address
            custom_dic["address_2"] = custom.address_2
            custom_dic["address_3"] = custom.address_3
            custom_dic["city"] = custom.city
            custom_dic["state"] = custom.state
            custom_dic["pincode"] = custom.pincode
            custom_dic["unique_id"] = custom.unique_id

            data.append(custom_dic)
        
        frappe.local.response["message"] = {
            "success_key": 1,
            "data": {
                "fsl_nominee_details":data
            }        
        }
        
    except:
        frappe.response["message"] = {
            "error":"This Session User can't Access This Customer"
        } 
        
        

@frappe.whitelist(allow_guest=True)
def put_nominee_details(data):
    table = data.get("fsl_nominee_details")
    result_data = []  
    
    for i in table:
        
        try:

            customer_data = frappe.get_last_doc("Customer", filters={'fsl_ucc_code': table.fsl_ucc_code})
           
            if not customer_data:
                frappe.response["message"] = {
                    "error":"No Customer document found for this user"
                }               
            else:
                for j in customer_data.fsl_nominee_details:
                   
                    if j.unique_id != i["unique_id"]:
                        frappe.response["message"] = {
                            "error":"No Customer document found for this user3",
                            "user" : i["nominee_name"]
                        } 

                    else:
                                               
                        total_percentage = 0
                        
                        for nominee in customer_data.fsl_nominee_details:
                            if nominee.percentage_allocation is not None:
                                total_percentage += nominee.percentage_allocation

                        if (total_percentage+i["percentage_allocation"]) > 100:
                            frappe.local.response["message"] = {
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

                                    if i["guardian"] is None:
                                        frappe.local.response["error"] = {
                                            "error" : f"Guardian is mandatory for individuals below 18 for {i.relationship}"
                                            }      
                            
                                    else :     
                                        j.nominee_number = i["nominee_number"]
                                        j.nominee_name = i["nominee_name"]
                                        j.relationship = i["relationship"]
                                        j.date_of_birth =  i["date_of_birth"]
                                        j.percentage_allocation = i["percentage_allocation"]
                                        j.guardian = i["guardian"]
                                        j.mobile_number = i["mobile_number"]
                                        j.pan = i["pan"]
                                        j.email_id = i["email_id"]
                                        j.address = i["address"]
                                        j.address_2 = i["address_2"]
                                        j.address_3 = i["address_3"]
                                        j.city = i["city"]
                                        j.state = i["state"]
                                        j.pincode = i["pincode"]
                        
                                        customer_data.save()
                                        result_data.append({ 
                                            "success_key" : 2,
                                            "nominee_number" : i["nominee_number"],
                                            "nominee_name": i["nominee_name"],                           
                                            "relationship": i["relationship"],
                                            "date_of_birth": i["date_of_birth"],
                                            "percentage_allocation": i["percentage_allocation"],
                                            "guardian": i["guardian"],
                                            "mobile_number": i["mobile_number"],
                                            "pan": i["pan"],
                                            "email_id": i["email_id"],
                                            "address": i["address"],
                                            "address_2": i["address_2"],
                                            "address_3": i["address_3"],
                                            "city": i["city"],
                                            "state": i["state"],
                                            "pincode": i["pincode"],                                         
                                            
                                            "unique_id":i["unique_id"]
                                        })
                                else :     
                                        j.nominee_number = i["nominee_number"]
                                        j.nominee_name = i["nominee_name"]
                                        j.relationship = i["relationship"]
                                        j.date_of_birth =  i["date_of_birth"]
                                        j.percentage_allocation = i["percentage_allocation"]
                                        j.guardian = i["guardian"]
                                        j.mobile_number = i["mobile_number"]
                                        j.pan = i["pan"]
                                        j.email_id = i["email_id"]
                                        j.address = i["address"]
                                        j.address_2 = i["address_2"]
                                        j.address_3 = i["address_3"]
                                        j.city = i["city"]
                                        j.state = i["state"]
                                        j.pincode = i["pincode"]

                                        customer_data.save()
                                        result_data.append({ 
                                            "success_key" : 2,
                                            "nominee_number" : i["nominee_number"],
                                            "nominee_name": i["nominee_name"],                           
                                            "relationship": i["relationship"],
                                            "date_of_birth": i["date_of_birth"],
                                            "percentage_allocation": i["percentage_allocation"],
                                            "guardian": i["guardian"],
                                            "mobile_number": i["mobile_number"],
                                            "pan": i["pan"],
                                            "email_id": i["email_id"],
                                            "address": i["address"],
                                            "address_2": i["address_2"],
                                            "address_3": i["address_3"],
                                            "city": i["city"],
                                            "state": i["state"],
                                            "pincode": i["pincode"],                                         
                                            
                                            "unique_id":i["new_id"]
                                        })
                            else:
                                frappe.local.response["error"] = {
                                        "error" : "Error: Date of birth is None or empty"
                                        }
                    
        except Exception as e:
            frappe.local.response["message"] = {
            "error" : f"An error occurred while processing the request: {str(e)}"
                }
    frappe.response["message"] = {
        "success_key":  "success_key",
        "data":result_data
     }


@frappe.whitelist(allow_guest=True)
def post_customer_nominee_details(data):
    table = data.get("fsl_nominee_details")
    result_data = [] 
    method = 0
    Success = 0
    
    for i in table: 
            try:
                customer_data = frappe.get_last_doc("Customer", filters={'fsl_ucc_code': table.fsl_ucc_code}) 
                             
                for j in customer_data.fsl_nominee_details:
                           
                     
                    method = 1
                    if not customer_data:
                        frappe.local.response["error"] = {
                        "error" : "No Customer document found for this user",                        
                        }                        
                    else:                   
                        if j.email_id != i["email_id"]:
                             frappe.local.response["error"] = {
                                "error" : "No Customer document found for this user",
                                "nominee_name" : i["nominee_name"]
                                }                             
                        else:
                            
                            if len(customer_data.fsl_nominee_details)<3:  
                                Success = 1                       
                                create_nominee(result_data,i,customer_data)
                                break
                            else:
                                frappe.local.response["error"] = {
                                    "error" : "Maximum 3 Nominee is Allowed to Add"
                                    }
                if  method == 0:
                    Success = 2
                    create_nominee(result_data,i,customer_data)                            
            except Exception as e:
                frappe.local.response["error"] = {
                "error" : f"An error occurred while processing the request: {str(e)}"
                 }
    frappe.response["message"] = {
        "Success key" : Success,
        "data appended":result_data
     }
                         
    

@frappe.whitelist(allow_guest=True)
def delete_customer_nominee_details(unique_id,ucc):
    
    customer_data = frappe.get_last_doc("Customer", filters={'fsl_ucc_code': ucc})

    for entry in customer_data.get("fsl_nominee_details"):
        if entry.get("unique_id") == unique_id:
            customer_data.get("fsl_nominee_details").remove(entry)
            customer_data.save()
            
    frappe.local.response["message"] = {
        "success_key": 1,
    }


def create_nominee(result_data,i,customer_data):
    total_percentage = 0
    
                                
    for nominee in customer_data.fsl_nominee_details:
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
                if i["guardian"] is None:
                    frappe.local.response["error"] = {
                        "error" : f"Guardian is mandatory for individuals below 18 for {i.relationship}"
                        }      
        
                else :
                    
                    new_id = frappe.generate_hash(length=2)
                    customer_data.append("fsl_nominee_details", {

                        
                        "nominee_number" : i["nominee_number"],
                        "nominee_name": i["nominee_name"],                           
                        "relationship": i["relationship"],
                        "date_of_birth": i["date_of_birth"],
                        "percentage_allocation": i["percentage_allocation"],
                        "guardian": i["guardian"],
                        "mobile_number": i["mobile_number"],
                        "pan": i["pan"],
                        "email_id": i["email_id"],
                        "address": i["address"],
                        "address_2": i["address_2"],
                        "address_3": i["address_3"],
                        "city": i["city"],
                        "state": i["state"],
                        "pincode": i["pincode"],

                        "unique_id":new_id
                    })
                    result_data.append({    
                                                
                                    
                                    "nominee_number" : i["nominee_number"],
                                    "nominee_name": i["nominee_name"],                           
                                    "relationship": i["relationship"],
                                    "date_of_birth": i["date_of_birth"],
                                    "percentage_allocation": i["percentage_allocation"],
                                    "guardian": i["guardian"],
                                    "mobile_number": i["mobile_number"],
                                    "pan": i["pan"],
                                    "email_id": i["email_id"],
                                    "address": i["address"],
                                    "address_2": i["address_2"],
                                    "address_3": i["address_3"],
                                    "city": i["city"],
                                    "state": i["state"],
                                    "pincode": i["pincode"],
                                    "total_percentage" : total_percentage,
                                    "unique_id":new_id
                                
                    })
                    customer_data.save()
            else :
                
                    
                new_id = frappe.generate_hash(length=2)
                customer_data.append("fsl_nominee_details", {

                        
                        "nominee_number" : i["nominee_number"],
                        "nominee_name": i["nominee_name"],                           
                        "relationship": i["relationship"],
                        "date_of_birth": i["date_of_birth"],
                        "percentage_allocation": i["percentage_allocation"],
                        "guardian": i["guardian"],
                        "mobile_number": i["mobile_number"],
                        "pan": i["pan"],
                        "email_id": i["email_id"],
                        "address": i["address"],
                        "address_2": i["address_2"],
                        "address_3": i["address_3"],
                        "city": i["city"],
                        "state": i["state"],
                        "pincode": i["pincode"],
                        
                        "unique_id":new_id
                    
                })
                result_data.append({    
                        
                        "nominee_number" : i["nominee_number"],
                        "nominee_name": i["nominee_name"],                           
                        "relationship": i["relationship"],
                        "date_of_birth": i["date_of_birth"],
                        "percentage_allocation": i["percentage_allocation"],
                        "guardian": i["guardian"],
                        "mobile_number": i["mobile_number"],
                        "pan": i["pan"],
                        "email_id": i["email_id"],
                        "address": i["address"],
                        "address_2": i["address_2"],
                        "address_3": i["address_3"],
                        "city": i["city"],
                        "state": i["state"],
                        "pincode": i["pincode"],
                        
                        "unique_id":new_id
                            
                })
                customer_data.save()
        else:
            frappe.local.response["error"] = {
                    "error" : "Error: Date of birth is None or empty"
                    }
    return result_data


@frappe.whitelist(allow_guest=True)
def get_customer_details(ucc):
    try:
        success = 0
        customer = frappe.get_all("Customer",
            filters={"fsl_ucc_code": ucc},
            fields=["customer_name", "fsl_relation_code", "fsl_own_code", "fsl_team_leader", "fsl_account_opened_on", "fsl_dob", "fsl_region", "fsl_branch", "fsl_rm", "fsl_branch_id", "fsl_ucc_category", "fsl_authorize_type", "fsl_depository_participant", "fsl_activation_status", "fsl_introducer", "fsl_support_code", "customer_type", "fsl_ucc_code", "fsl_father_name", "fsl_mother_name", "fsl_gender", "fsl_marital_status", "fsl_occupation", "fsl_trading_experience", "fsl_politically_exposed_person", "fsl_fund_settlement_cycle", "fsl_net_worth", "fsl_annual_income", "fsl_sebi_action", "fsl_nse", "fsl_bse", "fsl_nfo", "fsl_bfo", "fsl_cds", "fsl_bcd", "fsl_mcx", "customer_primary_contact", "customer_primary_address"]
        )

        if customer:
            success = 1
            nominee_details = frappe.get_all("Nominee Details",
                filters={"parent": customer[0]["fsl_ucc_code"]},
                fields=["nominee_number", "nominee_name", "relationship", "date_of_birth", "percentage_allocation", "guardian", "mobile_number", "pan", "email_id", "address", "address_2", "address_3", "city", "state", "pincode", "unique_id"]
            )

            bank_details = frappe.get_all("Bank Details",
                filters={"parent": customer[0]["fsl_ucc_code"]},
                fields=["account_no", "branch", "bank_name", "ifsc_code", "micr_code"]
            )

            family_details = frappe.get_all("Family Details",
                filters={"parent": customer[0]["fsl_ucc_code"]},
                fields=["customer_ucc_code", "sub_account", "h_name", "sub_account_pan", "sub_account_mobile_no", "status"]
            )

            customer[0]["nominee_details"] = nominee_details
            customer[0]["bank_details"] = bank_details
            customer[0]["family_details"] = family_details
            
        else:
            frappe.response["message"] = {
                "1" : 2,
                "error": "Customer not found"
            }

        frappe.response["message"] = {
                "Success_key": success,
                "data": customer[0]
            }

    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }


@frappe.whitelist(allow_guest=True)
def post_customer_nominee_details(data):
    table = data.get("fsl_nominee_table")
    result_data = [] 
    method = 0
    Success = 0
    
    for i in table: 
            try:
                customer_data = frappe.get_last_doc("Customer", filters={"fsl_ucc_code":data.get("ucc")}) 
                             
                for j in customer_data.fsl_nominee_table:
                           
                     
                    method = 1
                    if not customer_data:
                        frappe.local.response["error"] = {
                        "error" : "No Customer document found for this user",                        
                        }                        
                    else:                   
                        if j.email_id != i["email_id"]:
                             frappe.local.response["error"] = {
                                "error" : "No Customer document found for this user",
                                "nominee_name" : i["nominee_name"]
                                }                             
                        else:
                            
                            if len(customer_data.fsl_nominee_table)<3:  
                                Success = 1                    
                                create_nominee(result_data,i,customer_data)
                                break
                                # total_percentage = 0
                                # ##
                                # for nominee in customer_data.fsl_nominee_details:
                                #     # frappe.errprint("22")
                                #     if nominee.percentage_allocation is not None:
                                #         # frappe.errprint("33")
                                #         total_percentage += nominee.percentage_allocation
                                #         # frappe.errprint(total_percentage)

                                # if (total_percentage+i["percentage_allocation"]) > 100:
                                #     # frappe.errprint("44")
                                #     frappe.local.response["error"] = {
                                #     "error" : "Total percentage allocation cannot exceed 100%"
                                #     }
                                
                                # else:
                                    
                                #     if i["date_of_birth"] is not None:
                
                                #         if isinstance(i["date_of_birth"], date):
                                #             birth_date = i["date_of_birth"] # It's already a datetime.date object
                                #         else:
                                #             birth_date_str = i["date_of_birth"]  # It's a string
                                #             birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()

                                #         # Calculate age
                                #         today = datetime.now().date()
                                #         age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

                                    
                                #         # frappe.errprint(age)
                                #         if age < 18 :
                                #             # frappe. msgprint("Guardian is mandatory for individuals Under 18.")
                                #             # frappe.throw(f"Guardian is mandatory for individuals above 18. age is :{str(age)}")

                                #             if i["guardian"] is None:
                                #                 frappe.local.response["error"] = {
                                #                     "error" : f"Guardian is mandatory for individuals below 18 for {i.relationship}"
                                #                     }      
                                 
                                #             else :

                                #                 new_id = frappe.generate_hash(length=2)
                                #                 # Append data to the Customer document
                                #                 customer_data.append("fsl_nominee_details", {

                                                  
                                #                     "nominee_number" : i["nominee_number"],
                                #                     "nominee_name": i["nominee_name"],                           
                                #                     "relationship": i["relationship"],
                                #                     "date_of_birth": i["date_of_birth"],
                                #                     "percentage_allocation": i["percentage_allocation"],
                                #                     "guardian": i["guardian"],
                                #                     "mobile_number": i["mobile_number"],
                                #                     "pan": i["pan"],
                                #                     "email_id": i["email_id"],
                                #                     "address": i["address"],
                                #                     "address_2": i["address_2"],
                                #                     "address_3": i["address_3"],
                                #                     "city": i["city"],
                                #                     "state": i["state"],
                                #                     "pincode": i["pincode"],

                                #                     "unique_id":new_id
                                #                 })
                                #                 result_data.append({    
                                                                         
                                #                                 "success_key" : 2,
                                #                                 "nominee_number" : i["nominee_number"],
                                #                                 "nominee_name": i["nominee_name"],                           
                                #                                 "relationship": i["relationship"],
                                #                                 "date_of_birth": i["date_of_birth"],
                                #                                 "percentage_allocation": i["percentage_allocation"],
                                #                                 "guardian": i["guardian"],
                                #                                 "mobile_number": i["mobile_number"],
                                #                                 "pan": i["pan"],
                                #                                 "email_id": i["email_id"],
                                #                                 "address": i["address"],
                                #                                 "address_2": i["address_2"],
                                #                                 "address_3": i["address_3"],
                                #                                 "city": i["city"],
                                #                                 "state": i["state"],
                                #                                 "pincode": i["pincode"],
                                #                                 "total_percentage" : total_percentage,
                                #                                 "unique_id":new_id
                                                            
                                #                 })
                                #                 customer_data.save()
                                #         else :
                                                
                                #             new_id = frappe.generate_hash(length=2)
                                #             # Append data to the Customer document
                                #             customer_data.append("fsl_nominee_details", {

                                                 
                                #                     "nominee_number" : i["nominee_number"],
                                #                     "nominee_name": i["nominee_name"],                           
                                #                     "relationship": i["relationship"],
                                #                     "date_of_birth": i["date_of_birth"],
                                #                     "percentage_allocation": i["percentage_allocation"],
                                #                     "guardian": i["guardian"],
                                #                     "mobile_number": i["mobile_number"],
                                #                     "pan": i["pan"],
                                #                     "email_id": i["email_id"],
                                #                     "address": i["address"],
                                #                     "address_2": i["address_2"],
                                #                     "address_3": i["address_3"],
                                #                     "city": i["city"],
                                #                     "state": i["state"],
                                #                     "pincode": i["pincode"],
                                                    
                                #                     "unique_id":new_id
                                                
                                #             })
                                #             result_data.append({    
                                #                     "success_key" : 2,
                                #                     "nominee_number" : i["nominee_number"],
                                #                     "nominee_name": i["nominee_name"],                           
                                #                     "relationship": i["relationship"],
                                #                     "date_of_birth": i["date_of_birth"],
                                #                     "percentage_allocation": i["percentage_allocation"],
                                #                     "guardian": i["guardian"],
                                #                     "mobile_number": i["mobile_number"],
                                #                     "pan": i["pan"],
                                #                     "email_id": i["email_id"],
                                #                     "address": i["address"],
                                #                     "address_2": i["address_2"],
                                #                     "address_3": i["address_3"],
                                #                     "city": i["city"],
                                #                     "state": i["state"],
                                #                     "pincode": i["pincode"],
                                                    
                                #                     "unique_id":new_id
                                                        
                                #             })
                                #             customer_data.save()
                                #     else:
                                #         frappe.local.response["error"] = {
                                #                 "error" : "Error: Date of birth is None or empty"
                                #                 }
                            else:
                                frappe.local.response["error"] = {
                                    "error" : "Maximum 3 Nominee is Allowed to Add"
                                    }
                if  method == 0:
                    Success = 2
                    create_nominee(result_data,i,customer_data)                            
            except Exception as e:
                frappe.local.response["error"] = {
                "error" : f"An error occurred while processing the request: {str(e)}"
                 }
    frappe.response["message"] = {
        "Success key" : Success,
        "data appended":result_data
     }
