import frappe

@frappe.whitelist(allow_guest=True)
def update_referral(fsl_referral_type,id,fsl_referral_person_type=None,fsl_referral_person=None):
    try:
        doc1 = frappe.get_doc("Opportunity",id)
        if fsl_referral_type:
            if fsl_referral_type=="Referral":
                if fsl_referral_person_type:
                    if fsl_referral_person_type == "Employee":
                        try:
                            employee = frappe.get_doc("Employee",fsl_referral_person)
                            if employee:
                                frappe.db.set_value('Opportunity', id, 'fsl_branch', employee.branch)
                            frappe.db.set_value('Opportunity', id, 'fsl_referral_type', fsl_referral_type)
                            frappe.db.set_value('Opportunity', id, 'fsl_referral_person_type', fsl_referral_person_type)
                            frappe.db.set_value('Opportunity', id, 'fsl_referral_by', fsl_referral_person)
                            frappe.db.commit()
                            # doc1.fsl_branch = employee.branch

                            frappe.local.response["message"] = {
                                "success_key": 1,
                                "Data": {
                                    "id":id,
                                    "fsl_referral_type":doc1.fsl_referral_type,
                                    "fsl_branch":doc1.fsl_branch,
                                    "fsl_referral_person_type":doc1.fsl_referral_person_type,
                                    "fsl_referral_person":doc1.fsl_referral_by

                                }
                            }
                        except:

                            frappe.local.response["message"] = {
                                "success_key": 0,
                                "message": "Employee is Not Exists"
                            }
                    else:
                        if fsl_referral_person_type == "Customer":
                            frappe.db.set_value('Opportunity', id, 'fsl_referral_type', fsl_referral_type)
                            frappe.db.set_value('Opportunity', id, 'fsl_referral_person_type', fsl_referral_person_type)
                            frappe.db.set_value('Opportunity', id, 'fsl_referral_by', fsl_referral_person)
                            frappe.db.commit()
                            frappe.local.response["message"] = {
                                "success_key": 1,
                                "Data": {
                                    "id":id,
                                    "fsl_referral_type":doc1.fsl_referral_type,
                                    # "fsl_branch":doc1.fsl_branch,
                                    "fsl_referral_person_type":doc1.fsl_referral_person_type,
                                    "fsl_referral_person":doc1.fsl_referral_by

                                }
                            }
                        else:

                            frappe.local.response["message"] = {
                                "success_key": 0,
                                "message":"no records found check fsl_referral_person_type, it should one of the Employee or Customer"
                            }
                else:
                    frappe.local.response["message"] = {
                                "success_key": 0,
                                "message":"fsl_referral_person_type is Mandatory"
                            }
            else:
                frappe.db.set_value('Opportunity', id, 'fsl_referral_type', fsl_referral_type)
                frappe.db.commit()
                frappe.local.response["message"] = {
                    "success_key": 1,
                    "Data": {
                        "id":id,
                        "fsl_referral_type":doc1.fsl_referral_type
                    }
                }
        else:
            frappe.local.response["message"] = {
                "success_key": 0,
                "message":"fsl_referral_type is Mandatory"
            }
    except:
        frappe.local.response["message"] = {
            "success_key": 0,
            "message":"Opportunity Not Found"
        }