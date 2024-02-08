# # Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# # For license information, please see license.txt

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def customer_field_customization():
    print("Updating Customization For Customer...")
    custom_fields()
    # property_setter()

def custom_fields(): 
    custom_field = {
       "Customer": [
            dict(
                fieldname = "fsl_dashboard1",
                fieldtype = "Tab Break",
                label = "Customer Dashboard",
                insert_after = "basic_info"
            ),
            dict(
                fieldname = "custom_activity",
                fieldtype = "HTML",
                label = "Tradebook Transaction",
                # options = "<b>Tradebook Transaction</b><div id=\"myCanvas\" style=\"align-items: center;\"></div>",
                insert_after = "fsl_dashboard1"
            ),
            dict(
                fieldname = "details",
                fieldtype = "HTML",
                label = "Customer Details",
                # options = "<h5><strong>Customer Details</strong></h5><br><div style=\"display: flex; align-items: center;\"><div style=\"flex-grow: 1;\"><div style=\"display: flex; font-size: 13px;\"><div style=\"flex: 1; margin-right: 100px;\"><div><p><strong style=\"color: navy;\">Customer Name:</strong> {{doc.customer_name}}</p><p><strong style=\"color: navy;\">UCC Code:</strong> {{doc.fsl_ucc_code}}</p><p><strong style=\"color: navy;\">Phone:</strong> {{doc.mobile_no}}</p><p><strong style=\"color: navy;\">Gender:</strong> {{doc.gender}}</p><p><strong style=\"color: navy;\">Father Name:</strong> {{doc.fsl_father_name}}</p><p><strong style=\"color: navy;\">Mother Name:</strong> {{doc.fsl_mother_name}}</p><p><strong style=\"color: navy;\">Email ID:</strong> {{doc.email_id}}</p><p><strong style=\"color: navy;\">Mobile Number:</strong> {{doc.mobile_no}}</p></div></div><div style=\"flex: 1;\"><p><strong style=\"color: navy;\">Account Status:</strong> {{doc.fsl_activation_status}}</p><p><strong style=\"color: navy;\">PAN:</strong> {{doc.fsl_pan_card}}</p><p><strong style=\"color: navy;\">Occupation:</strong> {{doc.fsl_occupation}}</p><p><strong style=\"color: navy;\">Branch:</strong> {{doc.fsl_branch}}</p><p><strong style=\"color: navy;\">Customer Type:</strong> {{doc.customer_type}}</p><p><strong style=\"color: navy;\">Own Code:</strong> {{doc.own_code}}</p><p><strong style=\"color: navy;\">Relationship Manager:</strong> {{doc.fsl_rm}}</p></div></div></div></div>",
                insert_after = "custom_activity"
            ),
            dict(
                fieldname = "fsl_dashboard",
                fieldtype = "Tab Break",
                label = "Customer Basic",
                insert_after = "details"
            ), 
            dict(
                fieldname = "fsl_own_code",
                fieldtype = "Data",
                label = "Own Code",
                insert_after = "customer_group"
            ),
            dict(
                fieldname = "fsl_ucc_code",
                fieldtype = "Data",
                label = "UCC Code",
                insert_after = "fsl_own_code"
            ),
            dict(
                fieldname = "fsl_ucc_category",
                fieldtype = "Link",
                label = "UCC Category",
                options = "UCC Category",
                insert_after = "fsl_ucc_code"
            ),
            dict(
                fieldname = "fsl_branch",
                fieldtype = "Link",
                label = "Branch",
                options = "Branch",
                insert_after = "fsl_ucc_category"
            ),
            dict(
                fieldname = "fsl_branch_id",
                fieldtype = "Data",
                label = "Branch ID",
                fetch_from =  "fsl_branch.fsl_branch_code",
                insert_after = "fsl_branch"
            ),
            dict(
                fieldname = "fsl_rm",
                fieldtype = "Link",
                label = "Relationship Manager",
                options = "Employee",
                insert_after = "fsl_branch_id"
            ),           
            dict(
                fieldname = "fsl_region",
                fieldtype = "Link",
                label = "Region",
                options = "Region",
                insert_after = "fsl_rm"
            ),
            dict(
                fieldname = "fsl_rm_table",
                fieldtype = "Table",
                label = "RM Table",
                options = "RM Table",
                read_only = 1,
                insert_after = "fsl_rm"
            ),
            dict(
                fieldname = "fsl_branch_table",
                fieldtype = "Table",
                label = "Branch Table",
                options = "Branch Table",
                read_only = 1,
                insert_after = "fsl_rm_table"
            ),
            dict(
                fieldname = "fsl_account_opened_on",
                fieldtype = "Date",
                label = "Account Opened On",
                insert_after = "fsl_region"
            ),
            dict(
                fieldname = "fsl_dob",
                fieldtype = "Date",
                label = "DOB",
                insert_after = "fsl_account_opened_on"
            ), 
            dict(
                fieldname = "fsl_pan_card",
                fieldtype = "Data",
                label = "PAN",
                insert_after = "account_manager"
            ),
            dict(
                fieldname = "fsl_relation_code",
                fieldtype = "Link",
                label = "Relation Code",
                options = "Employee",
                insert_after = "fsl_pan_card"
            ),  
            dict(
                fieldname = "fsl_team_leader",
                fieldtype = "Link",
                label = "Team Leader",
                options = "Employee",
                insert_after = "fsl_relation_code"
            ),
            dict(
                fieldname = "fsl_authorize_type",
                fieldtype = "Select",
                label = "Authorize Type",
                options = "\nDaily\nQuarterly\nMonthly",
                insert_after = "fsl_team_leader"
            ),
            dict(
                fieldname = "fsl_introducer",
                fieldtype = "Data",
                label = "Introducer",
                insert_after = "fsl_authorize_type"
            ),
            dict(
                fieldname = "fsl_depository_participant",
                fieldtype = "Data",
                label = "Depository Participant",
                insert_after = "fsl_introducer"
            ),
            dict(
                fieldname = "fsl_activation_status",
                fieldtype = "Select",
                label = "Activation Status",
                options = "\nActive\nClosed\nDormant\nSuspended",
                insert_after = "fsl_depository_participant"
            ),
            dict(
                fieldname = "fsl_support_code",
                fieldtype = "Data",
                label = "Support Code",
                insert_after = "fsl_activation_status",
                read_only = "0"
            ), 
            dict(
                fieldname = "fsl_ckyc_number",
                fieldtype = "Int",
                label = "CKYC Number",
                insert_after = "default_currency"
            ), 
        ####### Basic Details            
            dict(
                fieldname = "fsl_tab1_break",
                fieldtype = "Tab Break",
                label = "Basic details",
                insert_after = "customer_details"
            ),
            dict(
                fieldname = "fsl_father_name",
                fieldtype = "Data",
                label = "Father's Name",
                insert_after = "fsl_tab1_break"
            ),
            dict(
                fieldname = "fsl_mother_name",
                fieldtype = "Data",
                label = "Mother's Name",
                insert_after = "fsl_father_name"
            ),
            dict(
                fieldname = "fsl_marital_status",
                fieldtype = "Select",
                label = "Marital Status",
                options = "\nSingle\nMarried\nOther",
                insert_after = "fsl_mother_name"
            ),
            dict(
                fieldname = "fsl_occupation",
                fieldtype = "Data",
                label = "Occupation",
                insert_after = "fsl_marital_status"
            ),
            dict(
                fieldname = "fsl_annual_income",
                fieldtype = "Select",
                label = "Annual Income",
                options = "\nBelow 1 lakh\n1-5 lakhs\n5-10 lakhs\n10-25 lakhs\nAbove 25 lakhs",
                insert_after = "fsl_occupation"
            ), 
            dict(
                fieldname = "fsl_column_break",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_annual_income"
            ),
            dict(
                fieldname = "fsl_fund_settlement_cycle",
                fieldtype = "Select",
                label = "Fund Settlement Cycle",
                options = "\nQuarterly\nMonthly",
                insert_after = "fsl_column_break"
            ),
            dict(
                fieldname = "fsl_politically_exposed_person",
                fieldtype = "Select",
                label = "Are you politically exposed person?",
                options = "\nNo\nYes",
                insert_after = "fsl_fund_settlement_cycle"
            ),
            dict(
                fieldname = "fsl_trading_experience",
                fieldtype = "Select",
                label = "Trading Experience",
                options = "\nNo experience\n0-2 years\n2-5 years\n5-10 years\n10-15 years\n more than 15 years",
                insert_after = "fsl_politically_exposed_person"
            ),
            dict(
                fieldname = "fsl_net_worth",
                fieldtype = "Currency",
                label = "Net Worth",
                insert_after = "fsl_trading_experience"
            ),
            dict(
                fieldname = "fsl_sebi_action",
                fieldtype = "Check",
                label = "SeBI Actions",
                insert_after = "fsl_net_worth"
            ),
            dict(
                fieldname = "fsl_bank_tab",
                fieldtype = "Tab Break",
                label = "Bank Details",
                insert_after = "fsl_sebi_action"
            ),
            dict(
                fieldname = "fsl_bank_table",
                fieldtype = "Table",
                label = "Bank Details",
                options = "Bank Details",
                insert_after = "fsl_bank_tab"
            ),
            dict(
                fieldname = "fsl_family_tab",
                fieldtype = "Tab Break",
                label = "Family / Nominee Details",
                insert_after = "fsl_bank_table"
            ), 
            dict(
                fieldname = "fsl_family_table",
                fieldtype = "Table",
                label = "Family Details",
                options = "Family Details",
                insert_after = "fsl_family_tab"
            ), 
            dict(
                fieldname = "fsl_nominee_table",
                fieldtype = "Table",
                label = "Nominee Details",
                options = "Nominee Details",
                insert_after = "fsl_family_table"
            ),
            dict(
                fieldname = "fsl_tab2_break",
                fieldtype = "Tab Break",
                label = "Segment Selection",
                insert_after = "fsl_nominee_table"
            ),
            dict(
                fieldname = "fsl_nse",
                label = "NSE",
                fieldtype = "Select",
                options = "Inactive\nActive\nDormant",
                default = "Inactive",
                insert_after = "fsl_tab2_break"
            ), 
            dict(
                fieldname = "fsl_nsem",
                label = "NSEM",
                fieldtype = "Select",
                options = "Inactive\nActive\nDormant",
                default = "Inactive",
                insert_after = "fsl_nse"
            ),         
            dict(
                fieldname = "fsl_bse",
                label = "BSE",
                fieldtype = "Select",
                options = "Inactive\nActive\nDormant",
                default = "Inactive",
                insert_after = "fsl_nsem"
            ),
            dict(
                fieldname = "fsl_column_bsc",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_bse"
            ),   
            dict(
                fieldname = "fsl_nfo",
                fieldtype = "Select",
                options = "Inactive\nActive\nDormant",
                default = "Inactive",                
                label = "NFO",
                insert_after = "fsl_column_bsc"
            ),
            dict(
                fieldname = "fsl_bsem",
                label = "BSEM",
                fieldtype = "Select",
                options = "Inactive\nActive\nDormant",
                default = "Inactive",
                insert_after = "fsl_nfo"
            ), 
            dict(
                fieldname = "fsl_bfo",
                label = "BFO",
                fieldtype = "Select",
                options = "Inactive\nActive\nDormant",
                default = "Inactive",
                insert_after = "fsl_bsem"
            ),
            dict(
                fieldname = "fsl_column_bfo",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_bfo"
            ),
            dict(
                fieldname = "fsl_cds",
                label = "CDS",
                fieldtype = "Select",
                options = "Inactive\nActive\nDormant",
                default = "Inactive",
                insert_after = "fsl_column_bfo"
            ),
            dict(
                fieldname = "fsl_bcd",
                label = "BCD",
                fieldtype = "Select",
                options = "Inactive\nActive\nDormant",
                default = "Inactive",
                insert_after = "fsl_cds"
            ),
            dict(
                fieldname = "fsl_mcx",
                label = "MCX",
                fieldtype = "Select",
                options = "Inactive\nActive\nDormant",
                default = "Inactive",
                insert_after = "fsl_bcd"
            ),
            dict(
                fieldname = "fsl_sectionbreak",
                fieldtype = "Section Break",
                label = "",
                insert_after = "fsl_mcx"
            )
        ]
    }
    create_custom_fields(custom_field)
