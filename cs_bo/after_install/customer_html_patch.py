
import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def customer_field_customization():
    print("Updating Customization For Customer...")
    custom_fields()
    # property_setter()

def custom_fields():
    custom_field = {
        "Customer": [
            dict(
                fieldname = "fsl_dashboard1",
                fieldtype = "Tab Break",
                label = "Customer Dashboard",
                insert_after = "basic_info"
            ),
            dict(
                fieldname = "custom_activity",
                fieldtype = "HTML",
                label = "Tradebook Transaction",
                # options = "<b>Tradebook Transaction</b><div id="myCanvas" style="align-items: center;"></div>",
                insert_after = "fsl_dashboard1"
            ),
            dict(
                fieldname = "details",
                fieldtype = "HTML",
                label = "Customer Details",
                # options = "<h5><strong>Customer Details</strong></h5><br><div style="display: flex; align-items: center;"><div style="flex-grow: 1;"><div style="display: flex; font-size: 13px;"><div style="flex: 1; margin-right: 100px;"><div><p><strong style="color: navy;">Customer Name:</strong> {{doc.customer_name}}</p><p><strong style="color: navy;">UCC Code:</strong> {{doc.fsl_ucc_code}}</p><p><strong style="color: navy;">Phone:</strong> {{doc.mobile_no}}</p><p><strong style="color: navy;">Gender:</strong> {{doc.gender}}</p><p><strong style="color: navy;">Father Name:</strong> {{doc.fsl_father_name}}</p><p><strong style="color: navy;">Mother Name:</strong> {{doc.fsl_mother_name}}</p><p><strong style="color: navy;">Email ID:</strong> {{doc.email_id}}</p><p><strong style="color: navy;">Mobile Number:</strong> {{doc.mobile_no}}</p></div></div><div style="flex: 1;"><p><strong style="color: navy;">Account Status:</strong> {{doc.fsl_activation_status}}</p><p><strong style="color: navy;">PAN:</strong> {{doc.fsl_pan_card}}</p><p><strong style="color: navy;">Occupation:</strong> {{doc.fsl_occupation}}</p><p><strong style="color: navy;">Branch:</strong> {{doc.fsl_branch}}</p><p><strong style="color: navy;">Customer Type:</strong> {{doc.customer_type}}</p><p><strong style="color: navy;">Own Code:</strong> {{doc.own_code}}</p><p><strong style="color: navy;">Relationship Manager:</strong> {{doc.fsl_rm}}</p></div></div></div></div>",
                insert_after = "custom_activity"
            ),
            dict(
                fieldname = "fsl_dashboard",
                fieldtype = "Tab Break",
                label = "Customer Basic",
                insert_after = "details"
            )  
        ]
    }
    create_custom_fields(custom_field)
    
    