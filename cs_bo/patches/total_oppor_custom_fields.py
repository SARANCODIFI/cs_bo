import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def opp_customization():
    print("Updating Customization For Opportunity...")
    custom_fields()
    # property_setter()
 
def custom_fields():
    custom_field = {
        "Opportunity": [

            dict(
                fieldname = "fsl_stage",
                fieldtype = "Data",
                label = "Stage",
                insert_after = "status"        
            ),
            dict(
                 fieldname = "fsl_esigned_name",
                 fieldtype = "Data",
                 label = "Esigned Name",
                 insert_after = "fsl_stage"
            ),
             dict(
                fieldname = "fsl_marital_status",
                fieldtype = "Data",
                label = "Marital Status",
                insert_after = "fsl_esigned_name"
            ),
            dict(
                fieldname = "fsl_occu",
                fieldtype = "Data",
                label = "Occupation",
                insert_after = "fsl_marital_status"
            ),
             dict(
                 fieldname = "fsl_user_name",
                 fieldtype = "Data",
                 label = "User Name",
                 insert_after = "opportunity_owner"
            ),
             dict(
                 fieldname = "fsl_first_name",
                 fieldtype = "Data",
                 label = "First Name",
                 insert_after = "fsl_user_name"
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
                 fieldname = "fsl_gender",
                 fieldtype = "Link",
                 label = "Gender",
                 options = "Gender",
                 insert_after = "probability"
             ),
             dict(
                 fieldname = "fsl_dob",
                 fieldtype = "Date",
                 label = "DOB",
                 insert_after = "fsl_gender"
             ),

            dict(
                fieldname = "fsl_active_status",
                fieldtype = "Check",
                label = "Is Active",
                insert_after = "language"
            ),
            dict(
                fieldname = "fsl_assign_to",
                fieldtype = "Link",
                options="User",
                label = "Assign To",
                insert_after = "sales_stage"
            ),
            dict(
                fieldname = "fsl_assign_time",
                fieldtype = "Datetime",
                label = "Assign Time",
                insert_after = "fsl_assign_to"
            ),
            
             dict(
                 fieldname = "fsl_mobile_num",
                 fieldtype = "Data",
                 label = "Mobile Number",
                 insert_after = "job_title"
             ),
            dict(
                 fieldname = "fsl_kra_response_date",
                 fieldtype = "Date",
                 label = "Kra Response Date",
                 insert_after = "address_html"
            ),
            dict(
                fieldname = "fsl_annual_income",
                fieldtype = "Data",
                label = "Annual Income",
                insert_after = "annual_revenue"
            ),
            ## Referral
            dict(
                fieldname = "fsl_section_break_4",
                fieldtype = "Section Break",
                label = "Referral",
                insert_after = "base_opportunity_amount"
            ),
            dict(
                fieldname = "fsl_referral_by",
                fieldtype = "Data",
                label = "Referral By",
                insert_after = "fsl_section_break_4"
            ),
            dict(
                fieldname = "fsl_referral_type",
                fieldtype = "Select",
                options="\nDirect\nReferral",
                label = "Referral Type",
                insert_after = "fsl_referral_by"
            ),
            dict(
                fieldname = "fsl_referral_person_type",
                fieldtype = "Link",
                options = "DocType",
                label = "Referral Person Type",
                insert_after = "fsl_referral_person"
            ),
            dict(
                fieldname = "fsl_referral_person",
                fieldtype = "Dynamic Link",
                options = "fsl_referral_person_type",
                label = "Referral Person",
                insert_after = "fsl_referral_type"
            ),
            dict(
                fieldname = "fsl_column_break_7",
                fieldtype = "Column Break",
                label = " ",
                insert_after = "fsl_referral_person_type"
            ),
            

            dict(
                fieldname = "fsl_application_id",
                fieldtype = "Data",
                label = "Application ID",
                insert_after = "fsl_column_break_7"
            ),
            dict(
                fieldname = "fsl_mode_of_application",
                fieldtype = "Data",
                label = "Mode of Application",
                insert_after = "fsl_application_id"
            ),
            
            dict(
                fieldname = "fsl_branch",
                fieldtype = "Data",
                label = "Branch",
                insert_after = "fsl_mode_of_application"
            ),
            
            
            
            ##segment
            dict(
                 fieldname = "fsl_tab_break_1",
                 fieldtype = "Tab Break",
                 label = "Segment Details",
                 insert_after = "notes"
            ),
             dict(
                 fieldname = "fsl_category",
                 fieldtype = "Data",
                 label = "Category",
                 insert_after = "fsl_tab_break_1"
             ),
             dict(

                 fieldname = "fsl_currency_derivatives",
                 fieldtype = "Int",
                 label = "Currency Derivatives",
                 insert_after = "fsl_category"
             ),

             dict(
                 fieldname = "fsl_currency_derivatives_type",
                 fieldtype = "Data",
                 label = "Currency Derivatives Type",
                 insert_after = "fsl_currency_derivatives"
             ),
             dict(
                 fieldname = "fsl_segment_status",
                 fieldtype = "Select",
                 options="\nApproved\nRejected\nReset",
                 label = "Segment Status",
                 insert_after = "fsl_currency_derivatives_type"
             ),
             dict(
                 fieldname = "fsl_segment_remark",
                 fieldtype = "Data",
                 label = "Segment Remark",
                 insert_after = "fsl_segment_status"
             ),
             
             dict(
                 fieldname = "fsl_column_break_1",
                 fieldtype = "Column Break",
                 insert_after = "fsl_segment_remark"
             ),
              dict(
                  fieldname = "fsl_consent",
                  fieldtype = "Int",
                  label = "Consent",
                  insert_after = "fsl_column_break_1"
              ),
            dict(
                 fieldname = "fsl_Equity_derivative",
                 fieldtype = "Int",
                 label = "Equity Derivative",
                 insert_after = "fsl_consent"
             ),
            dict(
                 fieldname = "fsl_equity_cash",
                 fieldtype = "Int",
                 label = "Equity Cash",
                 insert_after = "fsl_Equity_derivative"
            ),
            dict(
                  fieldname = "fsl_mf_phy_or_dig",
                  fieldtype = "Data",
                  label = "MF PHY or DIG",
                  insert_after = "fsl_equity_cash"
            ),
            dict(
                  fieldname = "fsl_mutual_funds",
                  fieldtype = "Int",
                  label = "Mutual Funds",
                  insert_after = "fsl_mf_phy_or_dig"
            ),
            dict(
                  fieldname = "fsl_slb",
                  fieldtype = "Int",
                  label = "SLB",
                  insert_after = "fsl_mutual_funds"
            ),
            ##### Documnet Details
            dict(
                 fieldname = "fsl_tab_break_2",
                 fieldtype = "Tab Break",
                 label = "Document Details",
                 insert_after = "fsl_slb"
            ),
            dict(
                fieldname = "fsl_pan_no",
                fieldtype = "Data",
                label = "Pan Number",
                insert_after = "fsl_tab_break_2"
            ),
            
            dict(
                fieldname = "fsl_pan_status_code",
                fieldtype = "Data",
                label = "Pan Status Code",
                insert_after = "fsl_pan_no"
            ),
            dict(
                fieldname = "fsl_pan_status_code_description",
                fieldtype = "Data",
                label = "Pan Status Code Description",
                insert_after = "fsl_pan_status_code"
            ),
             dict(
                fieldname = "fsl_net_worth",
                fieldtype = "Data",
                label = "Net Worth",
                insert_after = "fsl_pan_status_code_description"
            ),
            dict(
                fieldname = "fsl_net_worth_date",
                fieldtype = "Date",
                label = "Net Worth Date",
                insert_after = "fsl_net_worth"
            ),
            dict(
                fieldname = "fsl_fatca",
                fieldtype = "Data",
                label = "Fatca",
                insert_after = "fsl_net_worth_date"
                ),
            dict(
                fieldname = "fsl_pwd",
                fieldtype = "Data",
                label = "PWD",
                insert_after = "fsl_fatca"
            ),
            #### Standing Instruction
            dict(
                 fieldname = "fsl_tab_break_3",
                 fieldtype = "Tab Break",
                 label = "Standing Instruction",
                 insert_after = "fsl_pan_status_code_description"
            ),
            
            dict(
                fieldname = "fsl_legal_action",
                fieldtype = "Data",
                label = "Legal Action",
                insert_after = "fsl_tab_break_3"
                ),
            dict(
                fieldname = "fsl_legal_action_statement",
                fieldtype = "Data",
                label = "Legal Action Statement",
                insert_after = "fsl_legal_action"
            ),
            dict(
                fieldname = "fsl_stand_ins_one",
                fieldtype = "Data",
                label = "Instruction One",
                insert_after = "fsl_legal_action_statement"
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
                fieldname = "fsl_column_break",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_standard_ins_four"
            ),
            dict(
                fieldname = "fsl_stand_ins_five",
                fieldtype = "Data",
                label = "Instruction Five",
                insert_after = "fsl_column_break"
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
            ##### Confirm
            dict(
                 fieldname = "fsl_tab_break_4",
                 fieldtype = "Tab Break",
                 label = "Confirm",
                 insert_after = "fsl_stand_ins_ten"
            ),
            dict(
                fieldname = "fsl_esigned_completed",
                fieldtype = "Check",
                label = "Esigned Completed",
                insert_after = "fsl_tab_break_4" 
            ),
            dict(
                fieldname = "fsl_pan_confirm",
                fieldtype = "Check",
                label = "Pan Confirm",
                insert_after = "fsl_esigned_completed"
            ),
            dict(
                fieldname = "fsl_sms_verified",
                fieldtype = "Check",
                label = "Sms Verified",
                insert_after = "fsl_pan_confirm"
            ),
            dict(
                fieldname = "fsl_nominee_opted_out",
                fieldtype = "Check",
                label = "Nominee Opted Out",
                insert_after = "fsl_sms_verified"
            ),
            dict(
                fieldname = "fsl_email_verified",
                fieldtype = "Check",
                label = "Email Verified",
                insert_after = "fsl_nominee_opted_out"
            ),
            dict(
                fieldname = "fsl_pdf_generated",
                fieldtype = "Check",
                label = "Pdf Generated",
                insert_after = "fsl_email_verified"
            ),
            dict(
                fieldname = "fsl_political_exposure",
                fieldtype = "Check",
                label = "Political Exposure",
                insert_after = "fsl_pdf_generated"
            ),
            
            dict(
                fieldname = "fsl_aadharpan_link",
                fieldtype = "Check",
                label = "Aadharpan Link",
                insert_after = "fsl_political_exposure"
            ),
            dict(
                fieldname = "fsl_column_break1",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_aadharpan_link"
            ),
            dict(
                fieldname = "fsl_pan_status",
                fieldtype = "Select",
                options="\nApproved\nRejected\n Reset",
                label = "Pan Status",
                insert_after = "fsl_column_break1"
            ),
            dict(
                fieldname = "fsl_pan_remark",
                fieldtype = "Data",
                label = "Pan Remark",
                insert_after = "fsl_pan_status"
            ),
            dict(
                fieldname = "fsl_sms_otp",
                fieldtype = "Data",
                label = "Sms Otp",
                insert_after = "fsl_pan_remark"
            ),
            dict(
                fieldname = "fsl_email_id",
                fieldtype = "Data",
                label = "Email Id",
                insert_after = "fsl_sms_otp"
            ),
            dict(
                fieldname = "fsl_email_otp",
                fieldtype = "Data",
                label = "Email Otp",
                insert_after = "fsl_email_id"
            ),
            dict(
                fieldname = "fsl_aadhar_no",
                fieldtype = "Data",                
                label = "Aadhar Number",
                insert_after = "fsl_email_otp"
            ),
            
            ##### Nominee Details
            dict(
                 fieldname = "fsl_tab_break_5",
                 fieldtype = "Tab Break",
                 label = "Nominee Details",
                 insert_after = "fsl_email_id"
            ),
            dict(
                fieldname = "fsl_nominee_table",
                fieldtype = "Table",
                label = "Nominee Details",
                options = "Opportunity Nominee Details",
                insert_after = "fsl_tab_break_5"
            ),
            ##### Bank Details
            dict(
                 fieldname = "fsl_tab_break_6",
                 fieldtype = "Tab Break",
                 label = "Bank Details",
                 insert_after = "fsl_nominee_table"
            ),
            dict(
                fieldname = "fsl_acc_no",
                fieldtype = "Data",
                label = "Account Number",
                insert_after = "fsl_tab_break_6"
            ),
            dict(
                fieldname = "fsl_verify_acc_number",
                fieldtype = "Data",
                label = "Verify Account Number",
                insert_after = "fsl_acc_no"
            ),
            dict(
                fieldname = "fsl_acc_hname",
                fieldtype = "Data",
                label = "Account Holder Name",
                insert_after = "fsl_verify_acc_number"
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
                fieldname = "fsl_bank_status",
                fieldtype = "Select",
                options="\nApproved\nRejected\nReset",
                label = "Bank Status",
                insert_after = "fsl_bank_pincode"
            ),
            dict(
                fieldname = "fsl_bank_remark",
                fieldtype = "Data",
                label = "Remark Status",
                insert_after = "fsl_bank_status"
            ),
             dict(
                fieldname = "fsl_column_break_2",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_bank_remark"
            ),
            dict(
                fieldname = "fsl_bank_ifsc",
                fieldtype = "Data",
                label = "Bank IFSC",
                insert_after = "fsl_column_break_2"
            ),
            dict(
                fieldname = "fsl_bank_micr",
                fieldtype = "Data",
                label = "Bank MICR",
                insert_after = "fsl_bank_ifsc"
            ),
            dict(
                fieldname = "fsl_bank_response",
                fieldtype = "Data",
                label = "Bank Response",
                insert_after = "fsl_bank_micr"
            ),
            dict(
                fieldname = "fsl_bank_branch",
                fieldtype = "Data",
                label = "Bank Branch",
                insert_after = "fsl_bank_response"
            ),
            dict(
                fieldname = "fsl_penny_response_code",
                fieldtype = "Table",
                options="Penny Drop",
                label = "Penny Json",
                insert_after = "fsl_bank_response"
            ),

            dict(
                fieldname = "fsl_bank_tnx_response",
                fieldtype = "Select",
                label = "Bank Transaction Response",
                options = "True\nFalse\nNull",
                insert_after = "fsl_penny_response_code"
            ),
            dict(
                fieldname = "fsl_penny_confirm",
                fieldtype = "Check",
                label = "Penny Confirm",
                insert_after = "fsl_bank_tnx_response"
            ),
            dict(
                fieldname = "fsl_section_break",
                fieldtype = "Section Break",                
                label = "",
                insert_after = "fsl_penny_confirm"
            ),
            dict(
                fieldname = "fsl_amount",
                fieldtype = "Int",
                label = "Amount",
                insert_after = "fsl_section_break"
            ),
            dict(
                fieldname = "fsl_amount_due",
                fieldtype = "Int",
                label = "Amount Due",
                insert_after = "fsl_amount"
            ),
            dict(
                fieldname = "fsl_amount_paid",
                fieldtype = "Int",
                label = "Amount Paid",
                insert_after = "fsl_amount_due"
            ),
            dict(
                fieldname = "fsl_attempts",
                fieldtype = "Int",
                label = "Attempts",
                insert_after = "fsl_amount_paid"
            ),
            dict(
                fieldname = "fsl_entity",
                fieldtype = "Data",
                label = "Entity",
                insert_after = "fsl_attempts"
            ),
            dict(
                fieldname = "fsl_order_id",
                fieldtype = "Int",
                label = "Order Id",
                insert_after = "fsl_entity"
            ),
            
            dict(
                fieldname = "fsl_column_break_3",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_order_id"
            ),
            dict(
                fieldname = "fsl_payment_status",
                fieldtype = "Data",
                label = "Payment Status",
                insert_after = "fsl_column_break_3"
            ),
            dict(
                fieldname = "fsl_payment_id",
                fieldtype = "Data",
                label = "Payment Id",
                insert_after = "fsl_payment_status"
            ),
            dict(
                fieldname = "fsl_razorpay_order_id",
                fieldtype = "Data",
                label = "Razorpay Order Id",
                insert_after = "fsl_payment_id"
            ),
            dict(
                fieldname = "fsl_razorpay_payment_id",
                fieldtype = "Data",
                label = "Razorpay Payment Id",
                insert_after = "fsl_razorpay_order_id"
            ),
            dict(
                fieldname = "fsl_razorpay_signature",
                fieldtype = "Data",
                label = "Razorpay Signature",
                insert_after = "fsl_razorpay_payment_id"
            ),
            dict(
                fieldname = "fsl_receipt",
                fieldtype = "Data",
                label = "Receipt",
                insert_after = "fsl_razorpay_signature"
            ),
            dict(
                fieldname = "fsl_reference_id",
                fieldtype = "Data",
                label = "Reference Id",
                insert_after = "fsl_receipt"
            ),
            dict(
                fieldname = "fsl_verify_url",
                fieldtype = "Data",
                label = "Verify Url",
                insert_after = "fsl_reference_id"
            ),
            
            
            ####### Stage Timing
            dict(
                 fieldname = "fsl_tab_break_7",
                 fieldtype = "Tab Break",
                 label = "Stage Timings",
                 insert_after = "fsl_penny_confirm"
            ),
            dict(
                fieldname = "fsl_notes",
                fieldtype = "Data",
                label = "Notes",
                insert_after = "fsl_tab_break_7"
            ),
            dict(
                fieldname = "fsl_stage_table",
                fieldtype = "Table",
                label = "Stage Timings",
                options = "Stage Timings",
                insert_after = "fsl_notes"
            ),
            # dict(
            #     fieldname = "fsl_password",
            #     fieldtype = "Data",
            #     label = "password",
            #     insert_after = "fsl_user_id"        
            # ),

        ####################### connection

                   
            # dict(
            #     fieldname = "fsl_penny_response_json",
            #     fieldtype = "Code",
            #     label = "Penny Response Json",
            #     insert_after = "fsl_bank_micr"
            # ),  
            
         ]
    }
    create_custom_fields(custom_field)

    