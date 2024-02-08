import frappe

@frappe.whitelist(allow_guest=True)
def get_rm_details1(emp_email_id):
    
    # user1 = frappe.session.user
        
    try:
        emp=frappe.get_last_doc("Employee",filters={"user_id":emp_email_id}) 
        # user_roles = frappe.get_roles(user1)
        
        if  emp: 
            
                    try:
                                    
                        oppr1=frappe.get_list("Opportunity",filters={"fsl_referral_by":emp.name})  
                        if oppr1:                    
                            oppr_list=[]
                            for i in oppr1:
                                
                                oppr=frappe.get_doc("Opportunity",i.name)
                                oppr_dic={}
                                oppr_dic["name"] = oppr.customer_name
                                oppr_dic["applicationid"]= oppr.fsl_application_id
                                oppr_dic["pan"]= oppr.fsl_pan_no                      
                                    
                
                
                                if oppr.fsl_stage=="0.5":                            
                                    oppr_dic["stage"]="SMS verification"
                                if oppr.fsl_stage=="1":
                                    oppr_dic["stage"]="E-mail verification"
                                if oppr.fsl_stage=="1.1":
                                    oppr_dic["stage"]="Password verification"
                                if oppr.fsl_stage=="2":
                                    oppr_dic["stage"]="Pan verification"
                                if oppr.fsl_stage=="2.1":
                                    oppr_dic["stage"]="Pan NSDL Data Confirm verification"
                                if oppr.fsl_stage=="2.2":
                                    oppr_dic["stage"]="Pan Confirm verification"
                                if oppr.fsl_stage=="2.3":                            
                                    oppr_dic["stage"]="Pan KRA DOB Entry verification"
                                if oppr.fsl_stage=="3":
                                    oppr_dic["stage"]="Aadhar verification"
                                if oppr.fsl_stage =="4":
                                    oppr_dic["stage"]="Profile verification"
                                if oppr.fsl_stage =="5":
                                    oppr_dic["stage"]="Bank verification"
                                if oppr.fsl_stage =="5.1":
                                    oppr_dic["stage"]="Penny verification"                        
                                if oppr.fsl_stage =="6":
                                    oppr_dic["stage"]="Segment verification"
                                if oppr.fsl_stage =="7":
                                    oppr_dic["stage"]="Payment verification"
                                if oppr.fsl_stage =="8":
                                    oppr_dic["stage"]="Nominee verification"
                                if oppr.fsl_stage =="8.1":
                                    oppr_dic["stage"]="Nominee_1 verification"
                                if oppr.fsl_stage =="8.2":
                                    oppr_dic["stage"]="Nominee_2 verification"
                                if oppr.fsl_stage =="8.3":
                                    oppr_dic["stage"]="Nominee_3 verification"
                                if oppr.fsl_stage =="9":
                                    oppr_dic["stage"]="Document verification"
                                if oppr.fsl_stage =="10":
                                    oppr_dic["stage"]="IPV verification"
                                if oppr.fsl_stage =="11":
                                    oppr_dic["stage"]="PDF Download verification"
                                if oppr.fsl_stage =="12":
                                    oppr_dic["stage"]="E-Sign verification"
                                if oppr.fsl_stage =="13":
                                    oppr_dic["stage"]="Complete Email Attached verification"             

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
                    except Exception as e:
                        frappe.local.response["message"] = {
                            "error": f"An error occurred: {str(e)}"
                        }
    except:
        frappe.response["message"] = {
                            "Success": 0,                            
                            "message":"Employee not found"
                        }        
        

