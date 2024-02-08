import frappe

# Field Customization
from cs_bo.customizations.customer_dashboard import dashboard_customization





@frappe.whitelist()
def after_install():
    dashboard_customization()