import frappe

@frappe.whitelist()
def get_approval_details(id,document_type):
   
    
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
        pan_remark=" "
        address_remark=" "
        profile2=" "
        document_remark=" "
        ipv_remark=" "
        esign_remark=""
        bank_remark=""
        segment_remark=""
        nomin_details = []
        try:
            
            oppr=frappe.get_doc('Document Details',id)
           
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
                pan="null"
                bank="null"
                segment="null"
                nominee="null"
           
           
           
        except:
           frappe.local.response["message"] = {
            "error": "No Opportunity Found"
        } 
            
            
        try:
            document= frappe.get_last_doc('Document Details', filters={"opportunity_id":id})
            
            if document:
                
                document1=document.document_status
                document_remark=document.document_remarks

                ipv=document.ipv_status
                ipv_remark=document.ipv_remarks

                esign=document.e_sign_status
                esign_remark=document.e_sign_remarks
            else:
                document1="null"
                ipv="null"
                esign="null"
           
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
                profile2 = profile.fsl_profile_remarks
            else:
                profile1="null"
           
        except:
           frappe.local.response["message"] = {
            "error": "No Profile Found"
        } 
                      
        if document_type == "Pan":
            frappe.local.response["message"] = {
                "success_key": 1,
                "data": {
                    "pan status":pan,
                    "Pan remarks" : pan_remark
                }
            }
        elif document_type=="Address":
            frappe.local.response["message"] = {
                "success_key": 1,
                "data": {
                "address status":address1,
                "address remarks" : address_remark
                }
            }
        elif document_type=="Profile" :
            frappe.local.response["message"] = {
                "success_key": 1,
                "data": {
                "profile status":profile1,
                "Profile remarks" : profile2
                }
            }
        if document_type=="Bank" :
            frappe.local.response["message"] = {
                "success_key": 1,
                "data": {
                "bank status":bank,
                "bank remarks" :bank_remark
                }
            }
        if document_type=="Segment" :
            frappe.local.response["message"] = {
                "success_key": 1,
                "data": {
                "segment status":segment,
                "segment remarks" :segment_remark
                }
            }
        if document_type== "Nominee" :
            frappe.local.response["message"] = {
                "success_key": 1,
                "data": {
                "nominee":nomin_details
                }
            }

        if document_type=="Document" :
            frappe.local.response["message"] = {
                "success_key": 1,
                "data": {
                "document status":document1,
                "document remarks" :document_remark
                }
            }

        elif document_type== "IPV":
            frappe.local.response["message"] = {
                "success_key": 1,
                "data": {
                "IPV status":ipv,
                "IPV remarks" : ipv_remark
                }
            }
        elif document_type=="Esign":
            frappe.local.response["message"] = {
                "success_key": 1,
                "data": {         

                "Esign status":esign,
                "Esign remarks" : esign_remark
            }        
        }
        
    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }