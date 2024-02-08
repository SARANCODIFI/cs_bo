import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def customer_customization():
    print("Updating Customization For Customer...")
    custom_fields()
    # property_setter()
#################### added to new patch


def custom_fields():
    custom_field = {
        "Opportunity": [
            
            dict(
                fieldname = "fsl_bank_remark",
                fieldtype = "Data",
                label = "Remark Status",
                insert_after = "fsl_bank_status"
            ),
            dict(
                fieldname = "fsl_segment_remark",
                fieldtype = "Data",
                label = "Segment Status",
                insert_after = "fsl_segment_status"
            ),
            dict(
                fieldname = "fsl_pan_remark",
                fieldtype = "Data",
                label = "Pan Status",
                insert_after = "fsl_pan_status"
            )
        ]
    }
    create_custom_fields(custom_field)




  