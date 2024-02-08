import frappe

@frappe.whitelist()
def get_opportunity_Bank_details(name):
    data = []
    try:
        custom = frappe.get_last_doc("Opportunity",filters={'name':name})

        custom_dic = {}
        custom_dic["fsl_acc_no"] = custom.fsl_acc_no
        custom_dic["fsl_verify_acc_number"] = custom.fsl_verify_acc_number
        custom_dic["fsl_acc_hname"] = custom.fsl_acc_hname
        custom_dic["fsl_bank_name"] = custom.fsl_bank_name
        custom_dic["fsl_bank_branch"] = custom.fsl_bank_branch
        custom_dic["fsl_bank_address"] = custom.fsl_bank_address
        custom_dic["fsl_bank_pincode"] = custom.fsl_bank_pincode
        custom_dic["fsl_bank_ifsc"] = custom.fsl_bank_ifsc
        custom_dic["fsl_bank_micr"] = custom.fsl_bank_micr
        custom_dic["fsl_bank_response"] = custom.fsl_bank_response
        custom_dic["fsl_bank_tnx_response"] = custom.fsl_bank_tnx_response
        custom_dic["fsl_penny_confirm"] = custom.fsl_penny_confirm
        custom_dic["fsl_penny_response_code"] = custom.fsl_penny_response_code
        custom_dic["fsl_stage"] = custom.fsl_stage
        
        # data.append(custom_dic)
        
        frappe.local.response["message"] = {
            "success_key": 1,
            "data": custom_dic
        }
        
    except:
        frappe.response["message"] = {
            "error":"This Session User can't Access This Customer"
        }


