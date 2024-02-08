from frappe import _
import frappe
@frappe.whitelist(allow_guest=True)

def get_customer_and_family_details(fsl_ucc_code):

    try:
        customer_details = frappe.get_all("Customer",

            filters={"customer_name": fsl_ucc_code},
            fields=["customer_name", "fsl_relation_code", "fsl_own_code", "fsl_team_leader", "fsl_account_opened_on", "fsl_dob", "fsl_region", "fsl_branch", "fsl_rm", "fsl_branch_id", "fsl_ucc_category", "fsl_authorize_type", "fsl_depository_participant", "fsl_activation_status", "fsl_introducer", "fsl_support_code", "customer_type", "fsl_ucc_code", "fsl_father_name", "fsl_mother_name", "fsl_gender", "fsl_marital_status", "fsl_occupation", "fsl_trading_experience", "fsl_politically_exposed_person", "fsl_fund_settlement_cycle", "fsl_net_worth", "fsl_annual_income", "fsl_sebi_action", "fsl_nse", "fsl_bse", "fsl_nfo", "fsl_bfo", "fsl_cds", "fsl_bcd", "fsl_mcx", "customer_primary_contact", "customer_primary_address"]

        )
        if customer_details:
            family_details = frappe.get_all("Family Details",
                filters={"parent": fsl_ucc_code},
                fields=["customer_ucc_code", "sub_account", "h_name", "sub_account_pan", "sub_account_mobile_no", "status"]

            )
            customer_details[0]["fsl_family_table"] = family_details
            frappe.response["message"] = {
                "Success_key": "new code",
                "data": customer_details[0]
            }

        else:

            frappe.response["message"] = {
                "error": "Customer not found"
            }

    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }


@frappe.whitelist(allow_guest=True)
def put_customer_family_details(data):
    result_data = []
    table = data.get("fsl_family_table")
    for i in table:
    
        try:
            customer_data = frappe.get_last_doc("Customer",filters={'fsl_ucc_code': data.get("ucc")})    
            frappe.response["message"] = {
                     "error":data.get("ucc")
                  }
            if not customer_data:
                 frappe.response["message"] = {
                     "error":"No Customer document found for this user"
                  }
            else:
                for j in customer_data.fsl_family_details:
    
                    if j.sub_account == i["sub_account"]:
                        
                        j.sub_account_pan = i["sub_account_pan"]
                        j.h_name = i["h_name"]
                        j.sub_account_pan = i["sub_account_pan"]
                        j.sub_account_mobile_no = i["sub_account_mobile_no"]
                        j.sub_account_pan = i["sub_account_pan"]
                        j.status = i["status"]
                    
                        customer_data.save() 
                        result_data.append({
                            "sub_account": i["sub_account"],
                            "h_name": i["h_name"],
                            "sub_account_pan": i["h_nsub_account_paname"],
                            "sub_account_mobile_no": i["sub_account_mobile_no"],
                            "sub_account_pan": i["h_nsub_account_paname"],
                            "status": i["status"],
                        })  
                        
                    else:
                        frappe.response["message"] = {
                           "error":"This Account does not Exists",
                           "Id" : i["sub_account"]
                        }
        except:
             frappe.response["message"] = {
               "error":"This Session User can't Access This Customer"
             }
    frappe.response["message"] = {
        "success_key": 1,
        "data":result_data
     }



@frappe.whitelist(allow_guest=True)
def post_customer_family_details(data):
    # user1 = frappe.session.user
    table = data.get("fsl_family_details")
    data = []
    
    for i in table:
        try:
            user_per1 = frappe.db.exists("User Permission",{'user':user1,'allow':"Customer",'for_value':i["sub_account"]})
            if not user_per1:      
                user_per = frappe.new_doc("User Permission")
                user_per.user = user1
                user_per.allow = "Customer"
                user_per.for_value = i["sub_account"]
                user_per.insert()
                frappe.errprint("User Permission created")
            # try:
            customer_data = frappe.get_last_doc("Customer",filters={'fsl_ucc_code': table.fsl_ucc_code})
            
            if not customer_data:
                frappe.response["message"] = {
                "error" : f"No Customer document found for this user: {str(e)}"
        }
            else:                           
                customer_data.append("fsl_family_details", {
                    "sub_account": i["sub_account"],
                    "sub_account_pan": i["sub_account_pan"],
                    "sub_account_mobile_no": i["sub_account_mobile_no"]
                })
                data.append({
                    "sub_account": i["sub_account"],
                    "sub_account_pan": i["sub_account_pan"],
                    "sub_account_mobile_no": i["sub_account_mobile_no"]
                })
                customer_data.save()

        except Exception as e:
            frappe.response["message"] = {
                "error" : f"An error occurred while processing the request: {str(e)}"
             }
    frappe.response["message"] = {
        "success_key": 1,
        "data":data
     }


@frappe.whitelist(allow_guest=True)
def delete_customer_family_details(sub_account):
    table = data.get("fsl_family_table")
    
    customer_data = frappe.get_last_doc("Customer",filters={'fsl_ucc_code': data.get("ucc")})
    for entry in customer_data.get("fsl_family_details"):
        if entry.get("sub_account") == sub_account:
            customer_data.get("fsl_family_details").remove(entry)
            customer_data.save()
            
    frappe.local.response["message"] = {
        "success_key": 1,
    }
