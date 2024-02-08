import frappe

@frappe.whitelist()
def get_document_details(id):    
    try:
        
        # document = frappe.get_doc("Document Details", id)
        documents= frappe.get_all('Document Details', filters={"opportunity_id":id})
        datas = []
        for document1 in documents:
            document_dic = {}
            document = frappe.get_doc('Document Details',document1.name)
            document_dic["opportunity_id"] = document.opportunity_id
            document_dic["time"] = document.time
            document_dic["attachment_url"] = document.attachment_url
            document_dic["document_type"] = document.document_type
            document_dic["type_of_proof"] = document.type_of_proof
            document_dic["status"] = document.status
            document_dic["remarks"] = document.remarks
            document_dic["latitude"] = document.latitude
            document_dic["longitude"] = document.longitude
                       
            datas.append(document_dic)        
        # data.append(document_dic)
        
        frappe.local.response["message"] = {
            "success_key": 1,
            "data":datas     
        }
        
    # except:
    #     frappe.response["message"] = {
    #         "error":"No document details found for this opportunity"
    #     }
    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An errors occurred: {str(e)}"
        } 


@frappe.whitelist()
def delete_document_details(id,document_type):
    try:

        document= frappe.get_last_doc('Document Details', filters={"opportunity_id":id,"document_type":document_type})
        
        frappe.delete_doc('Document Details',document.name)
        frappe.response["message"] = {
                "success":"Document successfully deleted"
            }

    except:
        frappe.response["message"] = {
            "error":"No document details found."
        }


# @frappe.whitelist(allow_guest=True)
# def update_document_details(data):
#     datas = {}
#     for i in data:
#         try:
            
#             dd = frappe.get_last_doc('Document Details', filters={"opportunity_id": i["opportunity_id"]})
#             datas["opportunity_id"]=dd.opportunity_id
#             if "time" in i:
#                 dd.time = i["time"]
#                 datas["time"]=dd.time

#             if "attachment_url" in i:
#                 dd.attachment_url = i["attachment_url"]
#                 datas["attachment_url"]=dd.attachment_url

#             if "document_type" in i:
#                 dd.document_type = i["document_type"]
#                 datas["document_type"]= dd.document_type   

#             if "type_of_proof" in i:
#                 dd.type_of_proof = i["type_of_proof"]
#                 datas["type_of_proof"]= dd.type_of_proof

#             if "status" in i:
#                     dd.status = i["status"]
#                     datas["status"]= dd.status
                                
#             if "remarks" in i:                
#                 dd.remarks = i["remarks"]
#                 datas["remarks"]=dd.remarks
            
#             dd.save()
            

#             frappe.local.response["message"] = {
#                 "success_key": 1,
#                 "message":"Document Details Updated",
#                 "Data": datas,
                
#                 } 
                    

#         except :
           
#             try:
#                 dd = frappe.new_doc('Document Details')

#                 dd.opportunity_id = i.get("opportunity_id", None)
#                 datas["opportunity_id"] = dd.opportunity_id
#                 if "time" in i:
#                     dd.time = i["time"]
#                     datas["time"]=dd.time

#                 if "attachment_url" in i:
#                     dd.attachment_url = i["attachment_url"]
#                     datas["attachment_url"]=dd.attachment_url

#                 if "document_type" in i:
#                     dd.document_type = i["document_type"]
#                     datas["document_type"]= dd.document_type   

#                 if "type_of_proof" in i:
#                     dd.type_of_proof = i["type_of_proof"]
#                     datas["type_of_proof"]= dd.type_of_proof

#                 if "status" in i:
#                     dd.status = i["status"]
#                     datas["status"]= dd.status
                                
#                 if "remarks" in i:
                    
#                     dd.remarks = i["remarks"]
#                     datas["remarks"]=dd.remarks
                
#                 dd.save()


#                 frappe.local.response["message"] = {
#                     "success_key": 1,
#                     "message": "Document Details Submitted",
#                     "Data": datas,
#                 } 

#             except Exception as e:
#                 frappe.local.response["message"] = {
#                     "error": "An error occurred or Opportunity Not Found"
#                 }

@frappe.whitelist()
def update_document_details(data):
    datas = {}
    for i in data:
        try:
                       
            dd = frappe.get_last_doc('Document Details', filters={"opportunity_id": i["opportunity_id"],"document_type":i["document_type"]})
            datas["opportunity_id"]=dd.opportunity_id
            if dd.status=="Approved":                
                frappe.local.response["message"] = {                            
                "message": "Document Details Already Submitted",                            
                } 
            else:              
                
                if "time" in i:
                    dd.time = i["time"]
                    datas["time"]=dd.time

                if "attachment_url" in i:
                    dd.attachment_url = i["attachment_url"]
                    datas["attachment_url"]=dd.attachment_url

                if "document_type" in i:
                    dd.document_type = i["document_type"]
                    datas["document_type"]= dd.document_type   

                if "type_of_proof" in i:
                    dd.type_of_proof = i["type_of_proof"]
                    datas["type_of_proof"]= dd.type_of_proof

                if "status" in i:
                    dd.status = i["status"]
                    datas["status"]= dd.status
                                
                if "remarks" in i:                    
                    dd.remarks = i["remarks"]
                    datas["remarks"]=dd.remarks
                    
                if "latitude" in i:                    
                    dd.latitude = i["latitude"]
                    datas["latitude"]=dd.latitude
                    
                if "longitude" in i:                    
                    dd.longitude = i["longitude"]
                    datas["longitude"]=dd.longitude
                
                dd.save()


                frappe.local.response["message"] = {
                    "success_key": 1,
                    "message": "Document Details Updated Successfully",
                    "Data": datas,
                }
        except:
                dd = frappe.new_doc('Document Details')
                if "opportunity_id" in i:
                    dd.opportunity_id = i["opportunity_id"]
                    datas["opportunity_id"]=dd.opportunity_id

                if "time" in i:
                    dd.time = i["time"]
                    datas["time"]=dd.time

                if "attachment_url" in i:
                    dd.attachment_url = i["attachment_url"]
                    datas["attachment_url"]=dd.attachment_url

                if "document_type" in i:
                    dd.document_type = i["document_type"]
                    datas["document_type"]= dd.document_type   

                if "type_of_proof" in i:
                    dd.type_of_proof = i["type_of_proof"]
                    datas["type_of_proof"]= dd.type_of_proof

                if "status" in i:
                    dd.status = i["status"]
                    datas["status"]= dd.status
                                
                if "remarks" in i:                    
                    dd.remarks = i["remarks"]
                    datas["remarks"]=dd.remarks
                    
                if "latitude" in i:                    
                    dd.latitude = i["latitude"]
                    datas["latitude"]=dd.latitude
                    
                if "longitude" in i:                    
                    dd.longitude = i["longitude"]
                    datas["longitude"]=dd.longitude
                
                dd.save()


                frappe.local.response["message"] = {
                    "success_key": 1,
                    "message": "Document Details Uploaded Successfully",
                    "Data": datas,
                }           