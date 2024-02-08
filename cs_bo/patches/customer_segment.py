# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def customer_segment_customization():
    print("Updating Customization For Customer Segment...")
    custom_fields()
    # property_setter()

def custom_fields():
    custom_field = {
        "Customer": [
            dict(
                fieldname = "fsl_nsem",
                label = "NSEM",
                fieldtype = "Select",
                options = "Inactive\nActive\nDormant",
                default = "Inactive",
                insert_after = "fsl_nse"
            ), 
            dict(
                fieldname = "fsl_bsem",
                label = "BSEM",
                fieldtype = "Select",
                options = "Inactive\nActive\nDormant",
                default = "Inactive",
                insert_after = "fsl_nfo"
            ),
                            
        ]
    }
    create_custom_fields(custom_field)