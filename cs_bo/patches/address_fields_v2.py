# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def address_customization():
    print("Updating Customization For Address...")
    custom_fields()
    # property_setter()

def custom_fields():
    custom_field = {
        "Address": [
            # dict(
            #     fieldname = "fsl_is_your_company_address",
            #     fieldtype = "Check",
            #     label = "Is Your Company Address",
            #     insert_after = "disabled"
            # ),
            # dict(
            #     fieldname = "fsl_address_status",
            #     fieldtype = "Select",
            #     label = "address_status",
            #     insert_after = "disabled",
            #     options = "\nApproved\nRejected\nReset"
            # ),
            dict(
                fieldname = "fsl_address_remarks",
                fieldtype = "Data",
                label = "Remarks",
                insert_after = "fsl_address_status",
            ),
        ]
    }   
    create_custom_fields(custom_field) 