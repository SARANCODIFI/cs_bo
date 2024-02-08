import frappe
@frappe.whitelist(allow_guest=True)
def get_customer_Bank_details(ucc):
    data = []
    try:
        customer_data = frappe.get_last_doc("Customer" , filters={"fsl_ucc_code":ucc})
        # customer_data = frappe.get_doc("Customer",customer)
        for custom in customer_data.fsl_bank_table:
            custom_dic = {}
            custom_dic["primary"] = custom.primary
            custom_dic["branch"] = custom.branch
            custom_dic["bank_name"] = custom.bank_name
            custom_dic["account_no"] = custom.account_no
            custom_dic["ifsc_code"] = custom.ifsc_code
            custom_dic["micr_code"] = custom.micr_code
            data.append(custom_dic)
             
        frappe.local.response["message"] = {
            "success_key": 1,
            "data": {
                "fsl_bank_details":data
            }        
        }
        

    except:
        frappe.response["message"] = {
            "error":"This Session User can't Access This Customer"
        } 



@frappe.whitelist(allow_guest=True)
def update_bank_details(data):
    # Parse the input data as JSON
    data = frappe.parse_json(data)
    
    # Retrieve the "bank_details" from the input data
    table = data.get("bank_details")
    
    # Find the customer document based on the "ucc_code"
    customer_data = frappe.get_last_doc("Customer", filters={'fsl_ucc_code': data.get("ucc")})
    
    if customer_data:
        # Flag to check if the account was found
        account_found = False
        
        for i in table:
            for j in customer_data.fsl_bank_table:
                if j.account_no == i["account_no"]:
                    # Update the bank details for the matching account
                    j.account = i["account_no"]
                    j.branch = i["branch"]
                    j.bank = i["bank_name"]
                    j.ifsc = i["ifsc_code"]
                    j.micr = i["micr_code"]
                    
                    # Save the changes to the customer document
                    customer_data.save()
                    
                    # Set the success response message
                    frappe.response["message"] = {
                        "Success": 1,
                        "data": {
                            "account": i["account_no"],
                            "branch": i["branch"],
                            "bank": i["bank_name"],
                            "ifsc": i["ifsc_code"],
                            "micr": i["micr_code"]
                        }
                    }
                    
                    # Set the flag to indicate the account was found
                    account_found = True
                    break  # Exit the loop since the account was found

        # Check if the account was not found
        if not account_found:
            frappe.response["message"] = {
                "Success": 0,
                "message": "This Account does not Exist"
            }
    else:
        # Customer not found
        frappe.response["message"] = {
            "Success": 0,
            "message": "Customer not found"
        }

                

@frappe.whitelist(allow_guest=True)
def create_bank_details(data):
    table = data.get("fsl_bank_details")
    method = 0

    try:
        customer_data = frappe.get_last_doc("Customer", filters={'fsl_ucc_code': data.get("ucc")})

        if not customer_data:
            frappe.response["message"] = {
                "Success": 0,
                "message": "No Customer document found for this user"
            }
        else:
            exists = None
            prime = None

            for i in table:
                for j in customer_data.fsl_bank_table:
                    if j.account_no == i["account_no"]:
                        exists = 1
                    if j.primary == 1:
                        prime = 1

                if prime:
                    if i["account_no"] == 1:
                        frappe.response["message"] = {
                            "Success": 0,
                            "message": "Already one account is the primary account"
                        }
                    else:
                        for i in table:
                            method = 1
                            create_bank(customer_data, exists, i)

                    if method == 0:
                        create_bank(customer_data, exists, i)
                else:
                    for i in table:
                        method = 1
                        create_bank(customer_data, exists, i)

                    if method == 0:
                        create_bank(customer_data, exists, i)

    except Exception as e:
        frappe.response["message"] = {
            "Success": 0,
            "message": f"An error occurred: {str(e)}"
        }


def create_bank(customer_data,exists,i):
    if exists :
            frappe.response["message"] = {
                "Success": 0,
                "message":"This Account Number Already Exists"
            } 
    else:
            if len(customer_data.fsl_bank_table)< 3:
                customer_data.append("fsl_bank_table", {
                    # "primary": i["primary"],
                    "account_no": i["account_no"],
                    "branch": i["branch"],
                    "bank_name":i["bank_name"],
                    "ifsc_code":i["ifsc_code"],
                    "micr_code":i["micr_code"]
                })
                customer_data.save()
                frappe.response["message"] = {
                    "Success": 1,
                    "data":
                    {
                        # "primary": i["primary"],
                        "account": i["account_no"],
                        "branch": i["branch"],
                        "bank":i["bank_name"],
                        "ifsc":i["ifsc_code"],
                        "micr":i["micr_code"]
                    }
            
                } 
                
                
            else:
                frappe.response["message"] = {
                    "Success": 0,
                    "message":"Maximum 3 Bank Accounts Allowed to Add"
                
                }
@frappe.whitelist(allow_guest=True)
def delete_fsl_bank_details(account_no, ucc):
    try:
        customer_data = frappe.get_last_doc("Customer", filters={'fsl_ucc_code': ucc})
        
        if customer_data:
            account_found = False
            
            for entry in customer_data.fsl_bank_table:
                if entry.account_no == account_no:
                    customer_data.fsl_bank_table.remove(entry)
                    customer_data.save()
                    account_found = True
                    break 
                
            if account_found:
                frappe.local.response["message"] = {
                    "success_key": 1,
                    "message": "Bank detail deleted successfully."
                }
            else:
                frappe.local.response["message"] = {
                    "success_key": 0,
                    "message": "Account not found in customer's bank details."
                }
        else:
            frappe.local.response["message"] = {
                "success_key": 0,
                "message": "Customer not found."
            }
    except Exception as e:
        frappe.local.response["message"] = {
            "success_key": 0,
            "message": f"An error occurred: {str(e)}"
        }
 