

from __future__ import unicode_literals
import frappe
from frappe import _

from frappe.custom.doctype.property_setter.property_setter import make_property_setter

######### Old Patch ############

def execute_address_property():
    # List of fields to hide
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

    # Clear the cache to reflect the changes
    # frappe.clear_cache(doctype="Address")