@frappe.whitelist()
def update_bank_details(data):
    try:
        table = data.get("bank_details")
        success, message = 0, "Opportunity not found"
        
        oppr = frappe.get_last_doc("Opportunity", filters={'name': table.get("name")})
        
        if oppr:
            custom_dic = {}
            if "fsl_acc_no" in table:
                oppr.fsl_acc_no = table["fsl_acc_no"]
                frappe.db.set_value("Opportunity",oppr.name,"fsl_acc_no",table["fsl_acc_no"])
                custom_dic["Account Number"] = oppr.fsl_acc_no

            if "fsl_verify_acc_number" in table:
                oppr.fsl_verify_acc_number = table["fsl_verify_acc_number"]
                frappe.db.set_value("Opportunity",oppr.name,"fsl_verify_acc_number",table["fsl_verify_acc_number"])
                custom_dic["Verify Account Number"] = oppr.fsl_verify_acc_number

            if "fsl_acc_hname" in table:
                oppr.fsl_acc_hname = table["fsl_acc_hname"]
                frappe.db.set_value("Opportunity",oppr.name,"fsl_acc_hname",table["fsl_acc_hname"])
                custom_dic["Account Holder Name"] = oppr.fsl_acc_hname
                
            if "fsl_bank_name" in table:
                oppr.fsl_bank_name = table["fsl_bank_name"]
                frappe.db.set_value("Opportunity",oppr.name,"fsl_bank_name",table["fsl_bank_name"])
                custom_dic["Bank Name"] = oppr.fsl_bank_name
              ###  
            if "fsl_bank_branch" in table:
                oppr.fsl_bank_branch = table["fsl_bank_branch"]
                frappe.db.set_value("Opportunity",oppr.name,"fsl_bank_branch",table["fsl_bank_branch"])
                custom_dic["fsl_bank_branch"] = oppr.fsl_bank_branch

            if "fsl_bank_address" in table:
                oppr.fsl_bank_address = table["fsl_bank_address"]
                frappe.db.set_value("Opportunity",oppr.name,"fsl_bank_address",table["fsl_bank_address"])
                custom_dic["Bank Address"] = oppr.fsl_bank_address

            if "fsl_bank_pincode" in table:
                oppr.fsl_bank_pincode = table["fsl_bank_pincode"]
                frappe.db.set_value("Opportunity",oppr.name,"fsl_bank_pincode",table["fsl_bank_pincode"])
                custom_dic["Bank Pincode"] = oppr.fsl_bank_pincode

            if "fsl_bank_ifsc" in table:
                oppr.fsl_bank_ifsc = table["fsl_bank_ifsc"]
                frappe.db.set_value("Opportunity",oppr.name,"fsl_bank_ifsc",table["fsl_bank_ifsc"])
                custom_dic["Bank IFSC"] = oppr.fsl_bank_ifsc

            if "fsl_bank_micr" in table:
                oppr.fsl_bank_micr = table["fsl_bank_micr"]
                frappe.db.set_value("Opportunity",oppr.name,"fsl_bank_micr",table["fsl_bank_micr"])
                custom_dic["Bank MICR"] = oppr.fsl_bank_micr

            if "fsl_bank_response" in table:
                oppr.fsl_bank_response = table["fsl_bank_response"]
                frappe.db.set_value("Opportunity",oppr.name,"fsl_bank_response",table["fsl_bank_response"])
                custom_dic["Bank Response"] = oppr.fsl_bank_response

            if "fsl_bank_tnx_response" in table:
                oppr.fsl_bank_tnx_response = table["fsl_bank_tnx_response"]
                frappe.db.set_value("Opportunity",oppr.name,"fsl_bank_tnx_response",table["fsl_bank_tnx_response"])
                custom_dic["Bank Transaction Response"] = oppr.fsl_bank_tnx_response

            if "fsl_penny_confirm" in table:
                oppr.fsl_penny_confirm = table["fsl_penny_confirm"]
                frappe.db.set_value("Opportunity",oppr.name,"fsl_penny_confirm",table["fsl_penny_confirm"])
                custom_dic["Penny Confirm"] = oppr.fsl_penny_confirm
            

            if "fsl_penny_response_code" in table:
                # custom_list=[]
                
                for i in table["fsl_penny_response_code"]:
                    frappe.errprint(i["account_number"])
                    # if i.account_number == i["account_number"]:
                    oppr.append("fsl_penny_response_code",
                        {
                        "account_number":i["account_number"],
                        "ifsc":i["ifsc"],
                        "account_name":i["account_name"],
                        "bank_response":i["bank_response"],
                        "bank_txn_status":i["bank_txn_status"],
                        "request_id":i["request_id"],
                        "status_code":i["status_code"]
                    })
            frappe.db.commit()
            custom_dic = {}
            custom_dic["fsl_acc_no"] = oppr.fsl_acc_no
            custom_dic["fsl_verify_acc_number"] = oppr.fsl_verify_acc_number
            custom_dic["fsl_acc_hname"] = oppr.fsl_acc_hname
            custom_dic["fsl_bank_name"] = oppr.fsl_bank_name
            custom_dic["fsl_bank_address"] = oppr.fsl_bank_address
            custom_dic["fsl_bank_pincode"] = oppr.fsl_bank_pincode
            custom_dic["fsl_bank_ifsc"] = oppr.fsl_bank_ifsc
            custom_dic["fsl_bank_micr"] = oppr.fsl_bank_micr
            custom_dic["fsl_bank_response"] = oppr.fsl_bank_response
            custom_dic["fsl_bank_tnx_response"] = oppr.fsl_bank_tnx_response
            custom_dic["fsl_penny_confirm"] = oppr.fsl_penny_confirm
            custom_dic["fsl_stage"] = oppr.fsl_stage
            custom_dic["fsl_penny_response_code"] = oppr.fsl_penny_response_code
            
                
                
                # oppr.fsl_penny_confirm = table["fsl_penny_response_code"]
                # frappe.db.set_value("Opportunity",oppr.name,"fsl_penny_response_code",table["fsl_penny_response_code"])
                # custom_dic["Penny Response Json"] = oppr.fsl_penny_response_json
            

            # frappe.db.commit()
            
            
            # custom_dic["Stage"] = oppr.fsl_stage
        
            # success, message = 1, "Opportunity Bank Details Updated.."
        
        frappe.response["message"] = {
            "Success": success,
            "message": message,
            "Opportunity Id " : oppr.name,
            # "Stage" :oppr.fsl_stage,
            "data":custom_dic
        }
    except Exception as e:
            frappe.response["message"] = {
                "error" : f"An error occurred while processing the request: {str(e)}"
             }

