import frappe

@frappe.whitelist()
def ekyc_reset(id):
    
    oppor1 = frappe.get_doc("Opportunity",id)
    oppor1.fsl_stage = 1.1
    
    oppor1.set("fsl_nominee_table", [])
    oppor1.save()
    frappe.db.commit()


    fsl_stage_table = oppor1.get("fsl_stage_table")
    entries_to_keep = [entry for entry in fsl_stage_table if entry.stages in {"0.5", "1"}]

    # Remove entries that are not "0.5" or "1"
    entries_to_remove = [entry for entry in fsl_stage_table if entry not in entries_to_keep]

    for entry in entries_to_remove:
        frappe.errprint(f"Deleting entry with stages: {entry.stages}")
        fsl_stage_table.remove(entry)

    if entries_to_remove:
        frappe.errprint("Deleted entries")
    # Save oppor1 with the updated fsl_stage_table
        oppor1.save()

   
    # for entry in oppor1.get("fsl_stage_table"):
    #     frappe.errprint(entry.stages)
    #     frappe.errprint(entry)
    #     if entry.stages == "0.5" or entry.stages == "1":
    #         frappe.errprint(entry.stages)
    #         pass
    #     else:
    #         frappe.errprint(entry.stages)
    #         oppor1.get("fsl_stage_table").remove(entry)
    #         frappe.errprint("deleted")
    #         oppor1.save()
    #         frappe.db.commit()
    
    oppor1.save()
   
   
    try:
        customer_profile = frappe.get_last_doc("Customer Profile",filters={'fsl_from_opportunity': id})
        if customer_profile:
            frappe.errprint(customer_profile.name)
            frappe.delete_doc('Customer Profile', customer_profile.name)
            frappe.db.commit()
        else:
            frappe.errprint("else")
    except :
        pass
    
    try :
        documents= frappe.get_all('Document Details', filters={"opportunity_id":id})
        for document1 in documents:
            frappe.errprint(document1.name)
            frappe.delete_doc('Document Details', document1.name)
            frappe.db.commit()
    except :
        pass
     
    try :
            ts = frappe.get_last_doc('Trading Scheme', filters={"opportunity_id": id})
            frappe.errprint(ts.name)
            frappe.delete_doc('Trading Scheme', ts.name)
            # frappe.errprint(ts.name)
            frappe.db.commit()
    except :
            pass
    
    try:
        address1 = frappe.get_all("Address",filters={"fsl_from_opportunity": id})
        for address in address1:
            frappe.errprint(address.name)
            frappe.delete_doc('Address', address.name)
            frappe.db.commit()   
    except : 
        pass
    
# ####### Resource API
    oppor1.customer_name = None
    oppor1.fsl_pan_status_code = None
    oppor1.fsl_dob = None
    oppor1.fsl_referral_by = None
    oppor1.fsl_mode_of_application = None
    oppor1.fsl_verify_acc_number = None
    oppor1.fsl_bank_response = None
    oppor1.fsl_payment_status = None
    oppor1.status = "In-Progress"
    frappe.db.commit()
    # frappe.errprint("555")
    
####### Stage 3
    oppor1.fsl_first_name = None
    oppor1.fsl_pan_no = None
    oppor1.fsl_middle_name = None
    oppor1.fsl_last_name = None
    oppor1.fsl_user_name = None
    oppor1.fsl_aadharpan_link = None
    oppor1.fsl_pan_confirm = None
    oppor1.save()
    frappe.db.commit()

####### Bank Details
    oppor1.fsl_acc_no = None
    oppor1.fsl_acc_hname = None
    oppor1.fsl_bank_name = None
    oppor1.fsl_bank_address = None
    oppor1.fsl_bank_pincode = None
    oppor1.fsl_bank_ifsc = None
    oppor1.fsl_bank_micr = None
    oppor1.fsl_bank_tnx_response = None
    oppor1.fsl_penny_confirm = None
    oppor1.save()
    frappe.db.commit()
    
####### Stage 6
    oppor1.fsl_category = None
    oppor1.fsl_currency_derivatives = None
    oppor1.fsl_currency_derivatives_type = None
    oppor1.fsl_consent = None
    oppor1.fsl_equity_derivative = None
    oppor1.fsl_equity_cash = None
    oppor1.fsl_mf_phy_or_dig = None
    oppor1.fsl_mutual_funds = None
    oppor1.fsl_slb = None
    oppor1.save()
    frappe.db.commit()
    
######## Stage 8

    oppor1.fsl_amount = None
    oppor1.fsl_amount_due= None
    oppor1.fsl_amount_paid= None
    oppor1.fsl_attempts= None
    oppor1.fsl_entity= None
    oppor1.fsl_order_id= None
    oppor1.fsl_payment_id= None
    oppor1.fsl_razorpay_order_id= None
    oppor1.fsl_razorpay_payment_id= None
    oppor1.fsl_razorpay_signature= None
    oppor1.fsl_receipt= None
    oppor1.fsl_reference_id= None
    oppor1.fsl_verify_url= None
    oppor1.fsl_notes= None
    oppor1.fsl_application_id= None
    oppor1.currency= None
    oppor1.save()
    frappe.db.commit()
    
######### ekyc Update

    oppor1.fsl_esiged_name = None  
    oppor1.customer_name = None
    oppor1.fsl_esigned_completed = None
    oppor1.fsl_pdf_generated = None
    oppor1.save()
    frappe.db.commit()
    
######## opportuity

    oppor1.fsl_active_status = None
    oppor1.fsl_legal_action_statement = None
    oppor1.fsl_kra_response_date = None
    oppor1.save()
    oppor1.fsl_annual_income = None
    oppor1.fsl_user_name = None
    oppor1.fsl_application_id = None
    oppor1.fsl_fatca = None
    oppor1.fsl_gender = None
    oppor1.fsl_legal_action = None
    oppor1.fsl_marital_status = None
    oppor1.fsl_net_worth = None
    oppor1.fsl_net_worth_date = None
    oppor1.fsl_occu = None
    oppor1.fsl_political_exposure = None
    oppor1.fsl_stand_ins_one = None
    oppor1.fsl_standard_ins_two = None
    oppor1.fsl_stand_ins_three = None
    oppor1.fsl_standard_ins_four = None
    oppor1.fsl_stand_ins_five = None
    oppor1.fsl_standard_ins_six = None
    oppor1.fsl_stand_ins_seven = None
    oppor1.fsl_standard_ins_eight = None
    oppor1.fsl_stand_ins_nine = None
    oppor1.fsl_stand_ins_ten = None
    oppor1.save()
    frappe.db.commit()
    
######## opportunity referral

    oppor1.fsl_branch = None
    oppor1.fsl_referral_type = None
    oppor1.fsl_referral_person_type = None
    # oppor1.fsl_referral_person = None
    oppor1.save()
    frappe.db.commit()
    
    frappe.local.response["message"] = {
            "success_key": 1,
            "message":"Opportunity Successfully Reset."     
        }