import frappe


@frappe.whitelist()
def get_opportunity_guardian_details(name,nominee_no):
    data = []
    try:
        customer_data = frappe.get_last_doc("Opportunity",filters={'name':name}) if frappe.db.exists("Opportunity",{'name':name}) else "This Session User can't Access This Opportunity"
        if customer_data != "This Session User can't Access This Opportunity":
            for custom in customer_data.fsl_nominee_table:
            	if custom.nominee_number == nominee_no:
                    custom_dic = {}
                    custom_dic["nominee_number"] = custom.nominee_number
                    custom_dic["opportunity_id"] = customer_data.name
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