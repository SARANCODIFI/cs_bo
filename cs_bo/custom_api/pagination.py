import frappe
from datetime import datetime, timedelta

@frappe.whitelist(allow_guest = True)
def get_pg_opportunity_details(from_date = None, to_date = None, pgstart = 0):
    if pgstart is not '0':
        pgstart = int(pgstart) * 20
    datas = []
    try:
        if from_date is None:
            from_date = (datetime.now() - timedelta(days=30)).date()
        if to_date is None:
            to_date = datetime.now().date()
    
        opprs = frappe.db.get_list('Opportunity',
            filters={'creation': ['between', [from_date, to_date]]},
            fields=['name', 'fsl_pan_no', 'fsl_stage', 'fsl_mobile_num', 'fsl_assign_to', 'fsl_user_name', 'status'],
            order_by='name desc',
            start=pgstart,
            page_length=20,
            as_list=True
        )


        
        for oppr in opprs:
           
                
            data = {
               "opportunity_id": oppr[0], 
                "customer_name": oppr[5],  
                "fsl_pan_no": oppr[1], 
                "fsl_mobile_num": oppr[3],  
                "fsl_assign_to": oppr[4],  
                "current_phase": get_current_phase(oppr[0]),  
                "phase": get_phase(oppr[0]), 
                "stage": oppr[2],  
            }
            datas.append(data)

        frappe.local.response["message"] = {
            "success_key": 1,
            "message": "Document Details Retrieved Successfully",
            "Data": datas,
        }
    except Exception as e:
       
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }

def get_current_phase(name):
    data_list = []
    pan=None
    address1=None
    profile1=None
    bank=None
    segment=None
    nominee=None
    document1=None
    ipv=None
    esign=None
    pan_remark=None
    address_remark=None
    profile2=None
    document_remark=None
    ipv_remark=None
    esign_remark=None
    bank_remark=None
    segment_remark=None
    # nomin_details = []
    try:
        # frappe.errprint("1")
        oppr=frappe.get_doc("Opportunity",name)
        document= frappe.get_last_doc('Document Details', filters={"opportunity_id":name})
        address = frappe.get_last_doc('Address',filters={"fsl_from_opportunity":name})
        profile = frappe.get_last_doc('Customer Profile',filters={"fsl_from_opportunity":name})
            
        if profile: 
            # frappe.errprint("5") 
            profile1=profile.profile_status
            data_list.append(profile1)
            
                    
            
        if address: 
            # frappe.errprint("4")
            address1=address.fsl_address_status
            data_list.append(address1)
        
        if document:
            # frappe.errprint("3")
            document1=document.document_status
            ipv=document.ipv_status
            esign=document.e_sign_status
            data_list.append(document1)
            data_list.append(ipv)
            data_list.append(esign)

        
        if oppr:
            # frappe.errprint("2")
            pan=oppr.fsl_pan_status
            bank=oppr.fsl_bank_status
            segment=oppr.fsl_segment_status
            data_list.append(pan)
            data_list.append(bank)
            data_list.append(segment)
            for i in oppr.fsl_nominee_table:                   
                data_list.append(i.nominee_status)
            
        all_approved = 1   
        all_reject = 1
        null_app = 1
        for stat in data_list:
            # frappe.errprint("6")
            if stat != "Approved":
                all_approved = 0
                break
        for stat in data_list:
            # frappe.errprint("6")
            if stat != "Rejected":
                all_reject = 0
                break
        for stat1 in data_list:
            # frappe.errprint("6")
            if stat1 != "null":
                null_app = 0
                break

        # stage = "Open"
        
        
        if oppr.fsl_assign_to is not None and all_approved == 1:
            # frappe.errprint(oppr.name)
            # frappe.errprint("Approved")
            # frappe.errprint(oppr.fsl_assign_to)
            stage="Approved"
        if oppr.fsl_assign_to is not None and all_approved == 0:
            # frappe.errprint(oppr.name)
            # frappe.errprint("Rejected")
            # frappe.errprint(oppr.fsl_assign_to)
            stage="Rejected"
        if oppr.fsl_assign_to is not None and all_approved == 0 and all_reject == 0: #            frappe.errprint("in")
            # frappe.errprint(oppr.name)
            # frappe.errprint("In-Progress")
            # frappe.errprint(oppr.fsl_assign_to)
            stage="In-Progress"
        if not oppr.fsl_assign_to :
            # frappe.errprint(oppr.name)
            # frappe.errprint("Open")
            # frappe.errprint(oppr.fsl_assign_to)
            stage = "Open"

        
        # else:
        #     stage="In-Progress"
        return stage

    
    except:
        # frappe.errprint("7")
        stage = "Open"
        return stage


def get_phase(name):
    
    try:
        oppr=frappe.get_doc("Opportunity",name)
        if oppr:
                if oppr.fsl_stage=="0.5":                            
                    stage="SMS verification"
                    
                if oppr.fsl_stage=="1":
                    stage="E-mail verification"
                if oppr.fsl_stage=="1.1":
                    stage="Password verification"
                    
                if oppr.fsl_stage=="2":
                    stage="Pan verification"
                if oppr.fsl_stage=="2.1":
                    stage="Pan NSDL Data Confirm verification"
                if oppr.fsl_stage=="2.2":
                    stage="Pan Confirm verification"
                if oppr.fsl_stage=="2.3":                            
                    stage="Pan KRA DOB Entry verification"
                    
                if oppr.fsl_stage=="3":
                    stage="Aadhar verification"
                    
                if oppr.fsl_stage =="4":
                    stage="Profile verification"
                    
                if oppr.fsl_stage =="5":
                    stage="Bank verification"                    
                if oppr.fsl_stage =="5.1":
                    stage="Penny verification"  
                                          
                if oppr.fsl_stage =="6":
                    stage="Segment verification"
                    
                if oppr.fsl_stage =="7":
                    stage="Payment verification"
                    
                if oppr.fsl_stage =="8":
                    stage="Nominee verification"                    
                if oppr.fsl_stage =="8.1":
                    stage="Nominee_1 verification"
                if oppr.fsl_stage =="8.2":
                    stage="Nominee_2 verification"
                if oppr.fsl_stage =="8.3":
                    stage="Nominee_3 verification"
                    
                if oppr.fsl_stage =="9":
                    stage="Document verification"
                    
                if oppr.fsl_stage =="10":
                    stage="IPV verification"
                    
                if oppr.fsl_stage =="11":
                    stage="PDF Download verification"
                    
                if oppr.fsl_stage =="12":
                    stage="E-Sign verification"
                    
                if oppr.fsl_stage =="13":
                    stage="Complete Email Attached verification"
                
                return stage
        else:
            frappe.response["message"] = {
                "Success": 0,                            
                "message": "Opportunity1 not found"
            }
    except:
        frappe.response["message"] = {
                "Success": 0,                            
                "message": "Opportunity2 not found"
            }
