import frappe

@frappe.whitelist(allow_guest=True)
def get_all_customer_data():
   
    try:
        customer_details = frappe.get_all("Customer",
            fields=["customer_name","fsl_dob","email_id","mobile_no","pan","fsl_demat_id","fsl_support_code"])
        for cus in customer_details:
            pan = ''
            customer_nm = cus.customer_name
            dob = cus.fsl_dob
            mail = cus.email_id
            phone = cus.mobile_no
            if cus.pan:
                pan = cus.pan
            demat = cus.fsl_demat_id
            support = cus.fsl_support_code
            address = frappe.get_last_doc("Address",filters={'address_title' :customer_nm,"address_type":"Billing"})
            tot_address = "{0}\n{1}\n{2}\n{3}\n{4}".format(address.address_line1,address.address_line2,address.city,address.state,address.pincode)
            frappe.response["message"] = {
                "data": {
                    "customer_name": customer_nm,
                    "fsl_dob":dob,
                    "email_id":mail,
                    "mobile_no":phone,
                    "pan":pan,
                    "fsl_demat_id": demat,
                    "fsl_support_code":support,
                    "address":tot_address
            }
            }
    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }