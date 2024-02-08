# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def country_customization():
    print("Updating Customization For Country...")
    custom_fields()
    # property_setter()

def custom_fields():
    custom_field = {
        "Country": [
            dict(
                fieldname = "fsl_country_code",
                fieldtype = "Data",
                label = "Country Code",
                insert_after = "code",
            ),
        ]
    }   
    create_custom_fields(custom_field) 