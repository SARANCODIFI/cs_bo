from frappe import _
from frappe.model.meta import get_meta
import frappe

@frappe.whitelist(allow_guest = True)
def create_customers(data):
    error = 1
    fullstatus = [] 
    try:
        customer_data = frappe.parse_json(data)
        message = "Ok"
        for customer in customer_data:
            try:
                ucc_code = customer["fsl_ucc_code"]
                customer_exists = frappe.db.exists("Customer", ucc_code)

                if customer_exists:
                    message = "Not Ok"
                    error = 0
                    errors = {
                    "ucc": ucc_code,
                    "error": "This UCC Already Exists"
                    }
                    fullstatus.append(errors)
                else:
                    create_customer(customer)

            except Exception as e:
                error = 0
                message = "Not Ok"
                errors = {
                    "ucc": ucc_code,
                    "error": f"An error occurred at: {str(e)}"
                }
                fullstatus.append(errors)
        if error:
       
            fullstatus = "Opportunity Converted Into Customer Successfully."

       
        frappe.response["data"] = {
            "status": message,
            "message": fullstatus
        }

    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }


##############  New  #################

def create_customer(customer_data):

    oppr = frappe.get_doc("Opportunity", customer_data["opportunity_id"])

    new_customer = frappe.new_doc("Customer")
    new_contact = frappe.new_doc("Contact")
    
    new_contact.first_name = oppr.fsl_user_name
    new_contact.mobile_no = oppr.fsl_mobile_num
    new_contact.append("phone_nos", {
        "phone": oppr.fsl_mobile_num,
        "is_primary_mobile_no": 1
    })
    new_contact.append("email_ids", {
        "email_id": oppr.fsl_email_id,
        "is_primary": 1
    })    

    new_customer.update({
        "name": customer_data["fsl_ucc_code"],
        "title": customer_data["fsl_ucc_code"],
        "customer_group": oppr.customer_group or "Individual",
        "territory": oppr.territory or "All Territories",
        "customer_name": oppr.fsl_user_name,
        "opportunity_name": customer_data["opportunity_id"],
        "fsl_gender": oppr.fsl_gender,
        "fsl_annual_income": oppr.fsl_annual_income,
        "customer_primary_contact": oppr.fsl_user_name+"-"+customer_data["fsl_ucc_code"],
        "fsl_pan_card": oppr.fsl_pan_no,
        "fsl_branch_id": oppr.fsl_branch,
        "fsl_dob": oppr.fsl_dob,
        "lead_name":oppr.party_name,
        "gender":oppr.fsl_gender,
        "fsl_ucc_code": customer_data["fsl_ucc_code"],
        "fsl_activation_status":"Active",
        "fsl_account_opened_on":frappe.utils.today()
    })
    if oppr.fsl_nominee_table:
        nominee_list = []
        for nominee_data in oppr.fsl_nominee_table:
            guardian_fname = nominee_data.guardian_fname or ""
            guardian_lname = nominee_data.guardian_lname or ""
            guardian = guardian_fname + " " + guardian_lname

            nominee_list.append({
                "nominee_number": nominee_data.nominee_number,
                "nominee_name": nominee_data.nominee_fname + "" + nominee_data.nominee_lname,
                "date_of_birth": nominee_data.date_of_birth,
                "relationship": nominee_data.relationship,
                "percentage_allocation": nominee_data.percentage_allocation,
                "mobile_number": nominee_data.mobile_number,
                "pan": nominee_data.pan,
                "email_id": nominee_data.email_id,
                "address": nominee_data.address,
                "address_2": nominee_data.address_2,
                "city": nominee_data.city,
                "state": nominee_data.state,
                "pincode": nominee_data.pincode,
                "proof": nominee_data.proof,
                "unique_id": nominee_data.unique_id,
                "customer_ucc_code": nominee_data.customer_ucc_code,
                "guardian": guardian,
                "proof": nominee_data.proof_id,
                "guardian_relationship": nominee_data.guardian_relationship,
                "guardian_dob": nominee_data.guardian_dob,
                "guardian_pan": nominee_data.guardian_pan,
                "guardian_phone_no": nominee_data.guardian_phone_no,
                "guardian_email_id": nominee_data.guardian_email_id,
                "guardian_address1": nominee_data.guardian_address1,
                "guardian_address2": nominee_data.guardian_address2,
                "guardian_city": nominee_data.guardian_city,
                "guardian_state": nominee_data.guardian_state,
                "guardian_pincode": nominee_data.guardian_pincode,
                "guardian_proof_id": nominee_data.guardian_proof_id,
                "guardian_prooftype": nominee_data.guardian_prooftype,
                "guardian_attachment_url": nominee_data.guardian_attachment_url,
            })

        new_customer.set("fsl_nominee_table", nominee_list)

    if oppr.fsl_acc_no:
        new_customer.append("fsl_bank_table", {
            "account_no": oppr.fsl_acc_no,
            "ifsc_code": oppr.fsl_bank_ifsc,
            "micr_code": oppr.fsl_bank_micr,
            "bank_name": oppr.fsl_bank_name,
            "branch": oppr.fsl_bank_branch,
        })
    
    
    new_customer.insert(ignore_permissions=True)
    frappe.db.commit()
    new_contact.append("links", {
        "link_doctype": "Customer",
        "link_name": customer_data["fsl_ucc_code"]
    })
    new_contact.insert()