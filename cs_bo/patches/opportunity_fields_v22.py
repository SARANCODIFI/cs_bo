import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def opportunity_customization():
    print("Updating Customization For Opportunity...")
    custom_fields()
    # property_setter()

########### added to new patch

def custom_fields():
    custom_field = {
        "Opportunity": [
            
            dict(
                fieldname = "fsl_mode_of_application",
                fieldtype = "Data",
                label = "Mode of Application",
                insert_after = "fsl_referral_by"
            ),
            dict(
                fieldname = "fsl_branch",
                fieldtype = "Data",
                label = "Branch",
                insert_after = "fsl_mode_of_application"
            ),
            dict(
                fieldname = "fsl_stage13_timing",
                fieldtype = "Data",
                label = "Stage13 Time",
                insert_after = "fsl_stage"
            )
            
        ]
    }
    create_custom_fields(custom_field)



# import frappe
# from frappe.custom.doctype.property_setter.property_setter import make_property_setter

# def execute():
#     make_property_setter("Opportunity", "fsl_assign_to", "permlevel", "1", "Int")
#     make_property_setter("Opportunity", "fsl_segment_status", "permlevel", "1", "Int")
#     make_property_setter("Opportunity", "fsl_pan_status", "permlevel", "1", "Int")
#     make_property_setter("Opportunity", "fsl_bank_status", "permlevel", "1", "Int")
#     make_property_setter("Opportunity", "fsl_segment_remark", "permlevel", "1", "Int")
#     make_property_setter("Opportunity", "fsl_pan_remark", "permlevel", "1", "Int")
#     make_property_setter("Opportunity", "fsl_bank_remark", "permlevel", "1", "Int")
#     make_property_setter("Opportunity", "fsl_stage", "permlevel", "1", "Int")

    