import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

######################## add to new patch
def customer_customization():
    print("Updating Customization For Opportunity...")
    custom_fields()
    # property_setter()
 
def custom_fields():
    custom_field = {
        "Opportunity": [
            dict(
                fieldname = "fsl_pan_status",
                fieldtype = "Select",
                options="\nApproved\nRejected\n Reset",
                label = "PAN Status",
                insert_after = "fsl_pan_no"
            ),
            dict(
                fieldname = "fsl_bank_status",
                fieldtype = "Select",
                options="\nAproved\nRejected\nReset",
                label = "Bank Status",
                insert_after = "fsl_bank_pincode"
            ),
            dict(
                fieldname = "fsl_segment_status",
                fieldtype = "Select",
                options="\nAproved\nRejected\nReset",
                label = "Segment Status",
                insert_after = "fsl_equity_derivative"
            )
        ]
    }
    create_custom_fields(custom_field)

