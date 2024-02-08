import frappe

@frappe.whitelist()
def get_segment_details(id):
    data = []

    try:
        segment= frappe.get_doc("Opportunity",id)
        if segment:
            segment_dic= {}
            segment_dic["fsl_category"] = segment.fsl_category
            segment_dic["fsl_currency_derivatives"]= segment.fsl_currency_derivatives
            segment_dic["fsl_currency_derivatives_type"] = segment.fsl_currency_derivatives_type
            segment_dic["fsl_consent"] = segment.fsl_consent
            segment_dic["fsl_equity_derivative"] = segment.fsl_equity_derivative
            segment_dic["fsl_equity_cash"] = segment.fsl_equity_cash
            segment_dic["fsl_mf_phy_or_dig"] = segment.fsl_mf_phy_or_dig
            segment_dic["fsl_mutual_funds"] = segment.fsl_mutual_funds
            segment_dic["fsl_slb"] = segment.fsl_slb
            
            # data.append(segment_dic)
        
        frappe.local.response["message"] = {
            "success_key": 1,
            "data": segment_dic
        }
        
    except:
        frappe.response["message"] = {
            "error":"This Session User can't Access This Customer"
        }
        
    
@frappe.whitelist()
def update_segment_details(data):  
    for table in data:
    # table = data.get("opportunity")
        Success = 0
        oppr = frappe.get_doc("Opportunity",table["id"])
        if oppr:
            Success=1
            if "fsl_category" in table:
                oppr.fsl_category=table["fsl_category"]
            if "fsl_currency_derivatives" in table:
                oppr.fsl_currency_derivatives= table["fsl_currency_derivatives"]
            if "fsl_currency_derivatives_type" in table:
                oppr.fsl_currency_derivatives_type= table["fsl_currency_derivatives_type"] 
            if "fsl_consent" in table:
                oppr.fsl_consent = table["fsl_consent"]
            if "fsl_equity_derivative" in table:
                oppr.fsl_equity_derivative = table["fsl_equity_derivative"]
            if "fsl_equity_cash" in table:
                oppr.fsl_equity_cash= table["fsl_equity_cash"]
            if "fsl_mf_phy_or_dig" in table:
                oppr.fsl_mf_phy_or_dig= table["fsl_mf_phy_or_dig"]
            if "fsl_mutual_funds" in table:
                oppr.fsl_mutual_funds= table["fsl_mutual_funds"]
            if "fsl_slb" in table:
                oppr.fsl_slb = table["fsl_slb"]  
            oppr.save()   

            segment_dic = {}
            segment_dic["fsl_category"] = oppr.fsl_category
            segment_dic["fsl_currency_derivatives"] = oppr.fsl_currency_derivatives
            segment_dic["fsl_currency_derivatives_type"] = oppr.fsl_currency_derivatives_type
            segment_dic["fsl_consent"] = oppr.fsl_consent
            segment_dic["fsl_equity_derivative"] = oppr.fsl_equity_derivative
            segment_dic["fsl_equity_cash"] = oppr.fsl_equity_cash
            segment_dic["fsl_mf_phy_or_dig"] = oppr.fsl_mf_phy_or_dig
            segment_dic["fsl_mutual_funds"] = oppr.fsl_mutual_funds
            segment_dic["fsl_slb"] = oppr.fsl_slb    

            frappe.response["message"] = {
                "success_key": 1,
                "id":oppr.name,
                "stage":oppr.fsl_stage,
                "message":"Opportunity Segment Details Updated"
            }

        else:
            frappe.response["message"]={
                "Success":Success,
                "message":"Opportunity not found"
            }
