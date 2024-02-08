# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

############# addded to new patch

def lead_execute():
    print("Updating Customization For Lead...")
    custom_field = {
        "Lead": [
            dict(
                fieldname = "fsl_referral_rm",
                fieldtype = "Link",
                label = "Referral RM",
                options = "Employee",
                insert_after = "source"
            )]} 
    create_custom_fields(custom_field)