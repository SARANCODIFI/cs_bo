import frappe

@frappe.whitelist()
def update_opportunity(id,fsl_esiged_name,customer_name,fsl_stage,status,fsl_esigned_completed,fsl_pdf_generated):
    
    oppr = frappe.get_doc('Opportunity', id)
    frappe.errprint(oppr)   
    if fsl_esiged_name:
        oppr.fsl_esiged_name = fsl_esiged_name
        
    if customer_name :
        oppr.customer_name = customer_name
        
    if fsl_stage:
        oppr.fsl_stage = fsl_stage
        
    if status:
        oppr.status = status
        
    if fsl_esigned_completed:
        oppr.fsl_esigned_completed = fsl_esigned_completed
        
    if fsl_pdf_generated:
        oppr.fsl_pdf_generated = fsl_pdf_generated
        
    oppr.save()
    
    frappe.response["message"] = {
        "Success" : 1,
        "data": {
            "id" : id,
            "fsl_esiged_name" : oppr.fsl_esiged_name,
            "customer_name" : oppr.customer_name,
            "fsl_stage" : oppr.fsl_stage,
            "status" : status,
            "fsl_esigned_completed" : oppr.fsl_esigned_completed,
            "fsl_pdf_generated" : oppr.fsl_pdf_generated
        }
    }