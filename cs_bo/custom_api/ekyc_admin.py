import frappe
from datetime import datetime, timedelta

@frappe.whitelist(allow_guest= True)
def get_oppr_details(from_date = None, to_date = None, id = None, pan_no = None, mobile_no = None, status = None):
    datas = []
    try:
        filters = {}
        if from_date is None:
            from_date = (datetime.now() - timedelta(days=30)).date()

        if to_date is None:
            to_date = datetime.now().date()

        if id:
            filters["name"] = id

        if from_date:
            filters["creation"] = [">=", from_date]

        if to_date:
            filters["creation"] = ["<=", to_date]

        if pan_no:
            filters["fsl_pan_no"] = pan_no

        if mobile_no:
            filters["fsl_mobile_num"] = mobile_no
        
        # if status is None:           
        #     filters["status"] = "In-Progress"
        
        if status:
            filters["status"] = status


        opprs = frappe.get_all('Opportunity',filters= filters,
                            fields=["name","fsl_pan_no","fsl_stage","fsl_mobile_num","fsl_assign_to","fsl_user_name","status","custom_assign_time"])
        # opprs = frappe.db.sql("""
        #                             SELECT
        #                                 name,
        #                                 fsl_pan_no,
        #                                 fsl_stage,
        #                                 fsl_mobile_num,
        #                                 fsl_assign_to,
        #                                 fsl_user_name,
        #                                 status,
        #                                 custom_assign_time
        #                             FROM
        #                                 `tabOpportunity`;
        #                         """)
       
        for oppr in opprs:
            # oppr = frappe.get_doc("Opportunity",oppr1.name)
            # if oppr.fsl_esigned_completed==1:
            
            data = {
                "opportunity_id": oppr.get("name"),
                "customer_name": oppr.get("fsl_user_name"),
                "fsl_pan_no": oppr.get("fsl_pan_no"),
                "fsl_mobile_num": oppr.get("fsl_mobile_num"),
                "fsl_assign_to": oppr.get("fsl_assign_to"),
                "current phase": get_current_phase(oppr.name),
                "phase": get_phase(oppr.name),
                "stage":oppr.get("fsl_stage"),
                "time": oppr.get("custom_assign_time")
            }
            datas.append(data)

        frappe.local.response["message"] = {
            "success_key": 1,
            "message": "Documents Details Retrieved Successfully",
            "Data": datas,
        }
    # except Exception as e:
    #     frappe.local.response["message"] = {
    #         "error": f"An error occurred: {str(e)}"
    #     }
          
            
    except:
                frappe.local.response["message"] = {
                    "error": "An error occurred or Opportunity Not Found"
                }





