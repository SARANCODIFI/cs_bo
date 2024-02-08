import frappe
from datetime import datetime, date

@frappe.whitelist(allow_guest=True)
def get_customer_nominee_details(ucc_code):
    data = []
    try:
        customer_data = frappe.get_last_doc("Customer",filters={'fsl_ucc_code':ucc_code}) if frappe.db.exists("Customer",{'fsl_ucc_code':ucc_code}) else "This Session User can't Access This Customer"
        if customer_data != "This Session User can't Access This Customer":
            for custom in customer_data.fsl_nominee_table:
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
        else:
            data= "This Session User can't Access This Customer"
    except Exception as e:
        data = f"An error occurred while processing the request: {str(e)}"
        
    frappe.local.response["message"] = {
        "success_key": 1,
        "data": {
            "fsl_nominee_details":data
        }        
    }

@frappe.whitelist(allow_guest=True)
def put_nominee_details(data):
    try :

        table = data.get("fsl_nominee_details")
        result_data = []  
        success = 0
        
        for i in table:
            
            try:
                customer_data = frappe.get_last_doc("Customer", filters={'fsl_ucc_code': data.get("ucc")})
            
                if not customer_data:
                    frappe.response["message"] = {
                        "error":"No Customer document found for this user"
                    }               
                else:
                    for j in customer_data.fsl_nominee_table:
                         
                 
                        if j.unique_id != i["unique_id"]:
                            frappe.response["message"] = {
                                "error":"No Customer document found for this user",
                                "user" : i["unique_id"]
                            } 

                        else:
                                                                            
                            total_percentage = 0
                            
                            for nominee in customer_data.fsl_nominee_table:
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
                                            success = 1
                                            customer_data.save()
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
                                                
                                                "unique_id":i["unique_id"]
                                            })
                                    else :     
                                            success = 1
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
                     
                    "error" : "Customer not found"
                    }  
        frappe.response["message"] = {
            "success_key":  success,
            "data":result_data
        }
    except Exception as e:
                frappe.local.response["message"] = {
                "error" : "Unable to process"
                    }


@frappe.whitelist(allow_guest=True)
def post_customer_nominee_details(data):
    
    table = data.get("fsl_nominee_details")
        
    result_data = [] 
    method = 0
    Success = 0
    
    for i in table: 
            try:
                customer_data = frappe.get_last_doc("Customer", filters={'fsl_ucc_code': data.get("ucc") })

                for j in customer_data.fsl_nominee_table:
                     
                    method = 1
                    if not customer_data:
                        frappe.local.response["error"] = {
                        "error" : "No Custoomer document found for this user",                        
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
                frappe.local.response["error"] = {
                "error" : f"An errors occurred while processing the request: {str(e)}"
                 }
    frappe.response["message"] = {
        "Success key" : Success,
        "data appended":result_data
     }


def create_nominee(result_data,i,customer_data):
    total_percentage = 0
    Success = 2
                                
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
                if i["guardian"] is None:
                    frappe.local.response["error"] = {
                        "error" : f"Guardian is mandatory for individuals below 18 for {i.relationship}"
                        }      
        
                else :
                    
                    new_id = frappe.generate_hash(length=2)
                    customer_data.append("fsl_nominee_table", {

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
            else :
                
                    
                new_id = frappe.generate_hash(length=2)
                customer_data.append("fsl_nominee_table", {

                        
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
        else:
            frappe.local.response["error"] = {
                    "error" : "Error: Date of birth is None or empty"
                    }
    return result_data,Success


@frappe.whitelist(allow_guest=True)
def delete_customer_nominee_details(ucc,unique_id):
        
    customer_data = frappe.get_last_doc("Customer", filters={'fsl_ucc_code':ucc})

    for entry in customer_data.get("fsl_nominee_table"):
        if entry.get("unique_id") == unique_id:
            customer_data.get("fsl_nominee_table").remove(entry)
            customer_data.save()
            
    frappe.local.response["message"] = {
        "success_key": 1,
    }
