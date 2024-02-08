import frappe

@frappe.whitelist()
def get_payment_details(id):
    data = []
    
    try:
        payment = frappe.get_doc("Opportunity",id)
        if payment:


            payment_dic = {}
            payment_dic["fsl_amount"] = payment.fsl_amount
            payment_dic["fsl_amount_due"] = payment.fsl_amount_due
            payment_dic["fsl_amount_paid"] = payment.fsl_amount_paid
            payment_dic["fsl_attempts"] = payment.fsl_attempts
            payment_dic["fsl_entity"] = payment.fsl_entity
            payment_dic["fsl_order_id"] = payment.fsl_order_id
            payment_dic["fsl_payment_id"] = payment.fsl_payment_id
            payment_dic["fsl_razorpay_order_id"] = payment.fsl_razorpay_order_id
            payment_dic["fsl_razorpay_payment_id"] = payment.fsl_razorpay_payment_id
            payment_dic["fsl_razorpay_signature"] = payment.fsl_razorpay_signature
            payment_dic["fsl_payment_status"] = payment.fsl_payment_status
            payment_dic["fsl_receipt"] = payment.fsl_receipt
            payment_dic["fsl_reference_id"] = payment.fsl_reference_id
            payment_dic["fsl_verify_url"] = payment.fsl_verify_url
            payment_dic["status"] = payment.status
            payment_dic["fsl_notes"] = payment.fsl_notes
            payment_dic["fsl_application_id"] = payment.fsl_application_id
            payment_dic["currency"] = payment.currency
                    
        # data.append(payment_dic)
        
        frappe.local.response["message"] = {
            "success_key": 1,
            "data":payment_dic
        }
        
    except:
        frappe.response["message"] = {
            "error":"This Session User can't Access This Customer"
        }

@frappe.whitelist()
def update_Opportunity_payment_details(data):

    for table in data:
            Success = 0
            oppr = frappe.get_doc("Opportunity",table["id"]) 
            if oppr:
                Success = 1
                if "fsl_amount" in table:
                    oppr.fsl_amount = table["fsl_amount"]
                if "fsl_amount_due" in table:
                    oppr.fsl_amount_due = table["fsl_amount_due"]
                if "fsl_amount_paid" in table:
                    oppr.fsl_amount_paid = table["fsl_amount_paid"]  
                if "fsl_attempts"in table:
                    oppr.fsl_attempts = table["fsl_attempts"]
                if "fsl_entity"in table:
                    oppr.fsl_entity = table["fsl_entity"]
                if "fsl_order_id"in table:
                    oppr.fsl_order_id = table["fsl_order_id"]
                if "fsl_payment_id"in table:
                    oppr.fsl_payment_id = table["fsl_payment_id"]
                if "fsl_razorpay_order_id" in table:
                    oppr.fsl_razorpay_order_id = table["fsl_razorpay_order_id"]
                if "fsl_razorpay_payment_id"in table:
                    oppr.fsl_razorpay_payment_id = table["fsl_razorpay_payment_id"]
                if "fsl_razorpay_signature" in table:
                    oppr.fsl_razorpay_signature = table["fsl_razorpay_signature"]
                if "fsl_payment_status" in table:
                    oppr.fsl_payment_status = table["fsl_payment_status"]
                if "fsl_receipt"in table:
                    oppr.fsl_receipt = table["fsl_receipt"]
                if "fsl_reference_id" in table:
                    oppr.fsl_reference_id = table["fsl_reference_id"]
                if "fsl_verify_url" in table:
                    oppr.fsl_verify_url= table["fsl_verify_url"]
                if "status" in table:
                    oppr.status= table["status"]
                if "fsl_notes" in table:
                    oppr.fsl_notes= table["fsl_notes"]
                if "fsl_application_id" in table:
                    oppr.fsl_application_id= table["fsl_application_id"]
                if "currency" in table:
                    oppr.currency= table["currency"]
                oppr.save()

                payment_dic = {}
                payment_dic["fsl_amount"] =oppr.fsl_amount
                payment_dic["fsl_amount_due"] = oppr.fsl_amount_due
                payment_dic["fsl_amount_paid"] = oppr.fsl_amount_paid
                payment_dic["fsl_attempts"] = oppr.fsl_attempts
                payment_dic["fsl_entity"] = oppr.fsl_entity
                payment_dic["fsl_order_id"] = oppr.fsl_order_id
                payment_dic["fsl_payment_id"] = oppr.fsl_payment_id
                payment_dic["fsl_razorpay_order_id"] = oppr.fsl_razorpay_order_id
                payment_dic["fsl_razorpay_payment_id"] = oppr.fsl_razorpay_payment_id
                payment_dic["fsl_razorpay_signature"] = oppr.fsl_razorpay_signature
                payment_dic["fsl_payment_status"] = oppr.fsl_payment_status
                payment_dic["fsl_receipt"] = oppr.fsl_receipt
                payment_dic["fsl_reference_id"] = oppr.fsl_reference_id
                payment_dic["fsl_verify_url"] = oppr.fsl_verify_url
                payment_dic["status"] = oppr.status
                payment_dic["fsl_notes"] = oppr.fsl_notes
                payment_dic["fsl_application_id"] = oppr.fsl_application_id
                payment_dic["currency"] = oppr.currency



                frappe.response["message"] = {
                    "Success": Success,
                    "id":oppr.name,
                    "stage":oppr.fsl_stage,
                    "message": "Opportunity Payment Details Updated.",
                    "data": payment_dic
                }


            else:
                frappe.response["message"] = {
                    "Success": Success,
                    "message": "Opportunity not found"
                }