###########
@frappe.whitelist(allow_guest=True)
def get_rm_details2(emp_email_id):
    frappe.errprint("new")
    try:
        emp=frappe.get_last_doc("Employee",filters={"user_id":emp_email_id}) 
        
        if  emp: 
            
                    try:
                        fun = 1
                        frappe.errprint(emp.name)    
                        if frappe.db.exists("Opportunity",{"fsl_referral_by":emp.name }):
                            fun = 0
                        oppr1=frappe.get_list("Opportunity",filters={"fsl_referral_by":emp.name})  
                        if frappe.db.exists("Opportunity",{"fsl_referral_by":emp_email_id }):
                            fun = 0
                        opprs=frappe.get_list("Opportunity",filters={"fsl_referral_by":emp_email_id })
                        oppr_list=[]
                        if oppr1:                    
                            
                            for i in oppr1:
                                oppr=frappe.get_doc("Opportunity",i.name)
                                oppr_dic={}
                                oppr_dic["name"] = oppr.customer_name
                                oppr_dic["applicationid"]= oppr.fsl_application_id
                                oppr_dic["pan"]= oppr.fsl_pan_no   
                                oppr_dic["fsl_referral_by"] = emp.name
                                oppr_dic["fsl_referral_name"] = emp.employee_name
                                oppr_dic["fsl_referral_branch"] = emp.branch
                                oppr_dic["fsl_referral_designation"] = emp.designation
                                if frappe.db.exists("Lead",{"fsl_referral_rm":emp.name}):
                                    oppr_dic["stage"]="Lead Referred"
                                if frappe.db.exists("Opportunity",{"fsl_mobile_num":oppr.fsl_mobile_num}):
                                    oppr_dic["stage"]="In-Progress"
                                if oppr.fsl_stage =="13":
                                    oppr_dic["stage"]="Completed"  
                                

                                oppr_dic["mobile"] = oppr.fsl_mobile_num
                                oppr_dic["assignto"] = oppr.fsl_assign_to
                                oppr_list.append(oppr_dic)

                        if opprs:                    
                            
                            for i in oppr1:
                                oppr=frappe.get_doc("Opportunity",i.name)
                                oppr_dic={}
                                oppr_dic["name"] = oppr.customer_name
                                oppr_dic["applicationid"]= oppr.fsl_application_id
                                oppr_dic["pan"]= oppr.fsl_pan_no   
                                oppr_dic["fsl_referral_by"] = emp.name
                                oppr_dic["fsl_referral_name"] = emp.employee_name
                                oppr_dic["fsl_referral_branch"] = emp.branch
                                oppr_dic["fsl_referral_designation"] = emp.designation
                                if frappe.db.exists("Lead",{"mobile_no":oppr.fsl_mobile_num}):
                                    oppr_dic["stage"]="Lead Referred"
                                if oppr:
                                    oppr_dic["stage"]="In-Progress"
                                if oppr.fsl_stage =="13":
                                    oppr_dic["stage"]="Completed" 

                                oppr_dic["mobile"] = oppr.fsl_mobile_num
                                oppr_dic["assignto"] = oppr.fsl_assign_to
                                oppr_list.append(oppr_dic)   

                        frappe.response["message"] = {
                                    "Success": 1,                            
                                    "data": oppr_list
                                }   
                        
                        if fun:
                            frappe.response["message"] = {
                                "Success": 0,                            
                                "message": "Opportunity not found"
                            }
                    except Exception as e:
                        frappe.local.response["message"] = {
                            "error": f"An error occurred: {str(e)}"
                        }
    except:
        frappe.response["message"] = {
                            "Success": 0,                            
                            "message":"Employee not found"
                        }      
        








