# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

############ added to new patch

def opp_customization():
    print("Updating Customization For Opportunity...")
    custom_fields()
    # property_setter()
 
def custom_fields():
    custom_field = {
        "Opportunity": [
            dict(
                fieldname = "fsl_application_id",
                fieldtype = "Data",
                label = "Application ID",
                insert_after = "fsl_sectionbreak1"
            ),
            dict(
                fieldname = "fsl_fatca",
                fieldtype = "Data",
                label = "Fatca",
                insert_after = "fsl_application_id"
            ),
            dict(
                fieldname = "fsl_legal_action",
                fieldtype = "Data",
                label = "Legal Action",
                insert_after = "fsl_fatca"
            ),
             dict(
                fieldname = "fsl_column_break1",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_legal_action"
            ),
             dict(
                fieldname = "fsl_net_worth",
                fieldtype = "Data",
                label = "Net Worth",
                insert_after = "fsl_column_break1"
            ),
            dict(
                fieldname = "fsl_net_worth_date",
                fieldtype = "Date",
                label = "Net Worth Date",
                insert_after = "fsl_net_worth"
            ),
            dict(
                fieldname = "fsl_active_status",
                fieldtype = "Check",
                label = "Is Active",
                insert_after = "fsl_net_worth_date"
            ),
            dict(
                fieldname = "fsl_sectionbreak2",
                fieldtype = "Section Break",
                label = "",
                insert_after = "fsl_active_status"
            ),
            dict(
                fieldname = "fsl_user_name",
                fieldtype = "Data",
                label = "User Name",
                insert_after = "fsl_sectionbreak2"
            ),
            dict(
                fieldname = "fsl_dob",
                fieldtype = "Date",
                label = "DOB",
                insert_after = "fsl_user_name"
            ),
            dict(
                fieldname = "fsl_first_name",
                fieldtype = "Data",
                label = "First Name",
                insert_after = "fsl_dob"
            ),
            dict(
                fieldname = "fsl_middle_name",
                fieldtype = "Data",
                label = "Middle Name",
                insert_after = "fsl_first_name"
            ),
            dict(
                fieldname = "fsl_last_name",
                fieldtype = "Data",
                label = "Last Name",
                insert_after = "fsl_middle_name"
            ),
            dict(
                fieldname = "fsl_full_name",
                fieldtype = "Data",
                label = "Full Name",
                insert_after = "fsl_last_name"
            ),
            dict(
                fieldname = "fsl_column_break2",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_full_name"
            ),
            dict(

                fieldname = "fsl_email_id",

                fieldtype = "Data",

                label = "Email Id",

                insert_after = "fsl_column_break2"

            ),

            dict(

                fieldname = "fsl_email_otp",

                fieldtype = "Data",

                label = "Email Otp",

                insert_after = "fsl_email_id"

            ),

            dict(

                fieldname = "fsl_mobile_num",

                fieldtype = "Data",

                label = "Mobile Number",

                insert_after = "fsl_email_otp"

            ),

            dict(

                fieldname = "fsl_sms_otp",

                fieldtype = "Data",

                label = "Sms Otp",

                insert_after = "fsl_mobile_num"

            ),

            dict(

                fieldname = "fsl_column_break3",

                fieldtype = "Column Break",

                label = "",

                insert_after = "fsl_sms_otp"

            ),

            dict(

                fieldname = "fsl_gender",

                fieldtype = "Link",

                label = "Gender",

                options = "Gender",

                insert_after = "fsl_column_break3"

            ),

            dict(

                fieldname = "fsl_legal_action_statement",

                fieldtype = "Data",

                label = "Legal Action Statement",

                insert_after = "fsl_gender"

            ),

            dict(

                fieldname = "fsl_marital_status",

                fieldtype = "Data",

                label = "Marital Status",

                insert_after = "fsl_legal_action_statement"

            ),

            dict(

                fieldname = "fsl_occu",

                fieldtype = "Data",

                label = "Occupation",

                insert_after = "fsl_marital_status"

            ),

            dict(

                fieldname = "fsl_annual_income",

                fieldtype = "Data",

                label = "Annual Income",

                insert_after = "fsl_occu"

            ),

            # dict(

            #     fieldname = "fsl_settle_cycle",

            #     fieldtype = "Data",

            #     label = "Settlement Cycle",

            #     insert_after = "fsl_annual_income"

            # ),

            dict(

                fieldname = "fsl_political_exposure",

                fieldtype = "Check",

                label = "Political Exposure",

                insert_after = "fsl_annual_income"

            ),

            dict(

                fieldname = "fsl_email_verified",

                fieldtype = "Check",

                label = "Email Verified",

                insert_after = "fsl_political_exposure"

            ),

            dict(

                fieldname = "fsl_sms_verified",

                fieldtype = "Check",

                label = "Sms Verified",

                insert_after = "fsl_email_verified"

            ),

            dict(

                fieldname = "fsl_tab_break1",

                fieldtype = "Tab Break",

                label = "Standing Instructions",

                insert_after = "fsl_sms_verified"

            ),

            # dict(

            #     fieldname = "fsl_stand_ins",

            #     fieldtype = "Data",

            #     label = "Standing Instructions",

            #     insert_after = "fsl_tab_break1"

            # ),

            dict(

                fieldname = "fsl_sectionbreak6",

                fieldtype = "Section Break",

                label = "",

                insert_after = "fsl_tab_break1"

            ),

            dict(

                fieldname = "fsl_stand_ins_one",

                fieldtype = "Data",

                label = "Instruction One",

                insert_after = "fsl_sectionbreak6"

            ),

            dict(

                fieldname = "fsl_standard_ins_two",

                fieldtype = "Data",

                label = "Instruction Two",

                insert_after = "fsl_stand_ins_one"

            ),

            dict(

                fieldname = "fsl_stand_ins_three",

                fieldtype = "Data",

                label = "Instruction Three",

                insert_after = "fsl_standard_ins_two"

            ),

            dict(

                fieldname = "fsl_standard_ins_four",

                fieldtype = "Data",

                label = "Instruction Four",

                insert_after = "fsl_stand_ins_three"

            ),

            dict(

                fieldname = "fsl_stand_ins_five",

                fieldtype = "Data",

                label = "Instruction Five",

                insert_after = "fsl_standard_ins_four"

            ),

            dict(

                fieldname = "fsl_standard_ins_six",

                fieldtype = "Data",

                label = "Instruction Six",

                insert_after = "fsl_stand_ins_five"

            ),

            dict(

                fieldname = "fsl_stand_ins_seven",

                fieldtype = "Data",

                label = "Instruction Seven",

                insert_after = "fsl_standard_ins_six"

            ),

            dict(

                fieldname = "fsl_standard_ins_eight",

                fieldtype = "Data",

                label = "Instruction Eight",

                insert_after = "fsl_stand_ins_seven"

            ),

            dict(

                fieldname = "fsl_stand_ins_nine",

                fieldtype = "Data",

                label = "Instruction Nine",

                insert_after = "fsl_standard_ins_eight"

            ),

            dict(

                fieldname = "fsl_stand_ins_ten",

                fieldtype = "Data",

                label = "Instructions Ten",

                insert_after = "fsl_stand_ins_nine"

            ),

            dict(

                fieldname = "fsl_document_details",

                fieldtype = "Tab Break",

                label = "Document Details",

                insert_after = "fsl_stand_ins_ten"

            ),

            dict(

                fieldname = "fsl_sectionbreak4",

                fieldtype = "Section Break",

                label = "",

                insert_after = "fsl_document_details"

            ),

            dict(

                fieldname = "fsl_aadharpan_link",

                fieldtype = "Check",

                label = "Aadharpan Link",

                insert_after = "fsl_sectionbreak4"

            ),

            dict(

                fieldname = "fsl_esigned_completed",

                fieldtype = "Check",

                label = "Esigned Completed",

                insert_after = "fsl_aadharpan_link"

            ),

            dict(

                fieldname = "fsl_esiged_name",

                fieldtype = "Data",

                label = "Esiged Name",

                insert_after = "fsl_esigned_completed"

            ),

            dict(

                fieldname = "fsl_column_break5",

                fieldtype = "Column Break",

                label = "",

                insert_after = "fsl_esiged_name"

            ),

            dict(

                fieldname = "fsl_referral_by",

                fieldtype = "Data",

                label = "Referral By",

                insert_after = "fsl_column_break5"

            ),

            dict(

                fieldname = "fsl_stage",

                fieldtype = "Data",

                label = "Stage",

                insert_after = "fsl_referral_by"

            ),

            dict(

                fieldname = "fsl_pdf_generated",

                fieldtype = "Check",

                label = "Pdf Generated",

                insert_after = "fsl_stage"

            ),

            dict(

                fieldname = "fsl_sectionbreak5",

                fieldtype = "Section Break",

                label = "",

                insert_after = "fsl_pdf_generated"

            ),

            dict(

                fieldname = "fsl_pwd",

                fieldtype = "Data",

                label = "PWD",

                insert_after = "fsl_sectionbreak5"

            ),

            dict(

                fieldname = "fsl_kra_response_date",

                fieldtype = "Date",

                label = "Kra Response Date",

                insert_after = "fsl_pwd"

            ),

            dict(

                fieldname = "fsl_column_break6",

                fieldtype = "Column Break",

                label = "",

                insert_after = "fsl_kra_response_date"

            ),

            dict(

                fieldname = "fsl_pan_confirm",

                fieldtype = "Check",

                label = "Pan Confirm",

                insert_after = "fsl_column_break6"

            ),

            dict(

                fieldname = "fsl_pan_status_code",

                fieldtype = "Data",

                label = "Pan Status Code",

                insert_after = "fsl_pan_confirm"

            ),

            dict(

                fieldname = "fsl_sectionbreak7",

                fieldtype = "Section Break",

                label = "",

                insert_after = "fsl_pan_status_code"

            ),

            # dict(

            #     fieldname = "fsl_father_name",

            #     fieldtype = "Data",

            #     label = "Father Name",

            #     insert_after = "fsl_sectionbreak7"

            # ),

            # dict(

            #     fieldname = "fsl_tax_out_india",

            #     fieldtype = "Data",

            #     label = "Tax Outside India",

            #     insert_after = "fsl_sectionbreak7"

            # ),

            dict(

                fieldname = "fsl_nominee_opted_out",

                fieldtype = "Check",

                label = "Nominee Opted Out",

                insert_after = "fsl_sectionbreak7"

            ),

            dict(

                fieldname = "fsl_column_break4",

                fieldtype = "Column Break",

                label = "",

                insert_after = "fsl_nominee_opted_out"

            ),

            # dict(

            #     fieldname = "fsl_mother_nm",

            #     fieldtype = "Data",

            #     label = "Mother Name",

            #     insert_after = "fsl_column_break4"

            # ),

            # dict(

            #     fieldname = "fsl_trading_exp",

            #     fieldtype = "Data",

            #     label = "Trading Experience",

            #     insert_after = "fsl_column_break4"

            # ),

            dict(

                fieldname = "fsl_nominee_opted_out",

                fieldtype = "Check",

                label = "Nominee Opted Out",

                insert_after = "fsl_column_break4"

            )
            
     
        ]
    }
    create_custom_fields(custom_field)