@frappe.whitelist(allow_guest= True)
def update_document_details(data):
    datas = {}
    for i in data:
        try:
                       
                oppr=frappe.get_doc('Opportunity',id)

                datas["opportunity_id"]=oppr.opportunity_id
                         
                
                if "customer_name" in i:
                    oppr.customer_name = i["customer_name"]
                    datas["customer_name"]=oppr.customer_name

                if "fsl_pan_no" in i:
                    oppr.fsl_pan_no = i["fsl_pan_no"]
                    datas["fsl_pan_no"]=oppr.fsl_pan_no

                if "fsl_mobile_num" in i:
                    oppr.fsl_mobile_num = i["fsl_mobile_num"]
                    datas["fsl_mobile_num"]= oppr.fsl_mobile_num   

                if "fsl_assign_to" in i:
                    oppr.fsl_assign_to = i["fsl_assign_to"]
                    datas["fsl_assign_to"]= oppr.fsl_assign_to

                if "status" in i:
                    oppr.status = i["status"]
                    datas["status"]= oppr.status
                                
                if "remarks" in i:
                    
                    oppr.remarks = i["remarks"]
                    datas["remarks"]=oppr.remarks
                
                oppr.save()


                frappe.local.response["message"] = {
                    "success_key": 1,
                    "message": "Document Details Updated Successfully",
                    "Data": datas,
                }
        except:
                oppr = frappe.new_doc('Document Details')
                if "opportunity_id" in i:
                    oppr.opportunity_id = i["opportunity_id"]
                    datas["opportunity_id"]=oppr.opportunity_id

                if "customer_name" in i:
                    oppr.customer_name = i["customer_name"]
                    datas["customer_name"]=oppr.customer_name

                if "fsl_pan_no" in i:
                    oppr.fsl_pan_no = i["fsl_pan_no"]
                    datas["fsl_pan_no"]=oppr.fsl_pan_no

                if "fsl_mobile_num" in i:
                    oppr.fsl_mobile_num = i["fsl_mobile_num"]
                    datas["fsl_mobile_num"]= oppr.fsl_mobile_num   

                if "fsl_assign_to" in i:
                    oppr.fsl_assign_to = i["fsl_assign_to"]
                    datas["fsl_assign_to"]= oppr.fsl_assign_to
                
                oppr.save()


                frappe.local.response["message"] = {
                    "success_key": 1,
                    "message": "Document Details Uploaded Successfully",
                    "Data": datas,
                }
                
                


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


@frappe.whitelist(allow_guest= True)
def get_approve_oppr_details(from_date = None, to_date = None):
    datas = []
    try:
        filters = {
            "fsl_esigned_completed": 1
        }
        
        if from_date is None:
            # frappe.errprint("no from")
            from_date = (datetime.now() - timedelta(days=30)).date()

        if to_date is None:
            # frappe.errprint("no to")
            to_date = datetime.now().date()

        if from_date:
            # frappe.errprint("on from")
            filters["creation"] = [">=", from_date]

        if to_date:
            # frappe.errprint("no ti")
            filters["creation"] = ["<=", to_date]
        
        opprs = frappe.get_all('Opportunity', filters=filters , fields=["name","fsl_user_name","fsl_pan_no","fsl_mobile_num","fsl_assign_to","status","custom_assign_time",])
        for oppr in opprs:
            # oppr = frappe.get_doc("Opportunity",oppr1.name)
            user_name = ""
            if oppr.fsl_assign_to:
                user1 = frappe.get_doc("User",oppr.fsl_assign_to)          
                user_name = user1.full_name
                
            # customer = frappe.get_doc("Customer",{"mobile_no":oppr.get("fsl_mobile_num")})
            data = {
                "opportunity_id": oppr.get("name"),
                "customer_name": oppr.get("fsl_user_name"),
                "fsl_pan_no": oppr.get("fsl_pan_no"),
                "fsl_mobile_num": oppr.get("fsl_mobile_num"),
                "fsl_assign_to": oppr.get("fsl_assign_to"),
                "assigned_person_name":user_name,
                "current phase": get_current_phase(oppr.get("name")),
                "phase": get_phase(oppr.name),
                "stage":oppr.get("fsl_stage"),
                "time":oppr.get("custom_assign_time")#get_current_phase(oppr.name)
               
            }
            datas.append(data)

        frappe.local.response["message"] = {
            "success_key": 1,
            "message": "Document Details Retrieved Successfully",
            "Data": datas,
        }
          
            
    except:
                frappe.local.response["message"] = {
                    "error": "An error occurred or Opportunity Not Found"
                }
################ new get_approve_oppr_details  Currently Using End Point in the front end ###