@frappe.whitelist(allow_guest=True)
def get_rm_details(emp_email_id):
    
    try:
       
        emp=frappe.get_last_doc("Employee",filters={"user_id":emp_email_id}) 
        
        if  emp:  
                
                try:
                    fun = 1
                    oppr_list=[]
                    
                    if frappe.db.exists("Lead",{"fsl_referral_rm":emp.name }):
                        
                        fun = 0
                        lead1 = frappe.get_all("Lead",filters={"fsl_referral_rm":emp.name,"status":"Lead"})       

                        for l in lead1:    
                            oppr_dic={}    
                            i = frappe.get_last_doc("Lead",l)      

                            oppr_dic["name"] = i.first_name 
                            oppr_dic["fsl_referral_by"] = emp.name
                            oppr_dic["fsl_referral_name"] = emp.employee_name
                            oppr_dic["fsl_referral_branch"] = emp.branch
                            oppr_dic["fsl_referral_designation"] = emp.designation                              
                            oppr_dic["mobile"] = i.mobile_no
                            oppr_dic["stage"]="Referred"  
                            
                            oppr_list.append(oppr_dic)
                            



                    if frappe.db.exists("Opportunity",{"fsl_referral_by":emp.name }):
                            
                            fun = 0
                            opprs=frappe.get_all("Opportunity",filters={"fsl_referral_by":emp.name})                           
                            # frappe.errprint(emp.name)
                            for oppr1 in opprs:
                                
                                oppr_dic={}
                                oppr=frappe.get_doc("Opportunity",oppr1)
                                
                                oppr_dic["customer_name"] = oppr.customer_name
                                oppr_dic["opportunity_id"]= oppr.name
                                oppr_dic["fsl_pan_no"]= oppr.fsl_pan_no   
                                oppr_dic["fsl_referral_by"] = emp.name
                                oppr_dic["fsl_referral_name"] = emp.employee_name
                                oppr_dic["fsl_referral_branch"] = emp.branch
                                oppr_dic["fsl_referral_designation"] = emp.designation                              
                                
                                oppr_dic["fsl_mobile_num"] = oppr.fsl_mobile_num
                                if oppr.fsl_stage =="13":
                                    oppr_dic["current phase"]="Completed"  
                                else :
                                    oppr_dic["current phase"]="InProgress"
                                    
                                oppr_dic["stage"]=oppr.fsl_stage
                                oppr_dic["fsl_assign_to"] = oppr.fsl_assign_to
                                oppr_dic["time"] = oppr.custom_assign_time
                                
                
                                if oppr.fsl_stage=="0.5":                            
                                    oppr_dic["phase"]="SMS verification"
                                if oppr.fsl_stage=="1":
                                    oppr_dic["phase"]="E-mail verification"
                                if oppr.fsl_stage=="1.1":
                                    oppr_dic["phase"]="Password verification"
                                if oppr.fsl_stage=="2":
                                    oppr_dic["phase"]="Pan verification"
                                if oppr.fsl_stage=="2.1":
                                    oppr_dic["phase"]="Pan NSDL Data Confirm verification"
                                if oppr.fsl_stage=="2.2":
                                    oppr_dic["phase"]="Pan Confirm verification"
                                if oppr.fsl_stage=="2.3":                            
                                    oppr_dic["phase"]="Pan KRA DOB Entry verification"
                                if oppr.fsl_stage=="3":
                                    oppr_dic["phase"]="Aadhar verification"
                                if oppr.fsl_stage =="4":
                                    oppr_dic["phase"]="Profile verification"
                                if oppr.fsl_stage =="5":
                                    oppr_dic["phase"]="Bank verification"
                                if oppr.fsl_stage =="5.1":
                                    oppr_dic["phase"]="Penny verification"                        
                                if oppr.fsl_stage =="6":
                                    oppr_dic["phase"]="Segment verification"
                                if oppr.fsl_stage =="7":
                                    oppr_dic["phase"]="Payment verification"
                                if oppr.fsl_stage =="8":
                                    oppr_dic["phase"]="Nominee verification"
                                if oppr.fsl_stage =="8.1":
                                    oppr_dic["phase"]="Nominee_1 verification"
                                if oppr.fsl_stage =="8.2":
                                    oppr_dic["phase"]="Nominee_2 verification"
                                if oppr.fsl_stage =="8.3":
                                    oppr_dic["phase"]="Nominee_3 verification"
                                if oppr.fsl_stage =="9":
                                    oppr_dic["phase"]="Document verification"
                                if oppr.fsl_stage =="10":
                                    oppr_dic["phase"]="IPV verification"
                                if oppr.fsl_stage =="11":
                                    oppr_dic["phase"]="PDF Download verification"
                                if oppr.fsl_stage =="12":
                                    oppr_dic["phase"]="E-Sign verification"
                                if oppr.fsl_stage =="13":
                                    oppr_dic["phase"]="Complete Email Attached verification"             

                                
                                oppr_list.append(oppr_dic)

   ####################
                                                        
                    if frappe.db.exists("Lead",{"fsl_referral_rm":emp_email_id }):
                        
                        fun = 0
                        lead1 = frappe.get_all("Lead",filters={"fsl_referral_rm":emp_email_id,"status":"Lead"})       

                        for l in lead1:    
                            oppr_dic={}    
                            i = frappe.get_last_doc("Lead",l)      

                            oppr_dic["name"] = i.first_name 
                            oppr_dic["fsl_referral_by"] = emp.name
                            oppr_dic["fsl_referral_name"] = emp.employee_name
                            oppr_dic["fsl_referral_branch"] = emp.branch
                            oppr_dic["fsl_referral_designation"] = emp.designation                              
                            oppr_dic["mobile"] = i.mobile_no
                            oppr_dic["stage"]="Referred"  
                            
                            oppr_list.append(oppr_dic)
                            



                    if frappe.db.exists("Opportunity",{"fsl_referral_by":emp_email_id }):
                            fun = 0
                            opprs=frappe.get_all("Opportunity",filters={"fsl_referral_by":emp_email_id})                           
                           
                            for oppr1 in opprs:
                                oppr_dic={}
                                oppr=frappe.get_doc("Opportunity",oppr1)
                                
                                oppr_dic["customer_name"] = oppr.customer_name
                                oppr_dic["opportunity_id"]= oppr.name
                                oppr_dic["fsl_pan_no"]= oppr.fsl_pan_no   
                                oppr_dic["fsl_referral_by"] = emp.name
                                oppr_dic["fsl_referral_name"] = emp.employee_name
                                oppr_dic["fsl_referral_branch"] = emp.branch
                                oppr_dic["fsl_referral_designation"] = emp.designation                              
                                
                                oppr_dic["fsl_mobile_num"] = oppr.fsl_mobile_num
                                if oppr.fsl_stage =="13":
                                    oppr_dic["current phase"]="Completed"  
                                else :
                                    oppr_dic["current phase"]="InProgress"
                                oppr_dic["stage"]=oppr.fsl_stage
                                oppr_dic["fsl_assign_to"] = oppr.fsl_assign_to
                                oppr_dic["time"] = oppr.custom_assign_time
                
                                if oppr.fsl_stage=="0.5":                            
                                    oppr_dic["phase"]="SMS verification"
                                if oppr.fsl_stage=="1":
                                    oppr_dic["phase"]="E-mail verification"
                                if oppr.fsl_stage=="1.1":
                                    oppr_dic["phase"]="Password verification"
                                if oppr.fsl_stage=="2":
                                    oppr_dic["phase"]="Pan verification"
                                if oppr.fsl_stage=="2.1":
                                    oppr_dic["phase"]="Pan NSDL Data Confirm verification"
                                if oppr.fsl_stage=="2.2":
                                    oppr_dic["phase"]="Pan Confirm verification"
                                if oppr.fsl_stage=="2.3":                            
                                    oppr_dic["phase"]="Pan KRA DOB Entry verification"
                                if oppr.fsl_stage=="3":
                                    oppr_dic["phase"]="Aadhar verification"
                                if oppr.fsl_stage =="4":
                                    oppr_dic["phase"]="Profile verification"
                                if oppr.fsl_stage =="5":
                                    oppr_dic["phase"]="Bank verification"
                                if oppr.fsl_stage =="5.1":
                                    oppr_dic["phase"]="Penny verification"                        
                                if oppr.fsl_stage =="6":
                                    oppr_dic["phase"]="Segment verification"
                                if oppr.fsl_stage =="7":
                                    oppr_dic["phase"]="Payment verification"
                                if oppr.fsl_stage =="8":
                                    oppr_dic["phase"]="Nominee verification"
                                if oppr.fsl_stage =="8.1":
                                    oppr_dic["phase"]="Nominee_1 verification"
                                if oppr.fsl_stage =="8.2":
                                    oppr_dic["phase"]="Nominee_2 verification"
                                if oppr.fsl_stage =="8.3":
                                    oppr_dic["phase"]="Nominee_3 verification"
                                if oppr.fsl_stage =="9":
                                    oppr_dic["phase"]="Document verification"
                                if oppr.fsl_stage =="10":
                                    oppr_dic["phase"]="IPV verification"
                                if oppr.fsl_stage =="11":
                                    oppr_dic["phase"]="PDF Download verification"
                                if oppr.fsl_stage =="12":
                                    oppr_dic["phase"]="E-Sign verification"
                                if oppr.fsl_stage =="13":
                                    oppr_dic["phase"]="Complete Email Attached verification"             

                                oppr_list.append(oppr_dic)                             
                                
                    # if frappe.db.exists("Opportunity",{"fsl_referral_rm":emp_email_id }):
                    #     fun = 0
                    #     lead = frappe.get_all("Lead",filters={"fsl_referral_rm":emp_email_id})                 
                            
                    #     for i in lead:
                            
                    #         oppr_dic["mobile"] = i.mobile_no
                    #         oppr_dic["stage"]="Lead Referred"
                            
                    #         if frappe.db.exists("Opportunity",{"fsl_mobile_num":i.mobile_no }):
                                
                    #             oppr=frappe.get_last_doc("Opportunity",filters={"fsl_mobile_num":i.mobile_no })
                                
                    #             oppr_dic["name"] = oppr.customer_name
                    #             oppr_dic["applicationid"]= oppr.fsl_application_id
                    #             oppr_dic["pan"]= oppr.fsl_pan_no   
                    #             oppr_dic["fsl_referral_by"] = emp.name
                    #             oppr_dic["fsl_referral_name"] = emp.employee_name
                    #             oppr_dic["fsl_referral_branch"] = emp.branch
                    #             oppr_dic["fsl_referral_designation"] = emp.designation
                    #             oppr_dic["stage"]="In-Progress"
                    #             if oppr.fsl_stage =="13":
                    #                 oppr_dic["stage"]="Completed"  
                                

                    #             oppr_dic["mobile"] = oppr.fsl_mobile_num
                    #             oppr_dic["assignto"] = oppr.fsl_assign_to
                    #         oppr_list.append(oppr_dic)
                    
                    if fun:
                            frappe.response["message"] = {
                                "Success": 0,                            
                                "message": "Referral not found"
                            }
                    
                    frappe.response["message"] = {
                                    "Success": 1,                            
                                    "data": oppr_list
                                } 

                except Exception as e:
                        frappe.local.response["message"] = {
                            "error": f"An error occurred: {str(e)}"
                        }
    except:
        frappe.response["message"] = {
                            "Success": 0,                            
                            "message":"Employee not found"
                        }  


