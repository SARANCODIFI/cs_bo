# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def execute():
    make_property_setter("Opportunity", "status", "options", "\nDormant\nActive\nInactive\nCompleted\nIn-Progress\nPdf Generated\nApproved\nRejected\nAssigned",'Small Text')