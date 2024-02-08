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
            dict(
                fieldname = "fsl_address_remarks",
                fieldtype = "Data",
                label = "Remarks",
                insert_after = "fsl_address_status",
            ),
            dict(
                fieldname = "fsl_digi_cur_countrycode",
                fieldtype = "Link",
                options="Country",
                label = "Digi Cur Country Code",
                insert_after = "fsl_digi_cur_country",
                
            ),
            dict(
                fieldname = "fsl_digi_per_countrycode",
                fieldtype = "Link",
                options="Country",
                label = "Digi Per Country Code",
                insert_after = "fsl_digi_per_country",
            ),
            dict(
                fieldname = "fsl_kra_countrycode",
                fieldtype = "Link",
                options="Country",
                label = "Kra Country Code",
                insert_after = "fsl_kra_country",
            ),
            dict(
                fieldname = "fsl_kra_per_countrycode",
                fieldtype = "Link",
                options="Country",
                label = "Kra Per Country Code",
                insert_after = "fsl_kra_per_country",
            ),
            dict(
                fieldname = "fsl_digi_cur_statecode",
                fieldtype = "Link",
                options="State",
                label = "Digi Cur State Code",
                insert_after = "fsl_digi_cur_state",
                
            ),
            dict(
                fieldname = "fsl_digi_per_statecode",
                fieldtype = "Link",
                options="State",
                label = "Digi Per State Code",
                insert_after = "fsl_digi_per_state",
            ),
            dict(
                fieldname = "fsl_kra_statecode",
                fieldtype = "Link",
                options="State",
                label = "Kra State Code",
                insert_after = "fsl_kra_state",
            ),
            dict(
                fieldname = "fsl_kra_per_statecode",
                fieldtype = "Link",
                options="State",
                label = "Kra Per State Code",
                insert_after = "fsl_kra_per_state",
            )
           
        ]
    }   
    create_custom_fields(custom_field) 

    