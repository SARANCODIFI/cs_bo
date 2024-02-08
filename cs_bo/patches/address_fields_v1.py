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
                fieldname = "fsl_active_status",
                fieldtype = "Int",
                label = "Active Status",
                insert_after = "pincode"
            ),
            dict(
                fieldname = "fsl_aadhaar_no",
                fieldtype = "Data",
                label = "Aadhaar No",
                insert_after = "fsl_active_status"
            ),
            dict(
                fieldname = "fsl_access_token",
                fieldtype = "Data",
                label = "Access Token",
                insert_after = "fsl_aadhaar_no"
            ),
            dict(
                fieldname = "fsl_address_confirm",
                fieldtype = "Int",
                label = "Address Confirm",
                insert_after = "fsl_access_token"
            ),
            dict(
                fieldname = "fsl_application_id",
                fieldtype = "Data",
                label = "Branch ID",
                fetch_from =  "fsl_branch.fsl_branch_code",
                insert_after = "fsl_address_confirm"
            ),
            dict(
                fieldname = "fsl_tab_break",
                fieldtype = "Tab Break",
                label = "Digi Section",
                insert_after = "links"
            ),
            dict(
                fieldname = "fsl_digi_name",
                fieldtype = "Data",
                label = "Digi Name",
                insert_after = "fsl_tab_break"
            ),
             dict(
                fieldname = "fsl_digi_dob",
                fieldtype = "Date",
                label = " Digi Dob",
                insert_after = "fsl_digi_name"
            ),
            dict(
                fieldname = "fsl_digi_gender",
                fieldtype = "Link",
                label = "Digi Gender",
                options ="Gender",
                insert_after = "fsl_digi_dob"
            ),
            dict(
                fieldname = "fsl_section_break1",
                fieldtype = "Section Break",
                label = "Digi Name",
                insert_after = "fsl_digi_gender"
            ),
            dict(
                fieldname = "fsl_digi_cur_address",
                fieldtype = "Small Text",
                label = "Digi Cur Address",
                insert_after = "fsl_section_break1"
            ),
            dict(
                fieldname = "fsl_digi_cur_countrycode",
                fieldtype = "Link",
                options="Country",
                label = "Digi Cur Country Code",
                insert_after = "fsl_digi_cur_address",
                
            ),
            dict(
                fieldname = "fsl_digi_cur_country",
                fieldtype = "Data",
                label = "Digi Cur Country",
                insert_after = "fsl_digi_cur_countrycode"
            ),
            dict(
                fieldname = "fsl_digi_cur_district",
                fieldtype = "Data",
                label = "Digi Cur district",
                insert_after = "fsl_digi_cur_country"
            ),
            dict(
                fieldname = "fsl_digi_cur_locality",
                fieldtype = "Data",
                label = "Digi Cur Locality",
                insert_after = "fsl_digi_cur_district"
            ),
            dict(
                fieldname = "fsl_digi_cur_pincode",
                fieldtype = "Data",
                label = "Digi Cur Pincode",
                insert_after = "fsl_digi_cur_locality"
            ),        
            dict(
                fieldname = "fsl_digi_cur_state",
                fieldtype = "Data",
                label = "Digi Cur State",
                insert_after = "fsl_digi_cur_pincode"
            ),
            dict(
                fieldname = "fsl_column_break1",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_digi_cur_state"
            ),
            dict(
                fieldname = "fsl_digi_per_address",
                fieldtype = "Small Text",
                label = "Digi Per Address",
                insert_after = "fsl_column_break1"
            ),
            dict(
                fieldname = "fsl_digi_per_country",
                fieldtype = "Data",
                label = "Digi Per Country",
                insert_after = "fsl_digi_per_address"
            ),
           dict(
                fieldname = "fsl_digi_per_district",
                fieldtype = "Data",
                label = "Digi Per District",
                insert_after = "fsl_digi_per_country"
            ),
            dict(
                fieldname = "fsl_digi_per_locality",
                fieldtype = "Data",
                label = "digi Per Locality",
                insert_after = "fsl_digi_per_district"
            ),
            dict(
                fieldname = "fsl_digi_per_pincode",
                fieldtype = "Data",
                label = "Digi Per Pincode",
                insert_after = "fsl_digi_per_locality"
            ),
            dict(
                fieldname = "fsl_digi_per_state",
                fieldtype = "Data",
                label = " Digi Per State",
                insert_after = "fsl_digi_per_pincode"
            ),
            dict(
                fieldname = "fsl_tab_break2",
                fieldtype = "Tab Break",
                label = "KRA Section",
                insert_after = "fsl_digi_per_state"
            ),
            dict(
                fieldname = "fsl_is_kra",
                fieldtype = "Int",
                label = "is kra",
                insert_after = "fsl_tab_break2"
            ),
            dict(
                fieldname = "fsl_is_manual",
                fieldtype = "Int",
                label = "Is Manual",
                insert_after = "fsl_is_kra"
            ),
            dict(
                fieldname = "fsl_is_digi",
                fieldtype = "Int",
                label = "Is Digi",
                insert_after = "fsl_is_manual"
            ),
            dict(
                fieldname = "fsl_section_break2",
                fieldtype = "Section Break",
                label = "",
                insert_after = "fsl_is_digi"
            ),
            dict(
                fieldname = "fsl_kra_address_1",
                fieldtype = "Small Text",
                label = "Kra Address_1",
                insert_after = "fsl_section_break2"
                ),     
            dict(
                fieldname = "fsl_kra_address_2",
                fieldtype = "Small Text",
                label = "Kra Address_2",
                insert_after = "fsl_kra_address_1"
                ), 
            dict(
                fieldname = "fsl_kra_address_3",
                fieldtype = "Small Text",
                label = "Kra Address_3",
                insert_after = "fsl_kra_address_2"
                ),
            dict(
                fieldname = "fsl_kra_city",
                fieldtype = "Data",
                label = "Kra City",
                insert_after = "fsl_kra_address_3"
            ),         
            dict(
                fieldname = "fsl_kra_country",
                fieldtype = "Data",
                label = "Kra Country",
                insert_after = "fsl_kra_city"
            ),            
            dict(
                fieldname = "fsl_column_break3",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_kra_country"
            ), 
            dict(
                fieldname = "fsl_kra_per_address_1",
                fieldtype = "Small Text",
                label = "Kra Per Address_1",
                insert_after = "fsl_column_break3"
            ),   
            dict(   
                fieldname = "fsl_kra_per_address_2",
                fieldtype = "Small Text",                
                label = "Kra Per Address_2",
                insert_after = "fsl_kra_per_address_1"
            ),
            dict(
                fieldname = "fsl_kra_per_address_3",
                label = "Kra Per Address_3",
                fieldtype = "Small Text",
                insert_after = "fsl_kra_per_address_2"
            ),
            dict(
                fieldname = "fsl_kra_per_city",
                fieldtype = "Data",
                label = "Kra Per City",
                insert_after = "fsl_kra_per_address_3"
            ),
            dict(
                fieldname = "fsl_kra_per_country",
                fieldtype = "Data",
                label = "Kra Per Country",
                insert_after = "fsl_kra_per_city"
            ),
            dict(
                fieldname = "fsl_kra_per_pin",
                fieldtype = "Int",
                label = "Kra Per Pin",
                insert_after = "fsl_kra_per_country"
            ),
            dict(
                fieldname = "fsl_kra_per_state",
                fieldtype = "Data",
                label = "Kra Per State",
                insert_after = "fsl_kra_per_pin"
            ),
            dict(
                fieldname = "fsl_column_break5",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_kra_per_state"
            ),
            dict(
                fieldname = "fsl_kra_address_proof",
                fieldtype = "Data",
                label = "Kra Address Proof",
                insert_after = "fsl_column_break5",
            ),  
             dict(
                fieldname = "fsl_kra_proof_IdNumber",
                fieldtype = "Data",
                label = "Kra Proof IdNumber",
                insert_after = "fsl_kra_address_proof"
            ),
            dict(
                fieldname = "fsl_kra_email_id",
                fieldtype = "Data",
                label = "Kra Email Id",
                insert_after = "fsl_kra_proof_IdNumber"
            ),
            dict(
                fieldname = "fsl_kra_mobile_number",
                fieldtype = "Data",
                label = "Kra Mobile Number",
                insert_after = "fsl_kra_email_id"
            ),
            dict(
                fieldname = "fsl_kra_push_needed",
                fieldtype = "Data",
                label = "Kra Push Needed",
                insert_after = "fsl_kra_mobile_number"
            ),
            dict(
                fieldname = "fsl_kra_pin",
                fieldtype = "Int",
                label = "Kra Pin",
                insert_after = "fsl_kra_push_needed"
            ),            
            dict(
                fieldname = "fsl_kra_state",
                fieldtype = "Data",
                label = "Kra State",
                insert_after = "fsl_kra_pin"
            ),
            dict(
                fieldname = "fsl_tab_break3",
                fieldtype = "Tab Break",
                label = "Connection",
                insert_after = "fsl_kra_state"
            ),
            dict(
                fieldname = "fsl_from_customer",
                fieldtype = "Link",
                label = "From Customer",
                options = "Customer",
                insert_after = "fsl_tab_break3"
            ),
            dict(
                fieldname = "fsl_from_opportunity",
                fieldtype = "Link",
                label = "From Opportunity",
                options = "Opportunity",
                insert_after = "fsl_from_customer"
            ),
            dict(
                fieldname = "fsl_from_lead",
                fieldtype = "Link",
                label = "From Lead",
                options = "Lead",
                insert_after = "fsl_from_opportunity"
            ),
            dict(
                fieldname = "fsl_address_remarks",
                fieldtype = "Data",
                label = "Remarks",
                insert_after = "fsl_address_status",
            ), 
            dict(
                fieldname = "fsl_address_remarks",
                fieldtype = "Data",
                label = "Remarks",
                insert_after = "fsl_address_status",
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