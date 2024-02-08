import frappe

@frappe.whitelist()
def ekyc_update(id,kra_response_date,dob= None,pan_status_code= None,pan_status_code_description = None):
        try:
            oppor = frappe.get_doc("Opportunity",id)
    
            if kra_response_date:
                oppor.fsl_kra_response_date = kra_response_date
            if pan_status_code:
                oppor.fsl_pan_status_code = pan_status_code
            if dob:
                oppor.fsl_dob = dob
            if pan_status_code_description:
                oppor.fsl_pan_status_code_description = pan_status_code_description

                
            oppor.save()

            frappe.local.response["message"] = {
                "success_key": 1,
                "message":"Opportunity Updated",
                }
                
        except :
             frappe.local.response["message"] = {
                    "success_key": 0,
                    "message":"Opportunity Not Exists"
             }
            
@frappe.whitelist()
def generate_keys(user):
    
	"""
	generate api key and api secret

	:param user: str
	"""
	# frappe.only_for("System Manager")
 
	user_details = frappe.get_doc("User", user)
 
	api_secret = frappe.generate_hash(length=15)
	# if api key is not set generate api key
	if not user_details.api_key:
		api_key = frappe.generate_hash(length=15)
		user_details.api_key = api_key
	user_details.api_secret = api_secret
	user_details.save()

	return [api_secret,api_key]
