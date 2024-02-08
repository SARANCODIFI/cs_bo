import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def opportunity_customization():
    print("Updating Customization For Opportunity...")
    custom_fields()
    # property_setter()
############ added to new patch

def custom_fields():
    custom_field = {
        "Opportunity": [
            
            dict(
                fieldname = "fsl_assign_to",
                fieldtype = "Link",
                options="User",
                label = "Assign To",
                insert_after = "sales_stage"
            ),
            dict(
                fieldname = "fsl_assign_time",
                fieldtype = "Time",
                label = "Assign Time",
                insert_after = "fsl_assign_to"
            )
            
        ]
    }
    create_custom_fields(custom_field)
