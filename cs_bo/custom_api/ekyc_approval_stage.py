import frappe

@frappe.whitelist(allow_guest=True)
def get_approval_details(id):
    data = []
    
    try:
        
        # document = frappe.get_doc("Document Details", id)
        
        pan=""
        address1=""
        profile1=""
        bank=""
        segment=""
        nominee=""
        document1=""
        ipv=""
        esign=""
        pan_remark=""
        address_remark=""
        profile2=""
        document_remark=""
        ipv_remark=""
        esign_remark=""
        bank_remark=""
        segment_remark=""
        nomin_details = []
        try:
            
            oppr=frappe.get_doc('Opportunity',id)
           
            if oppr:
                
                
                pan=oppr.fsl_pan_status
                pan_remark=oppr.fsl_pan_remark

                bank=oppr.fsl_bank_status
                bank_remark=oppr.fsl_bank_remark

                segment=oppr.fsl_segment_status
                segment_remark=oppr.fsl_segment_remark

                
                for i in oppr.fsl_nominee_table:                   
                    nomin ={}
                    nomin["nominee_number"] = i.nominee_number
                    nomin["status"] = i.nominee_status
                    nomin["remarks"]=i.nominee_remarks
                    nomin_details.append(nomin)
           
            else:   
                frappe.local.response["message"] = {
                    "error": "No Opportunity Found"
                } 
           
           
           
        except:
           frappe.local.response["message"] = {
            "error": "No Opportunity Found"
        } 
            
    
        try:
            document1= frappe.get_list('Document Details', filters={"opportunity_id":id})
            # document_list=[]
            if document1:
                for i in document1:
                    document_dic={}
                    document = frappe.get_doc('Document Details',i.name)
                    # document_type = document.document_type
                    if document:
                        if document.document_type == "IPV":
                            ipv=document.status
                            ipv_remark=document.document_remarks

                        if document.document_type == "ESIGN_DOCUMENT":
                            esign=document.status
                            esign_remark=document.document_remarks
            else:
                # document1="null"
                # ipv="null"
                # ipv_remark="null"
                # esign="null"
                # esign_remark="null"
                frappe.local.response["message"] = {
                        "error": "No Document Found"
                    } 
           
        except:
           frappe.local.response["message"] = {
            "error": "No Document Found"
        } 
            
        try:
            address = frappe.get_last_doc('Address',filters={"fsl_from_opportunity":id})
            
            if address:
                
                address1=address.fsl_address_status
                address_remark=address.fsl_address_remarks
            else:
                address1="null"
        except:
           frappe.local.response["message"] = {
            "error": "No Address Found"
        } 
            
        
        try:
            profile = frappe.get_last_doc('Customer Profile',filters={"fsl_from_opportunity":id})
            
            if profile:
                
                profile1=profile.profile_status
                profile2 = profile.profile_remarks
            else:
                profile1="null"
           
        except:
           frappe.local.response["message"] = {
            "error": "No Profile Found"
        } 
                      
        
        frappe.local.response["message"] = {
            "success_key": 1,
            "data": {
                "pan status":pan,
                "Pan remarks" : pan_remark,

                "address status":address1,
                "address remarks" : address_remark,

                "profile status":profile1,
                "Profile remarks" : profile2,

                "bank status":bank,
                "bank remarks" :bank_remark,

                "segment status":segment,
                "segment remarks" :segment_remark,

                "nominee":nomin_details,


                # "document status":document1,
                # "document remarks" :document_remark,

                "IPV status":ipv,
                "IPV remarks" : ipv_remark,

                "Esign status":esign,
                "Esign remarks" : esign_remark
            }        
        }
        
    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }