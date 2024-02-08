import frappe

@frappe.whitelist(allow_guest=True)
def get_document_details_status(id):
      
    try:
        document_details = frappe.get_list("Document Details", filters={"opportunity_id": id})
        data_list=[]
        for document in document_details:
            name=document.name
            doc =frappe.get_doc("Document Details",name)

            data={}

            document_type= doc.document_type
            status=doc.status
            remarks=doc.document_remarks
            
            data["Document Type"]=document_type
            data["status"]=status
            data["remarks"]=remarks
            data_list.append(data)

        
        frappe.local.response["message"] = {
                "success_key": 1,
                "data": data_list
        }

    except:
        frappe.local.response["message"] = {
            "error": "No document Found"
        } 



@frappe.whitelist(allow_guest=True)
def put_document_status(id,document_type,status,remarks=None):
    user1 =frappe.session.user
    oppr=frappe.get_last_doc('Opportunity',filters={"name":id})
    if user1 == oppr.fsl_assign_to:  
        try:
            doc =frappe.get_last_doc("Document Details", filters={"opportunity_id": id,"document_type":document_type})
          
            if status=="Approved": 
                # frappe.errprint("acc")                         
                frappe.db.set_value('Document Details', doc.name, 'document_remarks', None)
                frappe.db.set_value('Document Details', doc.name, 'status', status)
                frappe.db.commit()  
                frappe.local.response["message"] = {
                    "success_key": 1,
                    "data": {
                        "id":doc.name,          
                        "document_type":doc.document_type,
                        "status":doc.status,
                        "remarks":doc.document_remarks,
                        
            }
            }
                # frappe.db.commit()
            if status=="Reset":
                # frappe.errprint("re")
                frappe.db.set_value('Document Details', doc.name, 'status', None)
                frappe.db.set_value('Document Details', doc.name, 'document_remarks', None)
                frappe.db.commit()  
                frappe.local.response["message"] = {
                    "success_key": 1,
                    "data": {
                        "id":doc.name,          
                        "document_type":doc.document_type,
                        "status":doc.status,
                        "remarks":doc.document_remarks,
                        
            }
            }
                # frappe.db.commit()
                
            if status=="Rejected":
                # frappe.errprint("1")
                if remarks is not None:
                    # frappe.errprint("3")
                    frappe.db.set_value('Document Details', doc.name, 'status', status)
                    frappe.db.set_value('Document Details', doc.name, 'document_remarks', remarks)
                    frappe.db.commit()  
                    frappe.local.response["message"] = {
                    "success_key": 1,
                    "data": {
                        "id":doc.name,          
                        "document_type":doc.document_type,
                        "status":doc.status,
                        "remarks":doc.document_remarks,
                        
            }
            }
                    # frappe.db.commit()
                    
                    
                else:
                    
                    # frappe.errprint("2")
                    frappe.local.response["message"] = {
                    "error": "Remark is mandatory"
                    } 


        except:
            frappe.local.response["message"] = {
                "error": "No document Found"
            } 
    else : 
            # frappe.errprint(user_roles)
            frappe.local.response["message"] = {
            "success_key": 0,
            "message":"This User Has No permission",
            }