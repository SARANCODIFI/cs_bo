from frappe import _

import frappe

@frappe.whitelist(allow_guest=True)

def get_opportunity(id):
    try:
        get_opportunity = frappe.get_all("Opportunity",
            filters={'name': id},
            fields=["fsl_active_status","fsl_legal_action_statement","fsl_annual_income","fsl_user_name","fsl_application_id","fsl_fatca","fsl_gender","fsl_legal_action","fsl_marital_status","fsl_net_worth","fsl_net_worth_date","fsl_occu","fsl_political_exposure","fsl_stand_ins_one","fsl_standard_ins_two","fsl_stand_ins_three","fsl_standard_ins_four","fsl_stand_ins_five","fsl_standard_ins_six","fsl_stand_ins_seven","fsl_standard_ins_eight","fsl_stand_ins_nine","fsl_stand_ins_ten"])

        tot_data = get_opportunity  # Use the fetched data directly

        frappe.response["message"] = {
            "Success_key" : 1,
            "data": tot_data
        }
    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"Opportunity not found : {str(e)}"
        }