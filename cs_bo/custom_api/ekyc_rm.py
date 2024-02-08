import frappe

@frappe.whitelist()
def get_rm_details():
    
    user1 = frappe.session.user
        
    try:
        frappe.msgprint("1")
        emp=frappe.get_last_doc("Employee",filters={"user_id":user1}) 
        frappe.msgprint(emp.name)
        if emp:
            try:
                frappe.errprint("12345678")
                oppr=frappe.get_list("Opportunity",filters={"fsl_referral_by":emp.name})
                
                if oppr:
                    frappe.errprint("0")
                    oppr_list=[]
                    for i in oppr:
                        frappe.errprint("123")
                        oppr_dic={}
                        oppr_dic["name"] = oppr.customer_name
                        oppr_dic["applicationid"]= oppr.name
                        oppr_dic["pan"]= oppr.fsl_pan_no
                        stagetype=oppr.fsl_stage
                        # stage =  ""
                        if int(oppr.fsl_stage)==int(0.5):
                            oppr_dic["stage"]="SMS verification"
                        # if stagetype==1:
                        #     oppr_dic["stage"]="E-mail verification"
                        # if stagetype==1.1:
                        #     oppr_dic["stage"]="Password verification"
                        # if stagetype==2:
                        #     oppr_dic["stage"]="Pan verification"
                        # if stagetype==2.1:
                        #     oppr_dic["stage"]="Pan NSDL Data Confirm verification"
                        # if stagetype==2.2:
                        #     oppr_dic["stage"]="Pan Confirm verification"
                        # if stagetype==2.3:
                        #     oppr_dic["stage"]="Pan KRA DOB Entry verification"
                        # if stagetype==3:
                        #     oppr_dic["stage"]="Aadhar verification"
                        # if stagetype==4:
                        #     oppr_dic["stage"]="Profile verification"
                        # if stagetype==5:
                        #     oppr_dic["stage"]="Bank verification"
                        # if stagetype==5.1:
                        #     oppr_dic["stage"]="Penny verification"                        
                        # if stagetype==6:
                        #     oppr_dic["stage"]="Segment verification"
                        # if stagetype==7:
                        #     oppr_dic["stage"]="Payment verification"
                        # if stagetype==8:
                        #     oppr_dic["stage"]="Nominee verification"
                        # if stagetype==8.1:
                        #     oppr_dic["stage"]="Nominee_1 verification"
                        # if stagetype==8.2:
                        #     oppr_dic["stage"]="Nominee_2 verification"
                        # if stagetype==8.3:
                        #     oppr_dic["stage"]="Nominee_3 verification"
                        # if stagetype==9:
                        #     oppr_dic["stage"]="Document verification"
                        # if stagetype==10:
                        #     oppr_dic["stage"]="IPV verification"
                        # if stagetype==11:
                        #     oppr_dic["stage"]="PDF Download verification"
                        # if stagetype==12:
                        #     oppr_dic["stage"]="E-Sign verification"
                        # if stagetype==13:
                        #     oppr_dic["stage"]="Complete Email Attached verification"                  

                        oppr_dic["mobile"] = oppr.fsl_mobile_num
                        oppr_dic["assignto"] = oppr.fsl_assign_to
                        oppr_list.append(oppr_dic)


                        frappe.response["message"] = {
                            "Success": 1,                            
                            "data": oppr_list
                        }
                else:
                    frappe.response["message"] = {
                        "Success": 0,                            
                        "message": "Opportunity not found"
                    }
            except:
                frappe.response["message"] = {
                        "Success": 0,                            
                        "message": "Opportunity not found"
                    }

    except:
        frappe.response["message"] = {
                            "Success": 0,                            
                            "message":"Employee not found"
                        }









                       
        