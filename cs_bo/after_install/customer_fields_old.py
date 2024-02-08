import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields



def customer_customization():
    make_property_setter("Customer","gender","depends_on","","Small Text")
    make_property_setter("Customer","territory","hidden",0,"Check")
    make_property_setter("Customer","salutation","depends_on","","Small Text")
    make_property_setter("Customer","customer_group","hidden",0,"Check")
    make_property_setter("Customer","customer_group","hidden",0,"Check")
    frappe.reload_doc('Selling', 'DocType', 'Customer', force=True)
    customer_doctype = frappe.get_doc("DocType", "Customer")
    # status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_dob'][0]
    # status_field.insert_after = "customer_name"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'gender'][0]
    status_field.insert_after = "fsl_dob"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'salutation'][0]
    status_field.insert_after = "gender"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_pan_no'][0]
    status_field.insert_after = "salutation"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'customer_type'][0]
    status_field.insert_after = "fsl_pan_no"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'customer_group'][0]
    status_field.insert_after = "customer_type"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'customer_group'][0]
    status_field.insert_after = "customer_type"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_activation_status'][0]
    status_field.insert_after = "column_break0"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_ucc_code'][0]
    status_field.insert_after = "fsl_activation_status"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_ucc_category'][0]
    status_field.insert_after = "fsl_ucc_code"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_authorize_type'][0]
    status_field.insert_after = "fsl_ucc_category"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_own_code'][0]
    status_field.insert_after = "fsl_authorize_type"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'territory'][0]
    status_field.insert_after = "fsl_own_code"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_branch'][0]
    status_field.insert_after = "territory"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_branch_id'][0]
    status_field.insert_after = "fsl_branch"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_region'][0]
    status_field.insert_after = "fsl_branch_id"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_relation_code'][0]
    status_field.insert_after = "defaults_tab"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_team_leader'][0]
    status_field.insert_after = "fsl_relation_code"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'lead_name'][0]
    status_field.insert_after = "fsl_team_leader"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'opportunity_name'][0]
    status_field.insert_after = "lead_name"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'account_manager'][0]
    status_field.insert_after = "opportunity_name"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_introducer'][0]
    status_field.insert_after = "account_manager"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_ckyc_number'][0]
    status_field.insert_after = "column_break_14"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_rm'][0]
    status_field.insert_after = "fsl_ckyc_number"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_depository_participant'][0]
    status_field.insert_after = "fsl_rm"
    status_field = [field for field in customer_doctype.fields if field.fieldname == 'fsl_support_code'][0]
    status_field.insert_after = "fsl_depository_participant"
    
    # custom_field = {
    #     "Customer": [
    #         dict(
    #             fieldname = "fsl_occupation",
    #             fieldtype = "Link",
    #             label = "Occupation",
    #             options = "Occupation",
    #             insert_after = "fsl_date_of_birth"
    #         ),
    #         dict(
    #             fieldname = "fsl_branch",
    #             fieldtype = "Link",
    #             label = "Branch",
    #             options = "Barnch",
    #             insert_after = "fsl_occupation"
    #         ),
    #         dict(
    #             fieldname = "fsl_branch_id",
    #             fieldtype = "Data",
    #             label = "Branch Id",
    #             insert_after = "fsl_branch"
    #         ),
    #         dict(
    #             fieldname = "fsl_ucc_category",
    #             fieldtype = "Link",
    #             label = "UCC Category",
    #             options = "UCC Category",
    #             insert_after = "fsl_branch_id"
    #         ),
    #         dict(
    #             fieldname = "fsl_region",
    #             fieldtype = "Link",
    #             label = "Region",
    #             options = "Region",
    #             insert_after = "fsl_ucc_category"
    #         ),
    #         dict(
    #             fieldname = "fsl_rm",
    #             fieldtype = "Link",
    #             label = "Relationship Manager",
    #             options = "Employee",
    #             insert_after = "fsl_region"
    #         ),
    #         dict(
    #             fieldname = "fsl_authorize_type",
    #             fieldtype = "Select",
    #             label = "Authorize Type",
    #             options = "\nDaily\nQuarterly\nMonthly",
    #             insert_after = "fsl_rm"
    #         ),
    #         dict(
    #             fieldname = "fsl_marital_status",
    #             fieldtype = "Select",
    #             label = "Marital Status",
    #             options = "\nSingle\nMarried\nDivorced\nWidowed",
    #             insert_after = "fsl_authorize_type"
    #         ),
    #         dict(
    #             fieldname = "fsl_ckyc_number",
    #             fieldtype = "Data",
    #             label = "CKYC Number",
    #             insert_after = "fsl_marital_status"
    #         ),
    #         dict(
    #             fieldname = "fsl_bank_tab",
    #             fieldtype = "Tab Break",
    #             label = "Bank Details",
    #             insert_after = "fsl_annual_income"
    #         ),
    #         dict(
    #             fieldname = "fsl_bank_table",
    #             fieldtype = "Table",
    #             label = "Bank Details",
    #             options = "Bank Details",
    #             insert_after = "fsl_bank_tab"
    #         ),
    #         dict(
    #             fieldname = "fsl_family_tab",
    #             fieldtype = "Tab Break",
    #             label = "Family Details",
    #             insert_after = "fsl_bank_table"
    #         ),
    #         dict(
    #             fieldname = "fsl_family_table",
    #             fieldtype = "Table",
    #             label = "Family Details",
    #             options = "Family Details",
    #             insert_after = "fsl_family_tab"
    #         ),
    #         dict(
    #             fieldname = "fsl_nominee_tab",
    #             fieldtype = "Tab Break",
    #             label = "Nominee Details",
    #             insert_after = "fsl_family_table"
    #         ),
    #         dict(
    #             fieldname = "fsl_nominee_table",
    #             fieldtype = "Table",
    #             label = "Nominee Details",
    #             options = "Nominee Details",
    #             insert_after = "fsl_family_table"
    #         )
    #     ]
    # }
    # create_custom_fields(custom_field)
    