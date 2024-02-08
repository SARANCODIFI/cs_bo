# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def execute_address():
    make_property_setter("Address", "address_line1", "reqd", 0, "Check")
    make_property_setter("Address", "city", "reqd", 0, "Check")
    frappe.reload_doc('contacts', 'doctype', 'address', force=True)
    oppurtunity_doctype = frappe.get_doc("DocType", "Address")
    status_field = [field for field in oppurtunity_doctype.fields if field.fieldname == 'city'][0]
    status_field.mandatory = 0
    status_field = [field for field in oppurtunity_doctype.fields if field.fieldname == 'address_line1'][0]
    status_field.mandatory = 0
    
    fields_to_hide = ["address_title"]
                    #   "address_type","address_line2","address_line1",
                    #   "country","county","state","city","fax","phone","email_id",
                    #   "pincode","column_break0"]

    # Fetch and update each field from the Address doctype
    for field in fields_to_hide:
        docfield = frappe.get_doc("DocField", {"parent": "Address", "fieldname": field})
        if docfield:
            # Set the hidden property to 1 (true) to hide the field
            docfield.hidden = 0
            docfield.reqd = 0
            docfield.save()

    