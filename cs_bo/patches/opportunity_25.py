import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def opp_customization():
    print("Updating Customization For Opportunity...")
    custom_fields()
    # property_setter()
######## added to new patch
def custom_fields():
    custom_field = {
        "Opportunity": [
            dict(
                fieldname = "fsl_tab_break_1",
                fieldtype = "Tab Break",
                label = "Segment Details",
                insert_after = "notes"
            ),
            # dict(
            #     fieldname = "fsl_application_id",
            #     fieldtype = "Float",
            #     label = "Application ID",
            #     insert_after = "fsl_tab_break_1"
            # ),
            dict(
                fieldname = "fsl_category",
                fieldtype = "Data",
                label = "Category",
                insert_after = "fsl_tab_break_1"
            ),
            dict(

                fieldname = "fsl_currency_derivatives",
                fieldtype = "Int",
                label = "Currency Derivatives",
                insert_after = "fsl_category"
            ),

            dict(
                fieldname = "fsl_currency_derivatives_type",
                fieldtype = "Data",
                label = "Currency Derivatives Type",
                insert_after = "fsl_currency_derivatives"
            ),
            dict(
                fieldname = "fsl_column_break_1",
                fieldtype = "Column Break",
                label = "",
                insert_after = "fsl_currency_derivatives_type"
            ),
            dict(
                fieldname = "fsl_consent",
                fieldtype = "Int",
                label = "Consent",
                insert_after = "fsl_consent"
            ),
            dict(
                fieldname = "fsl_Equity_derivative",
                fieldtype = "Int",
                label = "Equity Derivative",
                insert_after = "fsl_currency_derivatives_type"
            ),
            dict(
                fieldname = "fsl_equity_cash",
                fieldtype = "Int",
                label = "Equity Cash",
                insert_after = "fsl_Equity_derivative"
            ),
            dict(
                fieldname = "fsl_mf_phy_or_dig",
                fieldtype = "Data",
                label = "MF PHY or DIG",
                insert_after = "fsl_equity_cash"
            ),
            dict(
                fieldname = "fsl_mutual_funds",
                fieldtype = "Int",
                label = "Mutual Funds",
                insert_after = "fsl_mf_phy_or_dig"
            ),
            dict(
                fieldname = "fsl_slb",
                fieldtype = "Int",
                label = "SLB",
                insert_after = "fsl_mutual_funds"
            )

        ]
    }
    create_custom_fields(custom_field)