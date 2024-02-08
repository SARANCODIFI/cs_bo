import frappe

@frappe.whitelist(allow_guest=True)
def convert_opportunity_to_customer(opportunity_name):
    try:
        
        return f"Opportunity  {opportunity_name}"
    except Exception as e:
        frappe.log_error(f"Error converting Opportunity to Customer: {e}")
        return None