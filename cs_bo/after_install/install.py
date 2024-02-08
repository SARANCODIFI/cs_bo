import frappe
from cs_bo.patches.address_fields_v1 import address_customization
from cs_bo.patches.address_new_property import execute_address
from cs_bo.patches.country import country_customization
from cs_bo.patches.customer_segment import custom_fields
from cs_bo.patches.total_oppor_custom_fields import opp_customization
from cs_bo.after_install.customer_dashboard import dashboard_customization
from cs_bo.patches.branch import branch_execute
from cs_bo.after_install.add_customer_fields import customer_field_customization
from cs_bo.patches.employee import employee_customization
from cs_bo.patches.lead_fields import lead_execute
from cs_bo.patches.opportunity_new1_property import oppor_pro_execute

@frappe.whitelist()
def after_install():
    address_customization() # address fields
    execute_address()  # address property
    country_customization() # country
    branch_execute() # Branch
    opp_customization() #opportunity
    dashboard_customization() #customer dashboard
    # customer_customization() # customer property setter
    customer_field_customization() # customer field custom
    employee_customization() #employee
    lead_execute() #Lead
    oppor_pro_execute()