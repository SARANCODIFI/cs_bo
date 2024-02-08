import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def opportunity_customization():
    print("Updating Customization For Opportunity...")
    custom_fields()
    # property_setter()

########## added to new patch

def custom_fields():
    custom_field = {
        "Opportunity": [
            
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
                insert_after = "fsl_referral_type"
            ),
            # Replaced by fsl_referral_by
            
            # dict(
            #     fieldname = "fsl_referral_person",
            #     fieldtype = "Dynamic Link",
            #     options = "fsl_referral_person_type",
            #     label = "Referral Person",
            #     insert_after = "fsl_referral_person_type"
            # ),
        ]
    }
    create_custom_fields(custom_field)

