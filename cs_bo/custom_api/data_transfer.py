from frappe import _

import frappe

@frappe.whitelist(allow_guest=True)
def put_customer_details(data):
    error = 1
    fullstatus = [] 
    try:
        customer_data = frappe.parse_json(data)
        message = "Ok"
        for customer in customer_data:
            try:
                # frappe.errprint("hello00")
                ucc_code = customer["fsl_ucc_code"]
                customer_exists = frappe.db.exists("Customer", ucc_code)

                if customer_exists:
                    update_customer(customer)
                else:
                    create_customer(customer)

            except Exception as e:
                error = 0
                message = "Not Ok"
                traceback_info = frappe.get_traceback()
                
                errors = {
                    "ucc": ucc_code,
                    "error": f"An error occurred at: {str(e)}",
                    # "traceback": traceback_info
                }
                fullstatus.append(errors)

        if error:
            # errors = {
            #         "": "Customer details processed successfully.",
            #     }
            fullstatus = "Customer details processed successfully."

       
        frappe.response["data"] = {
            "status": message,
            "message": fullstatus
        }

    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }

def update_customer(customer_data):
    ucc_code = customer_data["fsl_ucc_code"]
    existing_customer = frappe.get_doc("Customer", ucc_code)

    fields_to_update = [
        "customer_name", "fsl_own_code", "fsl_authorize_type", "customer_type",
        "customer_group", "fsl_activation_status", "fsl_gender",
        "fsl_politically_exposed_person", "fsl_sebi_action", "fsl_marital_status",
        "fsl_annual_income", "fsl_pan_card", "fsl_branch_id",
        "fsl_ucc_category", "primary_address", "mobile_no", "fsl_occupation",
        "fsl_dob", "email_id", "fsl_account_opened_on", "salutation", "territory"
    ]

    for field in fields_to_update:
        if field in customer_data:
            existing_customer.set(field, customer_data[field])

    existing_customer.save()

    return {"ucc_code": ucc_code, "status": "Successfully Updated"}

def create_customer(customer_data):
    new_customer = frappe.new_doc("Customer")

    fields_to_create = [
        "customer_name", "fsl_ucc_code", "fsl_own_code", "fsl_authorize_type", "customer_type",
        "fsl_activation_status", "fsl_gender",
        "fsl_politically_exposed_person", "fsl_sebi_action", "fsl_marital_status",
        "fsl_annual_income", "fsl_pan_card", "fsl_branch_id",
        "fsl_ucc_category", "primary_address", "mobile_no", "fsl_occupation",
        "fsl_dob", "email_id", "fsl_account_opened_on", "salutation"
    ]

    if "customer_group" not in customer_data:
        new_customer.customer_group = "Individual"
    else:
        new_customer.customer_group = customer_data["customer_group"]

    if "territory" not in customer_data:
        new_customer.territory = "All Territories"
    else:
        new_customer.territory = customer_data["territory"]

    for field in fields_to_create:
        if field in customer_data:
            new_customer.set(field, customer_data[field])

    new_customer.name = customer_data["fsl_ucc_code"]

    new_customer.insert()

    return {"ucc_code": new_customer.fsl_ucc_code, "status": "Successfully Created"}



##########################    BANK API   ############################

@frappe.whitelist(allow_guest=True)
def put_customer_bank_details(data):
    error = False
    fullstatus = []

    try:
        customer_datas = frappe.parse_json(data)
        message = "Ok"

        for customer in customer_datas:
            ucc_code = customer.get("fsl_ucc_code")

            customer_data = frappe.get_list("Customer", filters={'fsl_ucc_code': ucc_code}, fields=['name'], limit=1)

            if customer_data:
                customer_name = customer_data[0].get('name')
                customer_doc = frappe.get_doc("Customer", customer_name)

                bank_exists = any(
                    j.account_no == customer["account_no"] and j.ifsc_code == customer["ifsc_code"] for j in customer_doc.fsl_bank_table
                )

                try:
                    if bank_exists:
                        # Update existing bank details
                        for j in customer_doc.fsl_bank_table:
                            if j.account_no == customer["account_no"] and j.ifsc_code == customer["ifsc_code"]:
                                j.bank_name = customer["bank_name"]
                                j.bank_code = customer["bank_code"]
                                j.branch = customer["branch"]
                                j.account_no = customer["account_no"]
                                j.ifsc_code = customer["ifsc_code"]
                                j.micr_code = customer["micr_code"]
                                j.account_type = customer["account_type"]
                                j.bank_status = customer["bank_status"]
                                j.primary = customer["primary"]
                                customer_doc.save()
                                break
                    else:
                        # Append new bank details
                        customer_doc.append("fsl_bank_table", {
                            "bank_name": customer["bank_name"],
                            "bank_code": customer["bank_code"],
                            "branch": customer["branch"],
                            "account_no": customer["account_no"],
                            "ifsc_code": customer["ifsc_code"],
                            "micr_code": customer["micr_code"],
                            "account_type": customer["account_type"],
                            "bank_status": customer["bank_status"],
                            "primary": customer["primary"],
                        })
                        customer_doc.save()

                except Exception as e:
                    error = True
                    message = "Not Ok"
                    errors = {
                        "ucc": customer_name,
                        "error": f"An error occurred at: {str(e)}",
                    }
                    fullstatus.append(errors)
            else:
                error = True
                message = "Not Ok"
                errors = {
                    "ucc": customer.get("fsl_ucc_code"),
                    "error": "Customer not exists",
                }
                fullstatus.append(errors)

        if not error:
            fullstatus = "Customer Bank details processed successfully."

        frappe.response["data"] = {
            "status": message,
            "message": fullstatus
        }

    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }

