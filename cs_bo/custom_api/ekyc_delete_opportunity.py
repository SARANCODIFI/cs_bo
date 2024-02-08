# import frappe

# @frappe.whitelist()
# def ekyc_opportunity_delete(id):
#     oppor1 = frappe.get_doc("Opportunity",id)

#     try:
#         address = frappe.get_last_doc("Address",filters={'fsl_from_opportunity': id})
#         frappe.errprint(address.name)
#         frappe.delete_doc('Address', address.name)
#         # address.save()
#     except : 
#         pass
    
#     try:
#         customer_profile = frappe.get_last_doc("Customer Profile",filters={'fsl_from_opportunity': id})
#         frappe.db.delete('Customer Profile', customer_profile.name)
#         # cuRPNextAddresstomer_profile.save()
#     except :
#         pass
     
#     try :
#         ts = frappe.get_last_doc('Trading Scheme', filters={"opportunity_id": id})
#         frappe.db.delete('Customer Profile', ts.name)
#         # ts.save()
#     except :
#         pass
    
#     try :
#         documents= frappe.get_all('Document Details', filters={"opportunity_id":id})
#         for document1 in documents:
#             frappe.db.delete('Document Details', document1.name)
#             # document1.save()
#     except :
#         pass
    
#     frappe.db.delete('Opportunity', id)
#     # oppor1.save()
    
#     frappe.local.response["message"] = {
#             "success_key": 1,
#             "message":"Opportunity Successfully Deleted."     
#         }

import frappe

@frappe.whitelist()
def ekyc_opportunity_delete(id):
    try:
        # Retrieve the Opportunity document
        oppor1 = frappe.get_doc("Opportunity", id)

        # Attempt to delete associated records
        # frappe.errprint("else1")
        # Address
        try:
            customer_profile = frappe.get_last_doc("Customer Profile",filters={'fsl_from_opportunity': id})
            if customer_profile:
                frappe.delete_doc('Customer Profile', customer_profile.name)
                # frappe.errprint("else2")
                frappe.db.commit()
            else:
                frappe.errprint("else")
        except :
            pass
        
        try :
            ts = frappe.get_last_doc('Trading Scheme', filters={"opportunity_id": id})
            # frappe.errprint(ts.name)
            frappe.delete_doc('Trading Scheme', ts.name)
            # frappe.errprint(ts.name)
            frappe.db.commit()
        except :
            pass
        # frappe.errprint("else00")
        try :
            documents= frappe.get_all('Document Details', filters={"opportunity_id":id})
            for document1 in documents:
                frappe.delete_doc('Document Details', document1.name)
                frappe.db.commit()
        except :
            pass
        # frappe.errprint("else1567")
        try:
            address1 = frappe.get_all("Address",filters={"fsl_from_opportunity": id})
            for address in address1:
                frappe.delete_doc('Address', address.name)
                frappe.db.commit()
        except : 
            pass
        # Delete the Opportunity document
        # oppor1.delete()
        # frappe.errprint("else19876")
        frappe.delete_doc('Opportunity', id)
        # frappe.errprint("else1980000076")
        frappe.db.commit()
        # frappe.errprint("else1")

        # Set a success message in the response
        frappe.local.response["message"] = {
            "success_key": 1,
            "message": "Opportunity and associated records have been deleted."
        }
    except Exception as e:
        frappe.log_error("Error: Failed to delete Opportunity and associated records. Details")
