# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

##### New Patch ##########

def oppor_pro_execute():
    print("Updating Customization For oppor_pro_execute...")
    make_property_setter("Opportunity", "status", "default", "",'Small Text')
    make_property_setter("Opportunity", "status", "options", "\nDormant\nActive\nInactive\nCompleted\nIn-Progress\nPdf Generated\nApproved\nRejected\nAssigned",'Small Text')
    make_property_setter("Opportunity", "opportunity_from", "reqd", 0, "Check")
    make_property_setter("Opportunity", "party_name", "reqd", 0, "Check")
    make_property_setter("Opportunity", "naming_series", "reqd", 0, "Check")