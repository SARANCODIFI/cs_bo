# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def employee_customization():
    print("Updating Customization For employee...")
    custom_fields()

def custom_fields():
    custom_field = {
        "Employee": [
            dict(
                fieldname = "fsl_Column_break_external",
                fieldtype = "Column Break",
                insert_after = "fsl_l2_manager",
            ),
        ]
    }
    create_custom_fields(custom_field)