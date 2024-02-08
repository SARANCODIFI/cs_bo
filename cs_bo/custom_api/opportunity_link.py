import frappe

@frappe.whitelist()
def get_oppr_details(id):
    response = {}
    
    try:
        opprs = frappe.get_last_doc('Opportunity', filters={"name": id})
        
        if opprs:
            response["opportunity_data"] = opprs
        else:
            response["error"] = "No Opportunity Detail Found"

        documents = frappe.get_all('Document Details', filters={"opportunity_id": id})
        fdocument =[]
        for document in documents:
            # frappe.errprint(document)
            fdocument.append(frappe.get_doc('Document Details', document))
        response["document_data"] = fdocument if fdocument else "No Document Details Found"

        address = frappe.get_last_doc('Address', filters={"fsl_from_opportunity": id})
        response["address_data"] = address if address else "No Address Details Found"

        profile = frappe.get_last_doc('Customer Profile', filters={"fsl_from_opportunity": id})
        response["profile_data"] = profile if profile else "No Customer Profile Found"
        
        ts = frappe.get_last_doc('Trading Scheme', filters={"opportunity_id": id})   
        response["trading_scheme"] = ts if ts else "No Trading Scheme Found"
    except Exception as e:
        response["error"] = "Error Occured"+str(e)

    frappe.local.response["message"] = response


 
    


















# import frappe

# @frappe.whitelist(allow_guest=True)
# def get_oppr_details():
#     datas = []
#     try:
#         opprs = frappe.get_all('Opportunity',fields=["name","fsl_pan_no","fsl_mobile_num","fsl_assign_to","status"])
#         for oppr in opprs:
#             # oppr = frappe.get_doc("Opportunity",oppr1.name)
#             # if oppr.fsl_esigned_completed==1:
                
#             data = {
                
#                 "time": custom_validate(oppr.name, "save")
#             }
#             datas.append(data)

#         frappe.local.response["message"] = {
#             "success_key": 1,
#             "message": "Document Details Retrieved Successfully",
#             "Data": datas,
#         }
#     except Exception as e:
#         frappe.local.response["message"] = {
#             "error": f"An error occurred: {str(e)}"
#         }
          
            
#     except:
#                 frappe.local.response["message"] = {
#                     "error": "An error occurred or Opportunity Not Found"
#                 }






# def custom_validate(docname, method):
#     doc = frappe.get_doc("Opportunity", docname)

#     if doc is None:
#         frappe.msgprint(f"Opportunity with name '{docname}' not found.")
#         return 0

#     # Check if the "fsl_stage" field has changed
#     if doc.get('__islocal'):
#         return 1

#     previous_stage = doc.get_doc_before_save().get('fsl_stage')
#     current_stage = doc.fsl_stage

#     if previous_stage != current_stage:
#         # The "fsl_stage" field has changed
#         # You can perform any additional actions here, if needed
#         # ...

#         # Get the current timestamp
#         current_time = frappe.utils.now_datetime()

#         # Return the updated stage and current time
#         return current_time

# To trigger the function with a document name, you can call it like this:
# custom_validate("YourDocumentName", "save")

# To trigger the function with a document name, you can call it like this:
# custom_validate("YourDocumentName", "save")


# import frappe

# @frappe.whitelist(allow_guest=True)
# def get_time(self,event):
#     current_time = frappe.utils.now()
#     frappe.msgprint(f"Current Date and Time: {current_time}")

#     # if email_verified:
#     oppr1 = frappe.get_doc("Opportunity",self.name)
#     if oppr1.Stage:
#         v1 = frappe.get_all("Version Doctype", filters={"Opportunity",self.name})
#         frappe.errprint(v1.stage)
#         version= frappe.get_doc(version,v1.field_name)

# import frappe

# @frappe.whitelist()
# def update_and_return_current_time(doc, method):
#     if doc.fsl_stage:
#         # Store the current time in a new variable
#         doc.current_time = frappe.utils.now()
#         doc.save()

#         # Return the current time
#         return doc.current_time

# # Attach the update_and_return_current_time function to the 'on_change' trigger of the fsl_stage field
# doc_events = {
#     "Opportunity": {
#         "on_change": {
#             "fsl_stage": "your_module.your_script.update_and_return_current_time"
#         }
#     }
# }








# import frappe

# def get_last_field_edit_time(doctype, docname, fieldname):
#     # Query the Version table to get the most recent version for the specified field
#     version_record = frappe.db.sql(
#         """
#         SELECT modified
#         FROM `tabVersion`
#         WHERE ref_doctype=%s AND docname=%s AND fieldname=%s
#         ORDER BY modified DESC
#         LIMIT 1
#         """,
#         (doctype, docname, fieldname),
#         as_dict=True
#     )

#     if version_record:
#         last_edit_time = version_record[0].get('modified')
#         return last_edit_time
#     else:
#         return None

# # Replace 'Opportunity' with your specific doctype, and 'your_fieldname' with the field you're interested in
# docname = 'your_opportunity_id'  # Replace with the specific ID of your document
# fieldname = 'your_fieldname'

# last_edit_time = get_last_field_edit_time('Opportunity', docname, fieldname)

# if last_edit_time:
#     print(f"The last edited time of '{fieldname}' in the document '{docname}' is: {last_edit_time}")
# else:
#     print(f"Field '{fieldname}' does not exist in the document '{docname}' or the document was not found.")