@frappe.whitelist(allow_guest = True)
def new_get_approve_oppr_details(from_date = None, to_date = None, status = None, id = None, pan_no = None, mobile_no = None):
    datas = []
    try:
        filters = {
            "fsl_esigned_completed": 1
        }

        if id :
             filters["name"] = id
        
        if from_date is None:
           
            from_date = (datetime.now() - timedelta(days=30)).date()

        if to_date is None:
           
            to_date = datetime.now().date()

        if from_date or to_date:  
            if from_date and to_date:
                filters["creation"] = [">=", from_date, "<=", to_date]
            elif from_date:
                filters["creation"] = [">=", from_date]
            elif to_date:
                filters["creation"] = ["<=", to_date]

        # if status is None:   
                   
        #     filters["status"] = "In-Progress"
        
        if status:
            filters["status"] = status

        if id :
             filters["name"] = id

        if pan_no:
            filters["fsl_pan_no"] = pan_no

        if mobile_no:
            filters["fsl_mobile_num"] = mobile_no
          
        
        # opprs = frappe.get_all('Opportunity',filters={"fsl_esigned_completed":1,},fields=["name","fsl_user_name","fsl_referral_by","fsl_referral_type","fsl_pan_no","fsl_mobile_num","fsl_assign_to","status","custom_assign_time","modified","fsl_email_id","fsl_stage"])
        opprs = frappe.get_all('Opportunity',
                       filters = filters,
                       fields=["name", "fsl_user_name", "creation","fsl_referral_by", "fsl_referral_type", "fsl_pan_no", "fsl_mobile_num", "fsl_assign_to", "status", "custom_assign_time", "modified", "fsl_email_id", "fsl_stage"])

        
        for oppr in opprs:
            # oppr = frappe.get_doc("Opportunity",oppr1.name)
            user_name = ""
            if oppr.fsl_assign_to:
                user1 = frappe.get_doc("User",oppr.fsl_assign_to)          
                user_name = user1.full_name
               
            # customer = frappe.get_doc("Customer",{"mobile_no":oppr.get("fsl_mobile_num")})
            data = {
                "opportunity_id": oppr.get("name"),
                "customer_name": oppr.get("fsl_user_name"),
                "modified": oppr.get("modified"),
                "fsl_pan_no": oppr.get("fsl_pan_no"),
                "fsl_mobile_num": oppr.get("fsl_mobile_num"),
                "fsl_assign_to": oppr.get("fsl_assign_to"),
                "assigned_person_name":user_name,
                "current phase": get_current_phase(oppr.get("name")),
                "phase": get_phase(oppr.name),
                "stage":oppr.get("fsl_stage"),
                "time":oppr.get("custom_assign_time"),#get_current_phase(oppr.name)
                "fsl_mode_of_application": oppr.get("fsl_mode_of_application"),
                "status": oppr.get("status"),
                "email_id": oppr.get("fsl_email_id"),
                "reference_id": oppr.get("fsl_referral_by"),
            }
            if frappe.db.exists("Employee",oppr.fsl_referral_by):
            # if oppr.get("fsl_referral_type") == "Employee":
                emp = frappe.get_doc("Employee",oppr.fsl_referral_by)  

                data["referral_name"] = emp.employee_name
                data["designation"] = emp.designation
                data["branch"] = emp.branch
            
            if frappe.db.exists("Customer",oppr.fsl_referral_by):
            # if oppr.get("fsl_referral_type") == "Customer":
                emp = frappe.get_doc("Customer",oppr.fsl_referral_by)  

                data["referral_name"] = emp.customer_name
                data["branch"] = emp.fsl_branch

            datas.append(data)

        frappe.local.response["message"] = {
            "success_key": 1,
            "message": "Document Details Retrieved Successfully",
            "Data": datas,
        }
          
            
    except:
                frappe.local.response["message"] = {
                    "error": "An error occurred or Opportunity Not Found"
                }

########## NEW #############

