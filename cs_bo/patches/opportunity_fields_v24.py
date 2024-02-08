import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def opportunity_customization():
    print("Updating Customization For Opportunity...")
    custom_fields()
    # property_setter()
    
############## added to new Patch

def custom_fields():
    custom_field = {
        "Opportunity": [
            
            dict(
                fieldname = "fsl_penny_response_code",
                fieldtype = "Table",
                options="Penny Drop",
                label = "Penny Json",
                insert_after = "fsl_bank_response"
            ),
            dict(
                fieldname = "fsl_payment_status",
                fieldtype = "Data",                
                label = "Payment Status",
                insert_after = "fsl_razorpay_payment_id"
            ),
            dict(
                fieldname = "fsl_pan_status_code_description",
                fieldtype = "Data",
                label = "Pan Status Code Description",
                insert_after = "fsl_pan_remark"
            )
            
            
        ]
    }
    create_custom_fields(custom_field)