@frappe.whitelist(allow_guest=True)
def get_rm_ref_details(emp_email_id):
    
    try:
       
        emp=frappe.get_last_doc("Employee",filters={"user_id":emp_email_id}) 
        
        if  emp:  
                
                try:
                    fun = 1
                    oppr_list=[]
                    
                    # if frappe.db.exists("Lead",{"fsl_referral_rm":emp.name }):
                        
                    #     fun = 0
                    #     lead1 = frappe.get_all("Lead",filters={"fsl_referral_rm":emp.name,"status":"Lead"})       

                    #     for l in lead1:    
                    #         oppr_dic={}    
                    #         i = frappe.get_last_doc("Lead",l)      

                    #         oppr_dic["name"] = i.first_name 
                    #         oppr_dic["reference_id"] = emp.name
                    #         oppr_dic["referral_name"] = emp.employee_name
                    #         oppr_dic["branch"] = emp.branch
                    #         oppr_dic["fsl_referral_designation"] = emp.designation                              
                    #         oppr_dic["mobile"] = i.mobile_no
                    #         oppr_dic["stage"]="Referred"  
                            
                    #         oppr_list.append(oppr_dic)
                            



                    if frappe.db.exists("Opportunity",{"fsl_referral_by":emp.name }):
                            
                            fun = 0
                            opprs=frappe.get_all("Opportunity",filters={"fsl_referral_by":emp.name})                           
                            # frappe.errprint(emp.name)
                            for oppr1 in opprs:
                                
                                oppr_dic={}
                                oppr=frappe.get_doc("Opportunity",oppr1)
                                # frappe.errprint('assign')
                                # frappe.errprint(oppr.fsl_assign_to)
                                if oppr.fsl_assign_to:
                                    try:
                                        assign=frappe.get_doc("User",oppr.fsl_assign_to)
                                        oppr_dic["assigned_person_name"] = assign.full_name
                                        # frappe.errprint("11234567")
                                        # frappe.errprint(assign.username)
                                    except:
                                        frappe.errprint("")
                                # frappe.errprint(oppr.fsl_referral_by)
                                    # oppr_dic["assigned_person_name"] = assign.full_name
                                oppr_dic["customer_name"] = oppr.customer_name
                                oppr_dic["opportunity_id"]= oppr.name
                                oppr_dic["fsl_pan_no"]= oppr.fsl_pan_no  
                                # oppr_dic["reference_id"]= oppr.fsl_referral_by
                                # oppr_dic["reference_id1"] = oppr.fsl_referral_by
                                oppr_dic["referral_name"] = emp.employee_name
                                oppr_dic["branch"] = emp.branch
                                oppr_dic["fsl_referral_designation"] = emp.designation                              
                                
                                oppr_dic["fsl_mobile_num"] = oppr.fsl_mobile_num
                                
                                
                                oppr_dic["email_id"] = oppr.fsl_email_id
                                oppr_dic["reference_id"] = oppr.fsl_referral_by
                                
                                oppr_dic["modified"] = oppr.modified 
                                oppr_dic["fsl_mode_of_application"] = oppr.fsl_mode_of_application  
                                if oppr.fsl_stage =="13":
                                    oppr_dic["current phase"]="Completed"  
                                else :
                                    oppr_dic["current phase"]="InProgress"
                                    
                                oppr_dic["stage"]=oppr.fsl_stage
                                oppr_dic["fsl_assign_to"] = oppr.fsl_assign_to
                                oppr_dic["time"] = oppr.custom_assign_time
                                
                
                                if oppr.fsl_stage=="0.5":                            
                                    oppr_dic["phase"]="SMS verification"
                                if oppr.fsl_stage=="1":
                                    oppr_dic["phase"]="E-mail verification"
                                if oppr.fsl_stage=="1.1":
                                    oppr_dic["phase"]="Password verification"
                                if oppr.fsl_stage=="2":
                                    oppr_dic["phase"]="Pan verification"
                                if oppr.fsl_stage=="2.1":
                                    oppr_dic["phase"]="Pan NSDL Data Confirm verification"
                                if oppr.fsl_stage=="2.2":
                                    oppr_dic["phase"]="Pan Confirm verification"
                                if oppr.fsl_stage=="2.3":                            
                                    oppr_dic["phase"]="Pan KRA DOB Entry verification"
                                if oppr.fsl_stage=="3":
                                    oppr_dic["phase"]="Aadhar verification"
                                if oppr.fsl_stage =="4":
                                    oppr_dic["phase"]="Profile verification"
                                if oppr.fsl_stage =="5":
                                    oppr_dic["phase"]="Bank verification"
                                if oppr.fsl_stage =="5.1":
                                    oppr_dic["phase"]="Penny verification"                        
                                if oppr.fsl_stage =="6":
                                    oppr_dic["phase"]="Segment verification"
                                if oppr.fsl_stage =="7":
                                    oppr_dic["phase"]="Payment verification"
                                if oppr.fsl_stage =="8":
                                    oppr_dic["phase"]="Nominee verification"
                                if oppr.fsl_stage =="8.1":
                                    oppr_dic["phase"]="Nominee_1 verification"
                                if oppr.fsl_stage =="8.2":
                                    oppr_dic["phase"]="Nominee_2 verification"
                                if oppr.fsl_stage =="8.3":
                                    oppr_dic["phase"]="Nominee_3 verification"
                                if oppr.fsl_stage =="9":
                                    oppr_dic["phase"]="Document verification"
                                if oppr.fsl_stage =="10":
                                    oppr_dic["phase"]="IPV verification"
                                if oppr.fsl_stage =="11":
                                    oppr_dic["phase"]="PDF Download verification"
                                if oppr.fsl_stage =="12":
                                    oppr_dic["phase"]="E-Sign verification"
                                if oppr.fsl_stage =="13":
                                    oppr_dic["phase"]="Complete Email Attached verification"             

                                
                                oppr_list.append(oppr_dic)

   ####################
                                                        
                    # if frappe.db.exists("Lead",{"fsl_referral_rm":emp_email_id }):
                        
                    #     fun = 0
                    #     lead1 = frappe.get_all("Lead",filters={"fsl_referral_rm":emp_email_id,"status":"Lead"})       

                    #     for l in lead1:    
                    #         oppr_dic={}    
                    #         i = frappe.get_last_doc("Lead",l)      

                    #         oppr_dic["name"] = i.first_name 
                    #         oppr_dic["fsl_referral_by"] = emp.name
                    #         oppr_dic["fsl_referral_name"] = emp.employee_name
                    #         oppr_dic["fsl_referral_branch"] = emp.branch
                    #         oppr_dic["fsl_referral_designation"] = emp.designation                              
                    #         oppr_dic["mobile"] = i.mobile_no
                    #         oppr_dic["stage"]="Referred"  
                            
                    #         oppr_list.append(oppr_dic)
                            



                    if frappe.db.exists("Opportunity",{"fsl_referral_by":emp_email_id }):
                            fun = 0
                            opprs=frappe.get_all("Opportunity",filters={"fsl_referral_by":emp_email_id})                           
                           
                            for oppr1 in opprs:
                                oppr_dic={}
                                oppr=frappe.get_doc("Opportunity",oppr1)
                                if oppr.fsl_assign_to:
                                    try:
                                        assign=frappe.get_doc("User",oppr.fsl_assign_to)
                                        oppr_dic["assigned_person_name"] = assign.full_name
                                        # frappe.errprint("11234567")
                                        # frappe.errprint(assign.username)
                                    except:
                                        frappe.errprint("")
                                # frappe.errprint(oppr.fsl_referral_by)
                                oppr_dic["customer_name"] = oppr.customer_name
                                oppr_dic["opportunity_id"]= oppr.name
                                oppr_dic["fsl_pan_no"]= oppr.fsl_pan_no 
                                # oppr_dic["reference_id"]= oppr.fsl_referral_by  
                                # oppr_dic["reference_id1"] = oppr.fsl_referral_by
                                oppr_dic["referral_name"] = emp.employee_name
                                oppr_dic["branch"] = emp.branch
                                oppr_dic["fsl_referral_designation"] = emp.designation
                                oppr_dic["fsl_mobile_num"] = oppr.fsl_mobile_num
                                
                                  
                                oppr_dic["email_id"] = oppr.fsl_email_id
                                oppr_dic["reference_id"] = oppr.fsl_referral_by
                                
                                oppr_dic["modified"] = oppr.modified 
                                oppr_dic["fsl_mode_of_application"] = oppr.fsl_mode_of_application  
                                
                                if oppr.fsl_stage =="13":
                                    oppr_dic["current phase"]="Completed"  
                                else :
                                    oppr_dic["current phase"]="InProgress"
                                oppr_dic["stage"]=oppr.fsl_stage
                                oppr_dic["fsl_assign_to"] = oppr.fsl_assign_to
                                oppr_dic["time"] = oppr.custom_assign_time
                
                                if oppr.fsl_stage=="0.5":                            
                                    oppr_dic["phase"]="SMS verification"
                                if oppr.fsl_stage=="1":
                                    oppr_dic["phase"]="E-mail verification"
                                if oppr.fsl_stage=="1.1":
                                    oppr_dic["phase"]="Password verification"
                                if oppr.fsl_stage=="2":
                                    oppr_dic["phase"]="Pan verification"
                                if oppr.fsl_stage=="2.1":
                                    oppr_dic["phase"]="Pan NSDL Data Confirm verification"
                                if oppr.fsl_stage=="2.2":
                                    oppr_dic["phase"]="Pan Confirm verification"
                                if oppr.fsl_stage=="2.3":                            
                                    oppr_dic["phase"]="Pan KRA DOB Entry verification"
                                if oppr.fsl_stage=="3":
                                    oppr_dic["phase"]="Aadhar verification"
                                if oppr.fsl_stage =="4":
                                    oppr_dic["phase"]="Profile verification"
                                if oppr.fsl_stage =="5":
                                    oppr_dic["phase"]="Bank verification"
                                if oppr.fsl_stage =="5.1":
                                    oppr_dic["phase"]="Penny verification"                        
                                if oppr.fsl_stage =="6":
                                    oppr_dic["phase"]="Segment verification"
                                if oppr.fsl_stage =="7":
                                    oppr_dic["phase"]="Payment verification"
                                if oppr.fsl_stage =="8":
                                    oppr_dic["phase"]="Nominee verification"
                                if oppr.fsl_stage =="8.1":
                                    oppr_dic["phase"]="Nominee_1 verification"
                                if oppr.fsl_stage =="8.2":
                                    oppr_dic["phase"]="Nominee_2 verification"
                                if oppr.fsl_stage =="8.3":
                                    oppr_dic["phase"]="Nominee_3 verification"
                                if oppr.fsl_stage =="9":
                                    oppr_dic["phase"]="Document verification"
                                if oppr.fsl_stage =="10":
                                    oppr_dic["phase"]="IPV verification"
                                if oppr.fsl_stage =="11":
                                    oppr_dic["phase"]="PDF Download verification"
                                if oppr.fsl_stage =="12":
                                    oppr_dic["phase"]="E-Sign verification"
                                if oppr.fsl_stage =="13":
                                    oppr_dic["phase"]="Complete Email Attached verification"             

                                oppr_list.append(oppr_dic)                             
                                
                    # if frappe.db.exists("Opportunity",{"fsl_referral_rm":emp_email_id }):
                    #     fun = 0
                    #     lead = frappe.get_all("Lead",filters={"fsl_referral_rm":emp_email_id})                 
                            
                    #     for i in lead:
                            
                    #         oppr_dic["mobile"] = i.mobile_no
                    #         oppr_dic["stage"]="Lead Referred"
                            
                    #         if frappe.db.exists("Opportunity",{"fsl_mobile_num":i.mobile_no }):
                                
                    #             oppr=frappe.get_last_doc("Opportunity",filters={"fsl_mobile_num":i.mobile_no })
                                
                    #             oppr_dic["name"] = oppr.customer_name
                    #             oppr_dic["applicationid"]= oppr.fsl_application_id
                    #             oppr_dic["pan"]= oppr.fsl_pan_no   
                    #             oppr_dic["fsl_referral_by"] = emp.name
                    #             oppr_dic["fsl_referral_name"] = emp.employee_name
                    #             oppr_dic["fsl_referral_branch"] = emp.branch
                    #             oppr_dic["fsl_referral_designation"] = emp.designation
                    #             oppr_dic["stage"]="In-Progress"
                    #             if oppr.fsl_stage =="13":
                    #                 oppr_dic["stage"]="Completed"  
                                

                    #             oppr_dic["mobile"] = oppr.fsl_mobile_num
                    #             oppr_dic["assignto"] = oppr.fsl_assign_to
                    #         oppr_list.append(oppr_dic)
                    
                    if fun:
                            frappe.response["message"] = {
                                "Success": 0,                            
                                "message": "Referral not found"
                            }
                    
                    frappe.response["message"] = {
                                    "Success": 1,                            
                                    "data": oppr_list
                                } 

                except Exception as e:
                        frappe.local.response["message"] = {
                            "error": f"An error occurred: {str(e)}"
                        }
    except:
        frappe.response["message"] = {
                            "Success": 0,                            
                            "message":"Employee not found"
                        }  