@frappe.whitelist()
def post_bank_details(data):
    
    table = data.get("bank_details")
    
    Success = 0
    oppr = frappe.get_last_doc("Opportunity", filters={'name': table["name"]})
    
    if oppr:
        custom_dic = {}
        Success = 1
        if "fsl_acc_no" in table:
            oppr.fsl_acc_no = table["fsl_acc_no"]
            custom_dic["Account Number"] = oppr.fsl_acc_no

        if "fsl_verify_acc_number" in table:
            oppr.fsl_verify_acc_number = table["fsl_verify_acc_number"]
            custom_dic["Verify Account Number"] = oppr.fsl_verify_acc_number

        if "fsl_acc_hname" in table:
            oppr.fsl_acc_hname = table["fsl_acc_hname"]
            custom_dic["Account Holder Name"] = oppr.fsl_acc_hname
            
        if "fsl_bank_name" in table:
            oppr.fsl_bank_name = table["fsl_bank_name"]
            custom_dic["Bank Name"] = oppr.fsl_bank_name
            
        if "fsl_bank_branch" in table:
            oppr.fsl_bank_branch = table["fsl_bank_branch"]
            custom_dic["fsl_bank_branch"] = oppr.fsl_bank_branch

        if "fsl_bank_address" in table:
            oppr.fsl_bank_address = table["fsl_bank_address"]
            custom_dic["Bank Address"] = oppr.fsl_bank_address

        if "fsl_bank_pincode" in table:
            oppr.fsl_bank_pincode = table["fsl_bank_pincode"]
            custom_dic["Bank Pincode"] = oppr.fsl_bank_pincode

        if "fsl_bank_ifsc" in table:
            oppr.fsl_bank_ifsc = table["fsl_bank_ifsc"]
            custom_dic["Bank IFSC"] = oppr.fsl_bank_ifsc

        if "fsl_bank_micr" in table:
            oppr.fsl_bank_micr = table["fsl_bank_micr"]
            custom_dic["Bank MICR"] = oppr.fsl_bank_micr

        if "fsl_bank_response" in table:
            oppr.fsl_bank_response = table["fsl_bank_response"]
            custom_dic["Bank Response"] = oppr.fsl_bank_response

        if "fsl_bank_tnx_response" in table:
            oppr.fsl_bank_tnx_response = table["fsl_bank_tnx_response"]
            custom_dic["Bank Transaction Response"] = oppr.fsl_bank_tnx_response

        if "fsl_penny_confirm" in table:
            oppr.fsl_penny_confirm = table["fsl_penny_confirm"]
            custom_dic["Penny Confirm"] = oppr.fsl_penny_confirm

        if "fsl_penny_response_code" in table:
            oppr.append("Penny Drop",{
                "account_number":table["account_number"],
                "ifsc":table["ifsc"],
                "account_name":table["account_name"],
                "bank_response":table["bank_response"],
                "bank_tnx_status":table["bank_tnx_status"],
                "request_id":table["request_id"],
                "status_code":table["status_code"],
            })

        oppr.save()
          
        custom_dic["Stage"] = oppr.fsl_stage
        
        frappe.response["message"] = {
            "Success": Success,
            "message": "Opportunity Bank Details Updated.",
            "Opportunity Id " : oppr.name,
            "Stage" :custom_dic
        }


    else:
        frappe.response["message"] = {
            "Success": Success,
            "message": "Opportunity not found"
        }

@frappe.whitelist()
def delete_bank_details(name):    
    Success = 0
    oppr = frappe.get_last_doc("Opportunity", filters={'name': name})
    
    if oppr:
        Success = 1
        oppr.fsl_acc_no = ""
        oppr.fsl_verify_acc_number = ""
        oppr.fsl_acc_hname = ""
        oppr.fsl_bank_name = ""
        oppr.fsl_bank_address = ""
        oppr.fsl_bank_branch = ""
        oppr.fsl_bank_pincode = "".capitalize
        oppr.fsl_bank_ifsc = ""
        oppr.fsl_bank_micr = ""
        oppr.fsl_bank_tnx_response = ""
        oppr.fsl_penny_confirm = ""
        oppr.save()

        frappe.response["message"] = {
            "Success": Success,
            "message": "Opportunity Bank Details Deleted.",
            "Opportunity Id " : oppr.name,
            "Stage" :oppr.fsl_stage
        }


    else:
        frappe.response["message"] = {
            "Success": Success,
            "message": "Opportunity not found"
        }