#     custom_field = {
#         "Customer": [
#             dict(
#                 fieldname = "fsl_dashboard1",
#                 fieldtype = "Tab Break",
#                 label = "Customer Dashboard",
#                 insert_after = "basic_info"
#             ),
#             dict(
#                 fieldname = "custom_activity",
#                 fieldtype = "HTML",
#                 label = "Tradebook Transaction",
#                 options = "<b>Tradebook Transaction</b><div id="myCanvas" style="align-items: center;"></div>",
#                 insert_after = "fsl_dashboard1"
#             ),
#             dict(
#                 fieldname = "details",
#                 fieldtype = "HTML",
#                 label = "Customer Details",
#                 options = "<h5><strong>Customer Details</strong></h5><br><div style="display: flex; align-items: center;"><div style="flex-grow: 1;"><div style="display: flex; font-size: 13px;"><div style="flex: 1; margin-right: 100px;"><div><p><strong style="color: navy;">Customer Name:</strong> {{doc.customer_name}}</p><p><strong style="color: navy;">UCC Code:</strong> {{doc.fsl_ucc_code}}</p><p><strong style="color: navy;">Phone:</strong> {{doc.mobile_no}}</p><p><strong style="color: navy;">Gender:</strong> {{doc.gender}}</p><p><strong style="color: navy;">Father Name:</strong> {{doc.fsl_father_name}}</p><p><strong style="color: navy;">Mother Name:</strong> {{doc.fsl_mother_name}}</p><p><strong style="color: navy;">Email ID:</strong> {{doc.email_id}}</p><p><strong style="color: navy;">Mobile Number:</strong> {{doc.mobile_no}}</p></div></div><div style="flex: 1;"><p><strong style="color: navy;">Account Status:</strong> {{doc.fsl_activation_status}}</p><p><strong style="color: navy;">PAN:</strong> {{doc.fsl_pan_card}}</p><p><strong style="color: navy;">Occupation:</strong> {{doc.fsl_occupation}}</p><p><strong style="color: navy;">Branch:</strong> {{doc.fsl_branch}}</p><p><strong style="color: navy;">Customer Type:</strong> {{doc.customer_type}}</p><p><strong style="color: navy;">Own Code:</strong> {{doc.own_code}}</p><p><strong style="color: navy;">Relationship Manager:</strong> {{doc.fsl_rm}}</p></div></div></div></div>",
#                 insert_after = "custom_activity"
#             ),
#             dict(
#                 fieldname = "fsl_dashboard",
#                 fieldtype = "Tab Break",
#                 label = "Customer Basic",
#                 insert_after = "details"
#             ), 
#             dict(
#                 fieldname = "fsl_own_code",
#                 fieldtype = "Data",
#                 label = "Own Code",
#                 insert_after = "customer_group"
#             ),
#             dict(
#                 fieldname = "fsl_ucc_code",
#                 fieldtype = "Data",
#                 label = "UCC Code",
#                 insert_after = "fsl_own_code"
#             ),
#             dict(
#                 fieldname = "fsl_ucc_category",
#                 fieldtype = "Link",
#                 label = "UCC Category",
#                 options = "UCC Category",
#                 insert_after = "fsl_ucc_code"
#             ),
#             dict(
#                 fieldname = "fsl_branch",
#                 fieldtype = "Link",
#                 label = "Branch",
#                 options = "Branch",
#                 insert_after = "fsl_ucc_category"
#             ),
#             dict(
#                 fieldname = "fsl_branch_id",
#                 fieldtype = "Data",
#                 label = "Branch ID",
#                 fetch_from =  "fsl_branch.fsl_branch_code",
#                 insert_after = "fsl_branch"
#             ),
#             dict(
#                 fieldname = "fsl_rm",
#                 fieldtype = "Link",
#                 label = "Relationship Manager",
#                 options = "Employee",
#                 insert_after = "fsl_branch_id"
#             ),           
#             dict(
#                 fieldname = "fsl_region",
#                 fieldtype = "Link",
#                 label = "Region",
#                 options = "Region",
#                 insert_after = "fsl_rm"
#             ),
#             dict(
#                 fieldname = "fsl_rm_table",
#                 fieldtype = "Table",
#                 label = "RM Table",
#                 options = "RM Table",
#                 read_only = 1,
#                 insert_after = "fsl_rm"
#             ),
#             dict(
#                 fieldname = "fsl_branch_table",
#                 fieldtype = "Table",
#                 label = "Branch Table",
#                 options = "Branch Table",
#                 read_only = 1,
#                 insert_after = "fsl_rm_table"
#             ),
#             dict(
#                 fieldname = "fsl_account_opened_on",
#                 fieldtype = "Date",
#                 label = "Account Opened On",
#                 insert_after = "fsl_region"
#             ),
#             dict(
#                 fieldname = "fsl_dob",
#                 fieldtype = "Date",
#                 label = "DOB",
#                 insert_after = "fsl_account_opened_on"
#             ), 
#             dict(
#                 fieldname = "fsl_pan_card",
#                 fieldtype = "Data",
#                 label = "PAN",
#                 insert_after = "account_manager"
#             ),
#             dict(
#                 fieldname = "fsl_relation_code",
#                 fieldtype = "Link",
#                 label = "Relation Code",
#                 options = "Employee",
#                 insert_after = "fsl_pan_card"
#             ),  
#             dict(
#                 fieldname = "fsl_team_leader",
#                 fieldtype = "Link",
#                 label = "Team Leader",
#                 options = "Employee",
#                 insert_after = "fsl_relation_code"
#             ),
#             dict(
#                 fieldname = "fsl_authorize_type",
#                 fieldtype = "Select",
#                 label = "Authorize Type",
#                 options = "\nDaily\nQuarterly\nMonthly",
#                 insert_after = "fsl_team_leader"
#             ),
#             dict(
#                 fieldname = "fsl_introducer",
#                 fieldtype = "Data",
#                 label = "Introducer",
#                 insert_after = "fsl_authorize_type"
#             ),
#             dict(
#                 fieldname = "fsl_depository_participant",
#                 fieldtype = "Data",
#                 label = "Depository Participant",
#                 insert_after = "fsl_introducer"
#             ),
#             dict(
#                 fieldname = "fsl_activation_status",
#                 fieldtype = "Select",
#                 label = "Activation Status",
#                 options = "\nActive\nClosed\nDormant\nSuspended",
#                 insert_after = "fsl_depository_participant"
#             ),
#             dict(
#                 fieldname = "fsl_support_code",
#                 fieldtype = "Data",
#                 label = "Support Code",
#                 insert_after = "fsl_activation_status",
#                 read_only = "0"
#             ), 
#             dict(
#                 fieldname = "fsl_ckyc_number",
#                 fieldtype = "Int",
#                 label = "CKYC Number",
#                 insert_after = "default_currency"
#             ), 
#         ####### Basic Details            
#             dict(
#                 fieldname = "fsl_tab1_break",
#                 fieldtype = "Tab Break",
#                 label = "Basic details",
#                 insert_after = "customer_details"
#             ),
#             dict(
#                 fieldname = "fsl_father_name",
#                 fieldtype = "Data",
#                 label = "Father's Name",
#                 insert_after = "fsl_tab1_break"
#             ),
#             dict(
#                 fieldname = "fsl_mother_name",
#                 fieldtype = "Data",
#                 label = "Mother's Name",
#                 insert_after = "fsl_father_name"
#             ),
#             dict(
#                 fieldname = "fsl_marital_status",
#                 fieldtype = "Select",
#                 label = "Marital Status",
#                 options = "\nSingle\nMarried\nOther",
#                 insert_after = "fsl_mother_name"
#             ),
#             dict(
#                 fieldname = "fsl_occupation",
#                 fieldtype = "Data",
#                 label = "Occupation",
#                 insert_after = "fsl_marital_status"
#             ),
#             dict(
#                 fieldname = "fsl_annual_income",
#                 fieldtype = "Select",
#                 label = "Annual Income",
#                 options = "\nBelow 1 lakh\n1-5 lakhs\n5-10 lakhs\n10-25 lakhs\nAbove 25 lakhs",
#                 insert_after = "fsl_occupation"
#             ), 
#             dict(
#                 fieldname = "fsl_column_break",
#                 fieldtype = "Column Break",
#                 label = "",
#                 insert_after = "fsl_annual_income"
#             ),
#             dict(
#                 fieldname = "fsl_fund_settlement_cycle",
#                 fieldtype = "Select",
#                 label = "Fund Settlement Cycle",
#                 options = "\nQuarterly\nMonthly",
#                 insert_after = "fsl_column_break"
#             ),
#             dict(
#                 fieldname = "fsl_politically_exposed_person",
#                 fieldtype = "Select",
#                 label = "Are you politically exposed person?",
#                 options = "\nNo\nYes",
#                 insert_after = "fsl_fund_settlement_cycle"
#             ),
#             dict(
#                 fieldname = "fsl_trading_experience",
#                 fieldtype = "Select",
#                 label = "Trading Experience",
#                 options = "\nNo experience\n0-2 years\n2-5 years\n5-10 years\n10-15 years\n more than 15 years",
#                 insert_after = "fsl_politically_exposed_person"
#             ),
#             dict(
#                 fieldname = "fsl_net_worth",
#                 fieldtype = "Currency",
#                 label = "Net Worth",
#                 insert_after = "fsl_trading_experience"
#             ),
#             dict(
#                 fieldname = "fsl_sebi_action",
#                 fieldtype = "Check",
#                 label = "SeBI Actions",
#                 insert_after = "fsl_net_worth"
#             ),
#             dict(
#                 fieldname = "fsl_bank_tab",
#                 fieldtype = "Tab Break",
#                 label = "Bank Details",
#                 insert_after = "fsl_sebi_action"
#             ),
#             dict(
#                 fieldname = "fsl_bank_table",
#                 fieldtype = "Table",
#                 label = "Bank Details",
#                 options = "Bank Details",
#                 insert_after = "fsl_bank_tab"
#             ),
#             dict(
#                 fieldname = "fsl_family_tab",
#                 fieldtype = "Tab Break",
#                 label = "Family / Nominee Details",
#                 insert_after = "fsl_bank_table"
#             ), 
#             dict(
#                 fieldname = "fsl_family_table",
#                 fieldtype = "Table",
#                 label = "Family Details",
#                 options = "Family Details",
#                 insert_after = "fsl_family_tab"
#             ), 
#             dict(
#                 fieldname = "fsl_nominee_table",
#                 fieldtype = "Table",
#                 label = "Nominee Details",
#                 options = "Nominee Details",
#                 insert_after = "fsl_family_table"
#             ),
#             dict(
#                 fieldname = "fsl_tab2_break",
#                 fieldtype = "Tab Break",
#                 label = "Segment Selection",
#                 insert_after = "fsl_nominee_table"
#             ),
#             dict(
#                 fieldname = "fsl_nse",
#                 label = "NSE",
#                 fieldtype = "Select",
#                 options = "Inactive\nActive\nDormant",
#                 default = "Inactive",
#                 insert_after = "fsl_tab2_break"
#             ), 
#             dict(
#                 fieldname = "fsl_nsem",
#                 label = "NSEM",
#                 fieldtype = "Select",
#                 options = "Inactive\nActive\nDormant",
#                 default = "Inactive",
#                 insert_after = "fsl_nse"
#             ),         
#             dict(
#                 fieldname = "fsl_bse",
#                 label = "BSE",
#                 fieldtype = "Select",
#                 options = "Inactive\nActive\nDormant",
#                 default = "Inactive",
#                 insert_after = "fsl_nsem"
#             ),
#             dict(
#                 fieldname = "fsl_column_bsc",
#                 fieldtype = "Column Break",
#                 label = "",
#                 insert_after = "fsl_bse"
#             ),   
#             dict(
#                 fieldname = "fsl_nfo",
#                 fieldtype = "Select",
#                 options = "Inactive\nActive\nDormant",
#                 default = "Inactive",                
#                 label = "NFO",
#                 insert_after = "fsl_column_bsc"
#             ),
#             dict(
#                 fieldname = "fsl_bsem",
#                 label = "BSEM",
#                 fieldtype = "Select",
#                 options = "Inactive\nActive\nDormant",
#                 default = "Inactive",
#                 insert_after = "fsl_nfo"
#             ), 
#             dict(
#                 fieldname = "fsl_bfo",
#                 label = "BFO",
#                 fieldtype = "Select",
#                 options = "Inactive\nActive\nDormant",
#                 default = "Inactive",
#                 insert_after = "fsl_bsem"
#             ),
#             dict(
#                 fieldname = "fsl_column_bfo",
#                 fieldtype = "Column Break",
#                 label = "",
#                 insert_after = "fsl_bfo"
#             ),
#             dict(
#                 fieldname = "fsl_cds",
#                 label = "CDS",
#                 fieldtype = "Select",
#                 options = "Inactive\nActive\nDormant",
#                 default = "Inactive",
#                 insert_after = "fsl_column_bfo"
#             ),
#             dict(
#                 fieldname = "fsl_bcd",
#                 label = "BCD",
#                 fieldtype = "Select",
#                 options = "Inactive\nActive\nDormant",
#                 default = "Inactive",
#                 insert_after = "fsl_cds"
#             ),
#             dict(
#                 fieldname = "fsl_mcx",
#                 label = "MCX",
#                 fieldtype = "Select",
#                 options = "Inactive\nActive\nDormant",
#                 default = "Inactive",
#                 insert_after = "fsl_bcd"
#             ),
#             dict(
#                 fieldname = "fsl_sectionbreak",
#                 fieldtype = "Section Break",
#                 label = "",
#                 insert_after = "fsl_mcx"
#             ) 
#         ]
#     }
#     create_custom_fields(custom_field)


#     # make_property_setter("Customer","gender","depends_on","","Small Text")
#     # make_property_setter("Customer","territory","hidden",0,"Check")
#     # make_property_setter("Customer","salutation","depends_on","","Small Text")
#     # make_property_setter("Customer","customer_group","hidden",0,"Check")