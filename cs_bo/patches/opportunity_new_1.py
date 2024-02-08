# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
################# added to new patch
def execute():
    custom_field = {
        "Opportunity": [
           
            # dict(
            #     fieldname = "fsl_pan_no",
            #     fieldtype = "Data",
            #     label = "Pan Number",
            #     insert_after = "fsl_pan_confirm"
            # ),
            dict(
                fieldname = "fsl_stage_tab",
                fieldtype = "Tab Break",
                label = "Stage Timings",
                insert_after = "fsl_equity_cash"
            ),
            dict(
                fieldname = "fsl_stage_table",
                fieldtype = "Table",
                label = "Stage Timings",
                options = "Stage Timings",
                insert_after = "fsl_stage_tab"
            ),
            
        ]
    }
    create_custom_fields(custom_field)