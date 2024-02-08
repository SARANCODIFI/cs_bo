# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def employee_customization():
    print("Updating Customization For employee...")
    custom_fields()

def custom_fields():
    custom_field = {
        "Employee": [
            dict(
                fieldname = "fsl_tab_break_external",
                fieldtype = "Tab Break",
                label = "External",
                insert_after = "old_parent",
            ),
            dict(
                fieldname = "fsl_l1_manager_code",
                fieldtype = "Data",
                label = "L1_ManagerCode",
                insert_after = "fsl_tab_break_external",
            ),
            dict(
                fieldname = "fsl_l1_manager",
                fieldtype = "Data",
                label = "L1_Manager",
                insert_after = "fsl_l1_manager_code",
            ),
            dict(
                fieldname = "fsl_l2_manager_code",
                fieldtype = "Data",
                label = "L2_Manager_Code",
                insert_after = "fsl_l1_manager",
            ),
            dict(
                fieldname = "fsl_l2_manager",
                fieldtype = "Data",
                label = "L2_Manager",
                insert_after = "fsl_l2_manager_code",
             ),
            dict(
                fieldname = "fsl_sbu",
                fieldtype = "Data",
                label = "SBU",
                insert_after = "fsl_l2_manager",
             ),
            dict(
                fieldname = "fsl_functions",
                fieldtype = "Data",
                label = "Functions",
                insert_after = "fsl_sbu",
             ),
            dict(
                fieldname = "fsl_product",
                fieldtype = "Data",
                label = "Product",
                insert_after = "fsl_functions",
             ),
            dict(
                fieldname = "fsl_sub_product",
                fieldtype = "Data",
                label = "Sub_Product",
                insert_after = "fsl_product",
             ),     
            dict(
                fieldname = "fsl_zones",
                fieldtype = "Data",
                label = "Zones",
                insert_after = "fsl_sub_product",
             ),
            dict(
                fieldname = "fsl_states",
                fieldtype = "Data",
                label = "States",
                insert_after = "fsl_zones",
             ),
            dict(
                fieldname = "fsl_regions",
                fieldtype = "Data",
                label = "Regions",
                insert_after = "fsl_states",
             ),
            dict(
                fieldname = "fsl_locations",
                fieldtype = "Data",
                label = "Locations",
                insert_after = "fsl_regions",
             ),
            dict(
                fieldname = "fsl_locations_code",
                fieldtype = "Int",
                label = "Locations_Code",
                insert_after = "fsl_locations",
             ),
            dict(
                fieldname = "fsl_business_designation",
                fieldtype = "Data",
                label = "Business_Designation",
                insert_after = "fsl_locations_code",
             ),
            dict(
                fieldname = "fsl_final_approved_lwd",
                fieldtype = "Data",
                label = "Final_Approved_LWD",
                insert_after = "fsl_business_designation",
             ),
            dict(
                fieldname = "fsl_crt_dt",
                fieldtype = "Datetime",
                label = "Crt_DT",
                insert_after = "fsl_final_approved_lwd",
             ),
            dict(
                fieldname = "fsl_upd_dt",
                fieldtype = "Datetime",
                label = "Upd_DT",
                insert_after = "fsl_crt_dt",
             ),
            dict(
                fieldname = "fsl_brid",
                fieldtype = "Data",
                label = "Brid",
                insert_after = "fsl_upd_dt",
             ),
        ]
    }   
    create_custom_fields(custom_field)