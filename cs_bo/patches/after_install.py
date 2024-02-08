import frappe
from cs_bo.cs_bo.patches.address_fields_v1 import address_customization
from cs_bo.cs_bo.patches.address_new_property import execute_address
from cs_bo.cs_bo.patches.country import country_customization
from cs_bo.cs_bo.patches.customer_segment import custom_fields
from cs_bo.cs_bo.patches.total_oppor_custom_fields import opp_customization
# from cs_bo.cs_bo.patches.property_setter_v1 import execute_address_property

def execute():
    address_customization() # address fields
    execute_address()  # address property
    country_customization() # country
    custom_fields() # customer
    opp_customization() #opportunity