@frappe.whitelist(allow_guest=True)
def get_rm_ref_lead_details(emp_email_id):
    
    try:
       
        emp=frappe.get_last_doc("Employee",filters={"user_id":emp_email_id}) 
        
        if  emp:  
                
                try:
                    fun = 1
                    oppr_list=[]
                    
                    if frappe.db.exists("Lead",{"fsl_referral_rm":emp.name}):
                        
                        fun = 0
                        lead1 = frappe.get_all("Lead",filters={"fsl_referral_rm":emp.name})       

                        for l in lead1:    
                            oppr_dic={}    
                            i = frappe.get_last_doc("Lead",l)      

                            oppr_dic["name"] = i.first_name 
                            oppr_dic["fsl_referral_by"] = emp.name
                            oppr_dic["fsl_referral_name"] = emp.employee_name
                            oppr_dic["fsl_referral_branch"] = emp.branch
                            oppr_dic["fsl_referral_designation"] = emp.designation                              
                            oppr_dic["mobile"] = i.mobile_no
                            oppr_dic["stage"]= i.status
                            
                            oppr_list.append(oppr_dic)
                            
                        frappe.response["message"] = {
                                    "Success": 1,                            
                                    "data": oppr_list
                                } 
                    if fun:
                            frappe.response["message"] = {
                                "Success": 0,                            
                                "message": "Referral not found"
                            }

                except Exception as e:
                        frappe.local.response["message"] = {
                            "error": f"An error occurred: {str(e)}"
                        }
    except:
        frappe.response["message"] = {
                            "Success": 0,                            
                            "message":"Employee not found"
                        }  
