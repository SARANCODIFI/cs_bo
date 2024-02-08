import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def branch_execute():
    custom_field = {
        "Branch": [
            dict(
                fieldname = "fsl_branch_code",
                fieldtype = "Data",
                label = "Branch Code",
                insert_after = "branch"
            ),
            dict(
                fieldname = "fsl_branch_name",
                fieldtype = "Data",
                label = "Branch Name",
                insert_after = "fsl_branch_code"
            ),
            dict(
                fieldname = "fsl_branch_type",
                fieldtype = "Link",
                label = "Branch Type",
                options = "Branch Type",
                insert_after = "fsl_branch_name"
                
            ),
            dict(
                fieldname = "fsl_pan_no",
                fieldtype = "Data",
                label = "Pan No",
                insert_after = "fsl_branch_type"
            ),
            dict(
                fieldname = "fsl_column_break_external5",
                fieldtype = "Column Break",
                insert_after = "fsl_pan_no"
            ),
            
            dict(
                fieldname = "fsl_default_code",
                fieldtype = "Select",
                label = "Default Code",
                options="\nY\nN",
                insert_after = "fsl_column_break_external5"
            ),
            dict(
                fieldname = "fsl_active",
                fieldtype = "Select",
                label = "Active",
                options="\nY\nN",
                insert_after = "fsl_default_code"
            ),
            dict(
                fieldname = "fsl_open_date",
                fieldtype = "Date",
                label = "Open Date",
                insert_after = "fsl_active"
            ),
            dict(
                fieldname = "fsl_close_date",
                fieldtype = "Date",
                label = "Close Date",
                insert_after = "fsl_open_date"
            ),
            dict(
                fieldname = "fsl_section_break_external6",
                fieldtype = "Section Break",
                insert_after = "fsl_close_date"
            ),
            ###########################################
            dict(
                fieldname = "fsl_city",
                fieldtype = "Data",
                label = "City",
                insert_after = "fsl_section_break_external6"
            ),
            dict(
                fieldname = "fsl_state",
                fieldtype = "Link",
                label = "State",
                options = "State",
                insert_after = "fsl_city"
            ),
            dict(
                fieldname = "fsl_country",
                fieldtype = "Link",
                label = "Country",
                options = "Country",
                insert_after = "fsl_state"
            ),
            dict(
                fieldname = "fsl_pin_code",
                fieldtype = "Data",
                label = "Pin Code",
                insert_after = "fsl_country"
            ),
            
            dict(
                fieldname = "fsl_column_break_external7",
                fieldtype = "Column Break",
                insert_after = "fsl_pin_code"
            ),
            
            dict(
                fieldname = "fsl_service_branch",
                fieldtype = "Link",
                label = "Service Branch",
                options="Service Branch",
                insert_after = "fsl_column_break_external7"
            ),
            dict(
                fieldname = "fsl_email",
                fieldtype = "Data",
                label = "Email",
                options="email",
                insert_after = "fsl_service_branch"
                
            ),
            dict(
                fieldname = "fsl_ftp_dir",
                fieldtype = "Data",
                label = "FTP DIR",
                insert_after = "fsl_email"
            ),
            dict(
                fieldname = "fsl_section_break_external7",
                fieldtype = "Section Break",
                insert_after = "fsl_ftp_dir"
            ),
            ###########################################
            
            dict(
                fieldname = "fsl_tcl_branch_code",
                fieldtype = "Data",
                label = "TCL Branch Code",
                insert_after = "fsl_section_break_external7"
            ),
            dict(
                fieldname = "fsl_tcl_dealer_code",
                fieldtype = "Data",
                label = "TCL Dealer Code",
                insert_after = "fsl_tcl_branch_code"
            ),
            dict(
                fieldname = "fsl_tcl_ip_address",
                fieldtype = "Data",
                label = "TCL IP Address",
                insert_after = "fsl_tcl_dealer_code"
            ),
            dict(
                fieldname = "fsl_tel1",
                fieldtype = "Data",
                label = "Telephone",
                insert_after = "fsl_tcl_ip_address"
            ),
            dict(
                fieldname = "fsl_mobile_no",
                fieldtype = "Data",
                label = "Mobile No",
                options = "phone",
                insert_after = "fsl_tel1"
            ),
            dict(
                fieldname = "fsl_contact_person",
                fieldtype = "Data",
                label = "Contact Person",
                insert_after = "fsl_mobile_no"
            ),
            dict(
                fieldname = "fsl_subbranch_type",
                fieldtype = "Data",
                label = "Subbranch Type",
                insert_after = "fsl_contact_person"
            ),
            dict(
                fieldname = "fsl_column_break_external2",
                fieldtype = "Column Break",
                insert_after = "fsl_subbranch_type"
            ),
            dict(
                fieldname = "fsl_auth_sign1",
                fieldtype = "Data",
                label = "Auth Sign1",
                insert_after = "fsl_column_break_external2"
            ),
            dict(
                fieldname = "fsl_auth_sign2",
                fieldtype = "Data",
                label = "Auth Sign2",
                insert_after = "fsl_auth_sign1"
            ),
            dict(
                fieldname = "fsl_section_break_external8",
                fieldtype = "Section Break",
                insert_after = "fsl_auth_sign2"
            ),##################################################
            dict(
                fieldname = "fsl_address1",
                fieldtype = "Small Text",
                label = "Address1",
                insert_after = "fsl_section_break_external8"
            ),
            dict(
                fieldname = "fsl_address2",
                fieldtype = "Small Text",
                label = "Address2",
                insert_after = "fsl_address1"
            ),
            dict(
                fieldname = "fsl_address3",
                fieldtype = "Small Text",
                label = "Address3",
                insert_after = "fsl_address2"
            ),
            dict(
                fieldname = "fsl_column_break_external8",
                fieldtype = "Column Break",
                insert_after = "fsl_address3"
            ),
            dict(
                fieldname = "fsl_hdfc_print_location",
                fieldtype = "Data",
                label = "HDFC Print Location",
                insert_after = "fsl_column_break_external8"
            ),

            dict(
                fieldname = "fsl_uti_print_location",
                fieldtype = "Data",
                label = "UTI Print Location",
                insert_after = "fsl_hdfc_print_location"
            ),
            dict(
                fieldname = "fsl_scb_print_location",
                fieldtype = "Data",
                label = "SCB Print Location",
                insert_after = "fsl_uti_print_location"
            ),
            dict(
                fieldname = "fsl_citi_print_location",
                fieldtype = "Data",
                label = "CITI Print Location",
                insert_after = "fsl_scb_print_location"
            ),
            dict(
                fieldname = "fsl_icici_print_location",
                fieldtype = "Data",
                label = "ICICI Print Location",
                insert_after = "fsl_citi_print_location"
            ),
            dict(
                fieldname = "fsl_idbi_print_location",
                fieldtype = "Data",
                label = "IDBI Print Location",
                insert_after = "fsl_icici_print_location"
            ),
            dict(
                fieldname = "fsl_yes_bank_print_location",
                fieldtype = "Data",
                label = "YES BANK Print Location",
                insert_after = "fsl_idbi_print_location"
            ), 
            dict(
                 fieldname = "fsl_section_break_external9",
                 fieldtype = "Section Break",
                 insert_after = "fsl_yes_bank_print_location"
             ),##################################################
            
            dict(
                fieldname = "fsl_fo_front_code",
                fieldtype = "Data",
                label = "FO Front Code",
                insert_after = "fsl_section_break_external9"
            ),
            dict(
                fieldname = "fsl_cur_front_code",
                fieldtype = "Data",
                label = "CUR Front Code",
                insert_after = "fsl_fo_front_code"
            ),
            # dict(
            #     fieldname = "fsl_column_break_external4",
            #     fieldtype = "Column Break",
            #     insert_after = "fsl_cur_front_code"
            # ),
            
            dict(
                fieldname = "fsl_cap_registration_no",
                fieldtype = "Data",
                label = "CAP Registration No",
                insert_after = "fsl_cur_front_code"
            ),
            dict(
                fieldname = "fsl_region_code",
                fieldtype = "Data",
                label = "Region Code",
                insert_after = "fsl_branch_type"
            ),
            dict(
                fieldname = "fsl_region_name",
                fieldtype = "Data",
                label = "Region name",
                insert_after = "fsl_region_code"
            ),
            dict(
                fieldname = "fsl_zone",
                fieldtype = "Data",
                label = "Zone",
                insert_after = "fsl_region_name"
            ),

       ]
    } 
    create_custom_fields(custom_field)    

    make_property_setter("Branch","branch","unique","0",'Check')
