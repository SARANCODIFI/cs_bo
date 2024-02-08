from frappe import _

import frappe

@frappe.whitelist(allow_guest=True)
def get_customer_details():
    try:
        customer_details = frappe.get_list("Customer",
                                           fields=["customer_name","fsl_relation_code","fsl_own_code","fsl_team_leader","fsl_account_opened_on","fsl_dob","fsl_region","fsl_branch","fsl_rm","fsl_branch_id","fsl_ucc_category","fsl_authorize_type","fsl_depository_participant","fsl_activation_status","fsl_introducer","fsl_support_code","customer_type","fsl_ucc_code","fsl_father_name","fsl_mother_name","fsl_gender","fsl_marital_status","fsl_occupation","fsl_trading_experience","fsl_politically_exposed_person","fsl_fund_settlement_cycle","fsl_net_worth","fsl_annual_income","fsl_sebi_action","fsl_nse","fsl_bse","fsl_nfo","fsl_bfo","fsl_cds","fsl_bcd","fsl_mcx","customer_primary_contact","customer_primary_address"])

        nominee_details = []
    
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

            nominee_details.append(custom_dic)
        
        
        
        frappe.local.response["message"] = {
            "Success_key": "1",
            "data": customer_details
        }
    except Exception as e:
        frappe.local.response["message"] = {
            "error": "Customer not founds"
        }

@frappe.whitelist(allow_guest=True)
def get_filtered_customer():
    try:
        customer_details = frappe.get_list("Customer",filters={'fsl_activation_status': "Active"},
                                           fields=["customer_name","fsl_relation_code","fsl_own_code","fsl_team_leader","fsl_account_opened_on","fsl_dob","fsl_region","fsl_branch","fsl_rm","fsl_branch_id","fsl_ucc_category","fsl_authorize_type","fsl_depository_participant","fsl_activation_status","fsl_introducer","fsl_support_code","customer_type","fsl_ucc_code","fsl_father_name","fsl_mother_name","fsl_gender","fsl_marital_status","fsl_occupation","fsl_trading_experience","fsl_politically_exposed_person","fsl_fund_settlement_cycle","fsl_net_worth","fsl_annual_income","fsl_sebi_action","fsl_nse","fsl_bse","fsl_nfo","fsl_bfo","fsl_cds","fsl_bcd","fsl_mcx","customer_primary_contact","customer_primary_address"])

        frappe.local.response["message"] = {
            "Success_key": "1",
            "data": customer_details
        }
    except Exception as e:
        frappe.local.response["message"] = {
            "error": "Customer not founds"
        }




@frappe.whitelist(allow_guest=True)
def put_customer_details(data):
    try:
        data_dict = frappe.parse_json(data)

        ucc = data_dict.get('fsl_ucc_code')

        if ucc:
            customer = frappe.get_doc("Customer", filters={"fsl_ucc_code": ucc})
            if customer:
                for field, value in data_dict.items():
                    if field != "fsl_ucc_code" and field != "name":
                        customer.set(field, value)
                customer.save()
                frappe.response["message"] = {
                    "Success_key": "new code",
                    "message": f"Customer details for UCC {ucc} updated successfully"
                }
            else:
                frappe.response["message"] = {
                    "error": f"No customer found with UCC {ucc}"
                }
        else:
            frappe.response["message"] = {
                "error": "Missing 'ucc' parameter in the data"
            }
    except Exception as e:
        frappe.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }

@frappe.whitelist(allow_guest=True)
def delete_customer_details(name):
      
    customer_data = frappe.db.exists("Customer",{ "name" : name})
    
    if customer_data:
            frappe.local.response["message"] = {
                "status":"Customer deleted" ,
            }
    
    else :
         frappe.local.response["message"] = {
                "status":"Customer not found" ,
                "doc" : customer_data
            }
         