@frappe.whitelist(allow_guest = True)
def get_new_opportunity_details(from_date = None, to_date = None):
    datas = []
    try:
        if from_date is None:
            from_date = (datetime.now() - timedelta(days=30)).date()

        if to_date is None:
            to_date = datetime.now().date()
        # opprs = frappe.get_all('Opportunity',fields=["name","fsl_pan_no","fsl_stage","fsl_mobile_num","fsl_assign_to","fsl_user_name","status","custom_assign_time"])
        opprs = frappe.db.sql("""
                                    SELECT
                                        name,
                                        fsl_pan_no,
                                        fsl_stage,
                                        fsl_mobile_num,
                                        fsl_assign_to,
                                        fsl_user_name,
                                        status,
                                        custom_assign_time
                                    FROM
                                        `tabOpportunity`
                                    WHERE
                                        creation BETWEEN %s AND %s;
                                """,(from_date, to_date))
        
        for oppr in opprs:
            # oppr = frappe.get_doc("Opportunity",oppr1.name)
            # if oppr.fsl_esigned_completed==1:
                
            data = {
               "opportunity_id": oppr[0],  # accessing the first element of the tuple (name)
                "customer_name": oppr[5],  # accessing the sixth element of the tuple (fsl_user_name)
                "fsl_pan_no": oppr[1],  # accessing the second element of the tuple (fsl_pan_no)
                "fsl_mobile_num": oppr[3],  # accessing the fourth element of the tuple (fsl_mobile_num)
                "fsl_assign_to": oppr[4],  # accessing the fifth element of the tuple (fsl_assign_to)
                "current_phase": get_current_phase(oppr[0]),  # assuming get_current_phase takes an opportunity_id as an argument
                "phase": get_phase(oppr[0]),  # assuming get_phase takes an opportunity_id as an argument
                "stage": oppr[2],  # accessing the third element of the tuple (fsl_stage)
                "time": oppr[7]  # accessing the eighth element of the tuple (custom_assign_time)
            }
            datas.append(data)

        frappe.local.response["message"] = {
            "success_key": 1,
            "message": "Document Details Retrieved Successfully",
            "Data": datas,
        }
    except:
                frappe.local.response["message"] = {
                    "error": "An error occurred or Opportunity Not Found"
                }
          
            
   
@frappe.whitelist(allow_guest= True)
def get_new_approve_oppr_details(from_date = None, to_date = None):
    datas = []
    try:
        if from_date is None:
            from_date = (datetime.now() - timedelta(days=30)).date()

        if to_date is None:
            to_date = datetime.now().date()

        opprs = frappe.db.sql("""
            SELECT
                name,
                fsl_user_name,
                fsl_pan_no,
                fsl_mobile_num,
                fsl_assign_to,
                status,
                fsl_stage,
                custom_assign_time
            FROM
                `tabOpportunity`
            WHERE
                fsl_esigned_completed = 1
                AND creation BETWEEN %s AND %s;
        """, (from_date, to_date))
        
        for oppr in opprs:
            # oppr = frappe.get_doc("Opportunity",oppr1.name)
            user_name = ""
            if oppr[4]:
                user1 = frappe.get_doc("User",oppr[4])          
                user_name = user1.full_name
                
            # customer = frappe.get_doc("Customer",{"mobile_no":oppr.get("fsl_mobile_num")})
            data = {
                "opportunity_id": oppr[0],
                "customer_name": oppr[1],
                "fsl_pan_no": oppr[2],
                "fsl_mobile_num": oppr[3],
                "fsl_assign_to": oppr[4],
                "status" : oppr[5],
                "assigned_person_name":user_name,
                "current phase": get_current_phase(oppr[0]),
                "phase": get_phase(oppr[0]),
                "stage": oppr[6],
                "time": oppr[7]#get_current_phase(oppr.name)
            }
            datas.append(data)

        frappe.local.response["message"] = {
            "success_key": 1,
            "message": "Document Details Retrieved Successfully",
            "Data": datas,
        }


          
            
    except:
                frappe.local.response["message"] = {
                    "error": "An error occurred or Opportunity Not Found"
                }
    # except Exception as e:
    #     frappe.local.response["message"] = {
    #         "error": f"An error occurred: {str(e)}"
    #     }