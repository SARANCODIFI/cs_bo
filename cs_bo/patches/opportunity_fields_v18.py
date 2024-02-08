import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def customer_customization():
    print("Updating Customization For Customer...")
    custom_fields()
    # property_setter()
########## added to new patch

def custom_fields():
    custom_field = {
        "Opportunity": [
            
            dict(
                fieldname = "fsl_referral_by",
                fieldtype = "Link",
                options="Employee",
                label = "Referral By",
                insert_after = "fsl_reference_id"
            )
            
        ]
    }
    create_custom_fields(custom_field)

