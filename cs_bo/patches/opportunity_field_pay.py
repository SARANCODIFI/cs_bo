import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

################ added to new patch
def customer_customization():
    print("Updating Customization For Opportunity...")
    custom_fields()
    # property_setter()
 
def custom_fields():
    custom_field = {
        "Opportunity": [
            
            dict(
                fieldname = "fsl_payment_status",
                fieldtype = "Data",                
                label = "Payment Status",
                insert_after = "fsl_razorpay_payment_id"
            )
            
        ]
    }