def create_bank(customer_data,exists,i):
    if exists :
            frappe.response["message"] = {
                "Success": 0,
                "message":"This Account Number Already Exists"
            } 
    else:
            if len(customer_data.fsl_bank_table)< 5:
                for p in customer_data.fsl_bank_table:
                    if p.primary:
                        p.primary = 0
                        customer_data.save()
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
                    "message":"Maximum 5 Bank Accounts Allowed to Add"
                
                }

################## Branch Master ######################

@frappe.whitelist(allow_guest=True)
def put_branch_master(data):
    error = 1
    fullstatus = [] 
    try:
        branch_data = frappe.parse_json(data)
        message = "Ok"
        for branch in branch_data:
            try:
                b_name = branch["name"]
                branch_exists = frappe.db.exists("Branch", b_name)

                if branch_exists:
                    update_branch(branch)
                else:
                    create_branch(branch)

            except Exception as e:
                error = 0
                message = "Not Ok"
                errors = {
                    "branch_name": b_name,
                    "error": f"An error occurred at: {str(e)}"
                }
                fullstatus.append(errors)
        if error:
            fullstatus = "Branch Master details processed successfully."

       
        frappe.response["data"] = {
            "status": message,
            "message": fullstatus
        }

    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }

def update_branch(branch):
    b_name = branch["name"]
    existing_branch = frappe.get_doc("Branch", b_name)

    fields_to_update = [
        "branch", "fsl_branch_code", "fsl_default_code", "fsl_active", "fsl_service_branch",
        "fsl_email", "fsl_ftp_dir","fsl_tcl_branch_code", "fsl_tcl_dealer_code", "fsl_tcl_ip_address",
        "fsl_open_date", "fsl_close_date", "fsl_branch_type", "fsl_tel1", "fsl_mobile_no", "fsl_contact_person",
        "fsl_subbranch_type", "fsl_auth_sign1", "fsl_auth_sign2", "fsl_address1", "fsl_address2", "fsl_address3", 
        "fsl_hdfc_print_location","fsl_uti_print_location", "fsl_scb_print_location", "fsl_citi_print_location", 
        "fsl_icici_print_location", "fsl_idbi_print_location", "fsl_yes_bank_print_location", "fsl_fo_front_code", 
        "fsl_cur_front_code", "fsl_country", "fsl_state", "fsl_city", "fsl_pin_code","fsl_pan_no", "fsl_cap_registration_no", 
        "fsl_region_code", "fsl_region_name", "fsl_zone"
    ]

    for field in fields_to_update:
        if field in branch:
            existing_branch.set(field, branch[field])

    existing_branch.save()

    return {"branch_name": b_name, "status": "Successfully Updated"}

def create_branch(branch):
    new_branch = frappe.new_doc("Branch")

    fields_to_create = [
        "branch", "fsl_branch_code", "fsl_default_code", "fsl_active", "fsl_service_branch",
        "fsl_email", "fsl_ftp_dir","fsl_tcl_branch_code", "fsl_tcl_dealer_code", "fsl_tcl_ip_address",
        "fsl_open_date", "fsl_close_date", "fsl_branch_type", "fsl_tel1", "fsl_mobile_no", "fsl_contact_person",
        "fsl_subbranch_type", "fsl_auth_sign1", "fsl_auth_sign2", "fsl_address1", "fsl_address2", "fsl_address3", 
        "fsl_hdfc_print_location","fsl_uti_print_location", "fsl_scb_print_location", "fsl_citi_print_location", 
        "fsl_icici_print_location", "fsl_idbi_print_location", "fsl_yes_bank_print_location", "fsl_fo_front_code", 
        "fsl_cur_front_code", "fsl_country", "fsl_state", "fsl_city", "fsl_pin_code","fsl_pan_no", "fsl_cap_registration_no", 
        "fsl_region_code", "fsl_region_name", "fsl_zone"
    ]


    for field in fields_to_create:
        if field in branch:
            new_branch.set(field, branch[field])

    new_branch.name = branch["name"]

    new_branch.insert()

    return {"branch_name": new_branch.name, "status": "Successfully Created"}