import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def opp_customization():
    print("Updating Customization For Opportunity...")
    custom_fields()
    # property_setter()
 
############## added to new patch
 
def custom_fields():
    custom_field = {
        "Opportunity": [
            
            dict(
                fieldname = "fsl_tab_break_2",
                fieldtype = "Tab Break",
                label = "Payment Details",
                insert_after = "fsl_slb"
            ),
            dict(
                fieldname = "fsl_amount",
                fieldtype = "Int",
                label = "Amount",
                insert_after = "fsl_tab_break_2"
            ),
            dict(
                fieldname = "fsl_amount_due",
                fieldtype = "Int",
                label = "Amount Due",
                insert_after = "fsl_amount"
            ),
            dict(
                fieldname = "fsl_amount_paid",
                fieldtype = "Int",
                label = "Amount Paid",
                insert_after = "fsl_amount_due"
            ),
            dict(
                fieldname = "fsl_attempts",
                fieldtype = "Int",
                label = "Attempts",
                insert_after = "fsl_amount_paid"
            ),
            dict(
                fieldname = "fsl_entity",
                fieldtype = "Data",
                label = "Entity",
                insert_after = "fsl_attempts"
            ),
            dict(
                fieldname = "fsl_order_id",
                fieldtype = "Int",
                label = "Order Id",
                insert_after = "fsl_entity"
            ),
            dict(
                fieldname = "fsl_column_break_2",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_order_id"
            ),
            dict(
                fieldname = "fsl_payment_id",
                fieldtype = "Data",
                label = "Payment Id",
                insert_after = "fsl_column_break_2"
            ),
            dict(
                fieldname = "fsl_razorpay_order_id",
                fieldtype = "Data",
                label = "Razorpay Order Id",
                insert_after = "fsl_payment_id"
            ),
            dict(
                fieldname = "fsl_razorpay_payment_id",
                fieldtype = "Data",
                label = "Razorpay Payment Id",
                insert_after = "fsl_razorpay_order_id"
            ),
            dict(
                fieldname = "fsl_razorpay_signature",
                fieldtype = "Data",
                label = "Razorpay Signature",
                insert_after = "fsl_razorpay_payment_id"
            ),
            dict(
                fieldname = "fsl_receipt",
                fieldtype = "Data",
                label = "Receipt",
                insert_after = "fsl_razorpay_signature"
            ),
            dict(
                fieldname = "fsl_reference_id",
                fieldtype = "Data",
                label = "Reference Id",
                insert_after = "fsl_receipt"
            ),
            dict(
                fieldname = "fsl_verify_url",
                fieldtype = "Data",
                label = "Verify Url",
                insert_after = "fsl_reference_id"
            ),
            dict(
                fieldname = "fsl_notes",
                fieldtype = "Data",
                label = "Notes",
                insert_after = "fsl_verify_url"
            )    

        ]
    }
    create_custom_fields(custom_field)