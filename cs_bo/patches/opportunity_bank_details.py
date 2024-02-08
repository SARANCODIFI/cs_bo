# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

############# addded to new patch

def execute():
    print("Opportunity Bank Details Executing...")
    custom_field = {
        "Opportunity": [
            dict(
                fieldname = "fsl_tab_break2",
                fieldtype = "Tab Break",
                label = "Bank Details",
                insert_after = "fsl_application_id"
            ),
            dict(
                fieldname = "fsl_acc_no",
                fieldtype = "Data",
                label = "Account Number",
                insert_after = "fsl_tab_break2"
            ),
            dict(
                fieldname = "fsl_acc_hname",
                fieldtype = "Data",
                label = "Account Holder Name",
                insert_after = "fsl_acc_no"
            ),
            dict(
                fieldname = "fsl_bank_name",
                fieldtype = "Data",
                label = "Bank Name",
                insert_after = "fsl_acc_hname"
            ),
            dict(
                fieldname = "fsl_bank_address",
                fieldtype = "Data",
                label = "Bank Address",
                insert_after = "fsl_bank_name"
            ),
            dict(
                fieldname = "fsl_bank_pincode",
                fieldtype = "Data",
                label = "Bank Pincode",
                insert_after = "fsl_bank_address"
            ),
            dict(
                fieldname = "fsl_column_break7",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_bank_pincode"
            ),
            dict(
                fieldname = "fsl_bank_ifsc",
                fieldtype = "Data",
                label = "Bank IFSC",
                insert_after = "fsl_column_break7"
            ),
            dict(
                fieldname = "fsl_bank_micr",
                fieldtype = "Data",
                label = "Bank MICR",
                insert_after = "fsl_bank_ifsc"
            ),
            dict(
                fieldname = "fsl_bank_tnx_response",
                fieldtype = "Select",
                label = "Bank Transaction Response",
                options = "True\nFalse\nNull",
                insert_after = "fsl_bank_micr"
            ),
            dict(
                fieldname = "fsl_penny_confirm",
                fieldtype = "Check",
                label = "Penny Confirm",
                insert_after = "fsl_bank_tnx_response"
            ),
            dict(
                fieldname = "fsl_tab_break3",
                fieldtype = "Tab Break",
                label = "Nominee Details",
                insert_after = "fsl_application_id"
            ),
            dict(
                fieldname = "fsl_nominee_table",
                fieldtype = "Table",
                label = "Nominee Details",
                options = "Opportunity Nominee Details",
                insert_after = "fsl_application_id"
            ),
            dict(
                fieldname = "fsl_verify_acc_number",
                fieldtype = "Data",
                label = "Verify Account Number",
                insert_after = "fsl_acc_no"
            ),
            dict(
                fieldname = "fsl_bank_response",
                fieldtype = "Data",
                label = "Bank Response",
                insert_after = "fsl_bank_micr"
            ),
            dict(
                fieldname = "fsl_penny_response_json",
                fieldtype = "Code",
                label = "Penny Response Json",
                insert_after = "fsl_bank_micr"
            ),
        ]
    }
    create_custom_fields(custom_field)