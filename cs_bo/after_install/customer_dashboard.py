import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def dashboard_customization():
    make_property_setter("Customer","dashboard_tab","show_dashboard",0,"Check")
    custom_field = {
        "Customer": [
            dict(
                fieldname = "fsl_customer_tab",
                fieldtype = "Tab Break",
                label = "Customer",
                insert_after = "basic_info"
            )
        ]
    }
    create_custom_fields(custom_field)
    
    