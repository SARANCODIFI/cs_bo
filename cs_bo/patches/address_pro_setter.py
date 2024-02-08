from __future__ import unicode_literals
import frappe
from frappe import _

from frappe.custom.doctype.property_setter.property_setter import make_property_setter

######### Old Patch ############
def execute():
    frappe.reload_doc('contacts', 'doctype', 'address', force=True)
    oppurtunity_doctype = frappe.get_doc("DocType", "Address")
    status_field = [field for field in oppurtunity_doctype.fields if field.fieldname == 'city'][0]
    status_field.mandatory = 0
    status_field = [field for field in oppurtunity_doctype.fields if field.fieldname == 'address_line1'][0]
    status_field.mandatory = 0
    
    