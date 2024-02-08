import frappe
 
@frappe.whitelist(allow_guest=True)
def change_fsl_bank_details(data):
    # user1 = frappe.session.user
    # frappe.errprint(data.get("ucc"))
    customer_data = frappe.get_last_doc("Customer", filters={"fsl_ucc_code":data.get("ucc")})
    # frappe.errprint(customer_data.name)
    for j in customer_data.fsl_bank_table:
        if j.primary ==1:
            j.primary = 0
    for j in customer_data.fsl_bank_table:
        if j.account_no == data.get("account"):
            # frappe.errprint(j.account_no)
            j.primary = 1
            customer_data.save()
            frappe.local.response["message"] = {
                "success_key": 1,
                "message":"Successfully Primary Account Change"
            }
            break
        else:
            frappe.local.response["message"] = {
                "success_key": 0,
                "message":"Account Not Exists or No Primary Account Found"
            }
    customer_data.save()