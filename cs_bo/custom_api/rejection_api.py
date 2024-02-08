import frappe

@frappe.whitelist()
def reject_details(id):
    data = []
    reject = {}
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
            
            oppr=frappe.get_doc('Opportunity',id)
           
            if oppr:
                
                pan=oppr.fsl_pan_status
                if pan == "Rejected":
                    reject["pan_status"]=oppr.fsl_pan_status
                    reject["pan_remark"]=oppr.fsl_pan_remark

                bank=oppr.fsl_bank_status
                if bank == "Rejected":
                    reject["bank_status"]=oppr.fsl_bank_status
                    reject["bank_remark"]=oppr.fsl_bank_remark
                    # bank_remark=oppr.fsl_bank_remark

                segment=oppr.fsl_segment_status
                if segment == "Rejected":
                    reject["segment_status"]=oppr.fsl_segment_status
                    reject["segment_remark"]=oppr.fsl_segment_remark
                # segment_remark=oppr.fsl_segment_remark

                
                for i in oppr.fsl_nominee_table:                   
                    nomin ={}
                    nomin["nominee_number"] = i.nominee_number
                    nomin["status"] = i.nominee_status
                    nomin["remarks"]=i.nominee_remarks
                    reject["nominee"] = nomin
                    # nomin_details.append(nomin)
           
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
                if document1 == "Rejected":
                    reject["document_status"]=oppr.document_status
                    reject["document_remark"]=oppr.document_remark
                    # document_remark=document.document_remarks

                ipv=document.ipv_status
                if ipv == "Rejected":
                    reject["ipv_status"]=oppr.ipv_status
                    reject["ipv_remarks"]=oppr.ipv_remarks
                # ipv_remark=document.ipv_remarks

                esign=document.e_sign_status
                if esign == "Rejected":
                    reject["e_sign_status"]=oppr.e_sign_status
                    reject["e_sign_remarks"]=oppr.e_sign_remarks
                # esign_remark=document.e_sign_remarks
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
                if address1 == "Rejected":
                    reject["fsl_address_status"]=oppr.fsl_address_status
                    reject["fsl_address_remarks"]=oppr.fsl_address_remarks
                # address_remark=address.fsl_address_remarks
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
                if profile1 == "Rejected":
                    reject["profile_status"]=oppr.profile_status
                    reject["fsl_profile_remarks"]=oppr.fsl_profile_remarks
                # profile2 = profile.fsl_profile_remarks
            else:
                profile1="null"
           
        except:
           frappe.local.response["message"] = {
            "error": "No Profile Found"
        } 
                      
        
        frappe.local.response["message"] = {
            "success_key": 1,
            "data": reject        
        }
        
    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }