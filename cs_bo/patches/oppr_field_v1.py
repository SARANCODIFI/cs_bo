import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

####################### added to new patch
def customer_customization():
    print("Updating Customization For Customer...")
    custom_fields()
    # property_setter()
 
def custom_fields():
    custom_field = {
        "Opportunity": [
            
            dict(
                fieldname = "fsl_aadhar_no",
                fieldtype = "Data",                
                label = "Aadhar Number",
                insert_after = "fsl_aadharpan_link"
            )
            
        ]
    }
    create_custom_fields(custom_field)

 