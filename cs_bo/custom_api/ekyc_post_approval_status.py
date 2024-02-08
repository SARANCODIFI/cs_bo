import frappe

@frappe.whitelist(allow_guest=True)
def update_document_details(id,status,document_type,remarks=None,nominee_no=None,attachment_type = None):
    try:    
        user1 = frappe.session.user
        # frappe.errprint(user1)
        user = frappe.get_doc('User',user1)
        # frappe.errprint(user)
        oppr=frappe.get_last_doc('Opportunity',filters={"name":id})
        
        # user_roles = frappe.get_roles(user1)
        # frappe.errprint(oppr.name)
        # frappe.errprint(oppr.opportunity_from)
        # frappe.errprint(oppr.fsl_assign_to)
        # frappe.errprint(document_type)
        # Check if 'ekyc admin' role is in the user's roles
        # frappe.errprint("ifff")
        # if 'EKYC Admin' in user_roles:
            # for i in user.roles:
            # frappe.errprint("if")
            
            # if i.role == 1 :   
           
            #     if i.role == "ekyc" :
        frappe.errprint(oppr.fsl_assign_to)
        if user1 == oppr.fsl_assign_to:
                fun = 0
                # frappe.errprint("fun1")
        
                if oppr.fsl_esigned_completed==1:
                    # frappe.errprint("pan in")
            
                    if document_type == "Pan":
                        # frappe.errprint("fun2")
                        fun = 1
                        oppr=frappe.get_doc('Opportunity',id)   

                        if status == "Approved":
                            # frappe.errprint("Approved")
                            frappe.db.set_value('Opportunity', id, 'fsl_pan_status', status)
                            # oppr.fsl_pan_status = status
                            frappe.db.commit()
                            # frappe.errprint("commit")
                            # oppr.save()
                            frappe.local.response["message"] = {
                            "success_key": 1,
                            "message":"This Document Status Updated",
                            "id" : id,
                            "status" : oppr.fsl_pan_status,
                            "User-name" : user.username,
                            "mail-id" : user.name,

                            }
                            
                        if status == "Rejected":
                            frappe.db.commit()
                            fun = 1
                            if  remarks is not None:
                                frappe.db.set_value('Opportunity', id, 'fsl_pan_remark', remarks)
                                frappe.db.set_value('Opportunity', id, 'fsl_pan_status', status)
                                # oppr.fsl_pan_status = status
                                # oppr.fsl_pan_remark = remarks
                                # oppr.save()
                                frappe.db.commit()
                                
                                frappe.local.response["message"] = {
                                    "success_key": 1,
                                    "message":"This Document Status Updated",
                                    "id" : id,
                                    "status" : oppr.fsl_pan_status,
                                    "remarks" : oppr.fsl_pan_remark,
                                    "User-name" : user.username,
                                    "mail-id" : user.name,

                                    }
                                

                            else:
                                frappe.local.response["message"] = {
                                "success_key": 0,
                                "message":"Remarks Is Required For 'Rejected' Status",
                                }
                        if status == "Reset":
                            frappe.db.commit()
                            frappe.db.set_value('Opportunity', id, 'fsl_pan_status',None)
                            frappe.db.set_value('Opportunity', id, 'fsl_pan_remark', None)
                            
                            frappe.db.commit()
                            # oppr.save()
                            frappe.local.response["message"] = {
                            "success_key": 1,
                            "message":"This Pan Status Updated",
                            "id" : id,
                            "status" : oppr.fsl_pan_status,
                            "remarks":oppr.fsl_pan_remark,
                            "User-name" : user.username,
                            "mail-id" : user.name,

                            }
                            
            ################# BAnk ##########################
                    if document_type == "Bank":
                        frappe.db.commit()
                        fun = 1
                        oppr=frappe.get_doc('Opportunity',id)   
                        frappe.local.response["message"] = {
                            "success_key": 1,
                            "message":"This Document Status Updated",
                            "id" : id,
                            "status" : oppr.fsl_bank_status,
                            "User-name" : user.username,
                            "mail-id" : user.name,

                            }
                        if status == "Approved":
                            frappe.db.commit()
                                # frappe.db.set_value('Opportunity', id, 'fsl_bank_status',remarks)
                            frappe.db.set_value('Opportunity', id, 'fsl_bank_status',status)
                            # oppr.fsl_bank_status = status
                            frappe.db.commit()
                            # oppr.save()
                            frappe.local.response["message"] = {
                            "success_key": 1,
                            "message":"This Documents Status Updated",
                            "id" : id,
                            "status" : oppr.fsl_bank_status,
                            "User-name" : user.username,
                            "mail-id" : user.name,

                            }
                        

                        if status == "Rejected":
                            if  remarks is not None: 
                                
                                frappe.db.set_value('Opportunity', id, 'fsl_bank_remark',remarks)
                                frappe.db.set_value('Opportunity', id, 'fsl_bank_status',status)
                                # oppr.fsl_bank_status = status
                                # oppr.fsl_bank_remark = remarks
                                # oppr.save()
                                frappe.db.commit()
                                frappe.local.response["message"] = {
                                    "success_key": 1,
                                    "message":"This Document Status Updated",
                                    "id" : id,
                                    "status" : oppr.fsl_bank_status,
                                    "remarks" : oppr.fsl_bank_remark,
                                    "User-name" : user.username,
                                    "mail-id" : user.name,

                                    }
                            else:
                                frappe.local.response["message"] = {
                                "success_key": 0,
                                "message":"Remarks Is Required For 'Rejected' Status",
                                }
                        if status == "Reset":   
                            # frappe.db.commit()                 
                            frappe.db.set_value('Opportunity', id, 'fsl_bank_status',None)
                            frappe.db.set_value('Opportunity', id, 'fsl_bank_remark',None)                                
                            frappe.db.commit()
                            # oppr.save()
                            frappe.local.response["message"] = {
                            "success_key": 1,
                            "message":"This Bank Status Updated",
                            "id" : id,
                            "status" :oppr.fsl_bank_status,
                            "remark" :oppr.fsl_bank_remark,
                            "User-name" : user.username,
                            "mail-id" : user.name,

                            }
                            
            ####################### segment ##############################
                    if document_type == "Segment":
                            
                            fun = 1
                            oppr=frappe.get_doc('Opportunity',id)   
                            frappe.db.commit()
                            if status == "Approved":
                                # frappe.db.commit()
                                # frappe.db.set_value('Opportunity', id, 'fsl_segment_remark',remarks)
                                frappe.db.set_value('Opportunity', id, 'fsl_segment_status',status)
                                # oppr.fsl_segment_status = status
                                frappe.db.commit()
                                # oppr.save()
                                frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"This Document Status Updated",
                                "id" : id,
                                "status" : oppr.fsl_segment_status,
                                "User-name" : user.username,
                                "mail-id" : user.name,

                                }
                            
                            if status == "Rejected":
                                frappe.db.commit()
                                if  remarks is not None:
                                    # frappe.db.commit()
                                    frappe.db.set_value('Opportunity', id, 'fsl_segment_remark',remarks)
                                    frappe.db.set_value('Opportunity', id, 'fsl_segment_status',status)
                                    # oppr.fsl_segment_status = status
                                    # oppr.fsl_segment_remark = remarks
                                    # oppr.save()
                                    frappe.db.commit()
                                    frappe.local.response["message"] = {
                                        "success_key": 1,
                                        "message":"This Document Status Updated",
                                        "id" : id,
                                        "status" : oppr.fsl_segment_status,
                                        "remarks" : oppr.fsl_segment_remark,
                                        "User-name" : user.username,
                                        "mail-id" : user.name,

                                        }
                                    

                                else:
                                    frappe.local.response["message"] = {
                                    "success_key": 0,
                                    "message":"Remarks Is Required For 'Rejected' Status",
                                    }
                            if status == "Reset":
                                # frappe.db.commit()
                                frappe.db.set_value('Opportunity', id, 'fsl_segment_status',None)
                                frappe.db.set_value('Opportunity', id, 'fsl_segment_remark',None)
                                # frappe.db.set_value('Opportunity', id, 'fsl_segment_status',None)                                    
                                frappe.db.commit()
                                # oppr.save()
                                frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"This Document Status Updated",
                                "id" : id,
                                "status" :oppr.fsl_segment_status,
                                "remarks" : oppr.fsl_segment_remark,
                                "User-name" : user.username,
                                "mail-id" : user.name,

                                }

            ################## Address #####################
                    if document_type == "Address":
                            fun = 1
                            oppr=frappe.get_last_doc('Address',filters={"fsl_from_opportunity":id})  

                            if status == "Approved":
                                # frappe.db.commit()
                                # frappe.db.set_value('Address', oppr.name, 'fsl_address_remarks',remarks)
                                frappe.db.set_value('Address', oppr.name, 'fsl_address_status',status)
                                # oppr.fsl_address_status = status
                                frappe.db.commit()
                                # oppr.save()
                                frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"This Document Status Updated",
                                "id" : id,
                                "status" : oppr.fsl_address_status,
                                "User-name" : user.username,
                                "mail-id" : user.name,

                                }
                                
                            if status == "Rejected":
                                if  remarks is not None:
                                    # frappe.db.commit()
                                    frappe.db.set_value('Address', oppr.name, 'fsl_address_remarks',remarks)
                                    frappe.db.set_value('Address', oppr.name, 'fsl_address_status',status)
                                    # oppr.fsl_address_status = status
                                    # oppr.fsl_address_remarks = remarks
                                    # oppr.save()
                                    frappe.db.commit()
                                    frappe.local.response["message"] = {
                                        "success_key": 1,
                                        "message":"This Document Status Updated",
                                        "id" : id,
                                        "status" : oppr.fsl_address_status,
                                        "remarks" : oppr.fsl_address_remarks,
                                        "User-name" : user.username,
                                        "mail-id" : user.name,

                                        }
                                else:
                                    frappe.local.response["message"] = {
                                    "success_key": 0,
                                    "message":"Remarks Is Required For 'Rejected' Status",
                                    }

                            if status == "Reset":
                                frappe.db.commit()
                                frappe.db.set_value('Address', oppr.name, 'fsl_address_status',None)
                                frappe.db.set_value('Address', oppr.name, 'fsl_address_remarks',None)
                                
                                frappe.db.commit()
                                frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"This Document Status Updated",
                                "id" : id,
                                "status" : oppr.fsl_address_status,
                                "remarks" : oppr.fsl_address_remarks,
                                "User-name" : user.username,
                                "mail-id" : user.name,

                                }


                                    

                                
                            
            ################## profile ###########

                    if document_type == "Profile":
                            fun = 1
                            oppr = frappe.get_last_doc('Customer Profile',filters={"fsl_from_opportunity":id})

                            if status == "Approved":
                                frappe.db.commit()
                                    # frappe.db.set_value('Customer Profile', oppr.name, 'profile_remarks',remarks)
                                frappe.db.set_value('Customer Profile', oppr.name, 'profile_status',status)
                                oppr.profile_status = status
                                frappe.db.commit()
                                # oppr.save()
                                frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"This Document Status Updated",
                                "id" : id,
                                "status" : oppr.profile_status,
                                "User-name" : user.username,
                                "mail-id" : user.name,

                                }
                                
                            if status == "Rejected":
                                if  remarks is not None:
                                    frappe.db.commit()
                                    frappe.db.set_value('Customer Profile', oppr.name, 'profile_remarks',remarks)
                                    frappe.db.set_value('Customer Profile', oppr.name, 'profile_status',status)
                                    oppr.profile_status = status
                                    oppr.profile_remarks = remarks
                                    # oppr.save()
                                    frappe.db.commit()
                                    frappe.local.response["message"] = {
                                        "success_key": 1,
                                        "message":"This Document Status Updated",
                                        "id" : id,
                                        "status" : oppr.profile_status,
                                        "remarks" : oppr.profile_remarks,
                                        "User-name" : user.username,
                                        "mail-id" : user.name,

                                        }
                                    

                                else:
                                    frappe.local.response["message"] = {
                                    "success_key": 0,
                                    "message":"Remarks Is Required For 'Rejected' Status",
                                    }
                            if status == "Reset":
                                frappe.db.commit()
                                frappe.db.set_value('Customer Profile', oppr.name, 'profile_status',None)
                                frappe.db.set_value('Customer Profile', oppr.name, 'profile_remarks',None)
                                oppr.profile_status = None
                                frappe.db.commit()
                                frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"This Document Status Updated",
                                "id" : id,
                                "status" : oppr.profile_status,
                                "remarks" : oppr.profile_remarks,
                                "User-name" : user.username,
                                "mail-id" : user.name,

                                }

            ##################### Document #####################
                    if document_type == "Document":
                            fun = 1
                            oppr = frappe.get_last_doc('Document Details',filters={"opportunity_id":id,"document_type" : attachment_type})
                            # frappe.errprint(oppr.name)
                            if status == "Approved":
                                frappe.db.commit()
                                frappe.db.set_value('Document Details', oppr.name, 'document_remarks',remarks)
                                frappe.db.set_value('Document Details', oppr.name, 'document_status',status)
                                oppr.document_status = status
                                frappe.db.commit()
                                # oppr.save()
                                frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"This Document Status Updated",
                                "id" : id,
                                "status" : oppr.document_status,
                                "User-name" : user.username,
                                "mail-id" : user.name,

                                }
                                
                            if status == "Rejected":
                                if  remarks is not None:
                                    frappe.db.commit()
                                    frappe.db.set_value('Document Details', oppr.name, 'document_remarks',remarks)
                                    frappe.db.set_value('Document Details', oppr.name, 'document_status',status)
                                    
                                    oppr.document_status = status
                                    oppr.document_remarks = remarks
                                    # oppr.save()
                                    frappe.db.commit()
                                    frappe.local.response["message"] = {
                                        "success_key": 1,
                                        "message":"This Document Status Updated",
                                        "id" : id,
                                        "status" : oppr.document_status,
                                        "remarks" : oppr.document_remarks,
                                        "User-name" : user.username,
                                        "mail-id" : user.name,

                                        }
                                    

                                else:
                                    frappe.local.response["message"] = {
                                    "success_key": 0,
                                    "message":"Remarks Is Required For 'Rejected' Status",
                                    }
                            if status == "Reset":
                                frappe.db.commit()
                                frappe.db.set_value('Document Details', oppr.name, 'document_status',None)
                                frappe.db.set_value('Document Details', oppr.name, 'document_remarks',None)
                                # frappe.db.set_value('Address', oppr.name, 'fsl_document_status',None)                                    
                                frappe.db.commit()
                                frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"This Document Status Updated",
                                "id" : id,
                                "status" : oppr.fsl_document_status,
                                "remarks" : oppr.document_remarks,
                                "User-name" : user.username,
                                "mail-id" : user.name,

                                }
            #################### ipv ##########################
                    if document_type == "IPV":
                        # frappe.errprint("IPV")
                        fun = 1
                        oppr = frappe.get_last_doc('Document Details',filters={"opportunity_id":id,"document_type" : "IPV"})
                        frappe.errprint(oppr.name)
                        if status == "Approved":
                            frappe.db.commit()
                            frappe.db.set_value('Document Details', oppr.name, 'document_remarks',None)
                            frappe.db.set_value('Document Details', oppr.name, 'status',status)
                            oppr.status = status
                            # oppr.ipv_status = status
                            frappe.db.commit()
                            # oppr.save()
                            frappe.local.response["message"] = {
                            "success_key": 1,
                            "message":"This Document Status Updated",
                            "id" : id,
                            "status" : oppr.status,
                            "User-name" : user.username,
                            "mail-id" : user.name,

                            }
                            
                        if status == "Rejected":
                            if  remarks is not None:
                                frappe.db.commit()
                                frappe.db.set_value('Document Details', oppr.name, 'document_remarks',remarks)
                                frappe.db.set_value('Document Details', oppr.name, 'status',status)
                                oppr.status = status
                                # oppr.ipv_status = status
                                oppr.document_remarks = remarks
                                # oppr.save()
                                frappe.db.commit()
                                frappe.local.response["message"] = {
                                    "success_key": 1,
                                    "message":"This Document Status Updated",
                                    "id" : id,
                                    "status" : oppr.status,
                                    "remarks" : oppr.document_remarks,
                                    "User-name" : user.username,
                                    "mail-id" : user.name,

                                    }
                                

                            else:
                                frappe.local.response["message"] = {
                                "success_key": 0,
                                "message":"Remarks Is Required For 'Rejected' Status",
                                }
                        if status == "Reset":
                            frappe.db.commit()
                            frappe.db.set_value('Document Details', oppr.name, 'status',None)
                            frappe.db.set_value('Document Details', oppr.name, 'document_remarks',None)        
                            frappe.db.commit()
                            frappe.local.response["message"] = {
                            "success_key": 1,
                            "message":"This Document Status Updated",
                            "id" : id,
                            "status" : oppr.status,
                            "remarks" : oppr.document_remarks,
                            "User-name" : user.username,
                            "mail-id" : user.name,

                            }

            ###################### E-Sign #######################
                    if document_type == "E-Sign":
                            fun = 1
                            oppr= frappe.get_last_doc('Document Details', filters={"opportunity_id":id,"document_type" :"ESIGN_DOCUMENT"})
            
                            if status == "Approved":
                                frappe.db.commit()
                                frappe.db.set_value('Document Details', oppr.name, 'document_remarks',None)
                                frappe.db.set_value('Document Details', oppr.name, 'status',status)
                                # oppr.e_sign_status = status
                                frappe.db.commit()
                                # oppr.save()
                                frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"This Document Status Updated",
                                "id" : id,
                                "status" : oppr.status,
                                "User-name" : user.username,
                                "mail-id" : user.name,

                                }
                                
                            if status == "Rejected":

                                if  remarks is not None:
                                    frappe.db.commit()
                                    frappe.db.set_value('Document Details', oppr.name, 'document_remarks',remarks)
                                    frappe.db.set_value('Document Details', oppr.name, 'status',status)
                                    # oppr.e_sign_status = status
                                    # oppr.e_sign_remarks = remarks
                                    # oppr.save()
                                    frappe.db.commit()
                                    frappe.local.response["message"] = {
                                        "success_key": 1,
                                        "message":"This Document Status Updated",
                                        "id" : id,
                                        "status" : oppr.status,
                                        "remarks" : oppr.document_remarks,
                                        "User-name" : user.username,
                                        "mail-id" : user.name,

                                        }
                                    

                                else:
                                    frappe.local.response["message"] = {
                                    "success_key": 0,
                                    "message":"Remarks Is Required For 'Rejected' Status",
                                    }
                            if status == "Reset":
                                frappe.db.commit()
                                frappe.db.set_value('Document Details', oppr.name, 'document_remarks',None)
                                frappe.db.set_value('Document Details', oppr.name, 'status',None)
                                # frappe.db.set_value('Address', oppr.name, 'fsl_e_sign_status',None)
                                
                                frappe.db.commit()
                                frappe.local.response["message"] = {
                                "success_key": 1,
                                "message":"This Document Status Updated",
                                "id" : id,
                                "status" : oppr.status,
                                "remarks" : oppr.document_remarks,
                                "User-name" : user.username,
                                "mail-id" : user.name,

                                }
            ###################### Nominee ######################
                    if document_type == "Nominee":
                        fun = 1
                        success = 0
                        frappe.db.commit()
                        oppr=frappe.get_doc('Opportunity',id)
                        
                        for i in oppr.fsl_nominee_table:
                            # frappe.errprint(nominee_no)
                            # frappe.errprint(i.nominee_number)
                            if i.nominee_number == nominee_no:
                                # frappe.errprint("in if")
                                # frappe.errprint(i.nominee_number)
                                doc = frappe.get_doc("Opportunity",id)
                                success = 1
                                if status == "Approved":  
                                    i.nominee_status = status
                                    frappe.db.set_value('Opportunity Nominee Details',i.name, 'nominee_status',status)
                                    # frappe.db.set_value("Opportunity", id, "fsl_nominee_table", {"nominee_no": int(nominee_no)}, "nominee_status", status)
                                    # frappe.get_doc('Opportunity',id).for_each('Opportunity Nominee Details', lambda d: d.set('nominee_status', status)).save()
                                    # frappe.db.set_value(,"Opportunity Nominee Details","Opportunity","fsl_nominee_table",id,"nominee_status",status,index)
                                    # i.nominee_status = "Approved"
                                    # frappe.set_value("Opportunity Nominee Details",doc.name,nominee_status,status)
                                    frappe.db.commit()
                                    oppr.save()
                                    frappe.local.response["message"] = {
                                    "success_key": 1,
                                    "message":"This Document Status Updated",
                                    "id" : id,
                                    "status" : i.nominee_status,
                                    "User-name" : user.username,
                                    "mail-id" : user.name,

                                    }
                                

                                if status == "Rejected":
                                    if  remarks is not None:
                                        frappe.db.set_value('Opportunity Nominee Details',i.name, 'nominee_status',status)
                                        frappe.db.set_value('Opportunity Nominee Details',i.name, 'nominee_remarks',remarks)
                                        # frappe.set_value("Opportunity Nominee Details",doc.name,nominee_status,status)
                                        # frappe.set_value("Opportunity Nominee Details",doc.name,nominee_remarks,remarks)
                                        # frappe.db.set_value(,"Nominee Details","Opportunity","fsl_nominee_table",id,"nominee_status",status,index)
                                        # frappe.db.set_value(,"Nominee Details","Opportunity","fsl_nominee_table",id,"nominee_remarks",remarks,index)
                                        i.nominee_status = "Rejected"
                                        i.nominee_remarks = remarks
                                        
                                        frappe.db.commit()
                                        oppr.save()
                                        frappe.local.response["message"] = {
                                            "success_key": 1,
                                            "message":"This Document Status Updated",
                                            "id" : id,
                                            "status" : i.nominee_status,
                                            "remarks" : i.nominee_remarks,
                                            "User-name" : user.username,
                                            "mail-id" : user.name,

                                            }
                                        

                                    else:
                                        frappe.local.response["message"] = {
                                        "success_key": 0,
                                        "message":"Remarks Is Required For 'Rejected' Status",
                                        }
                                if status == "Reset":  
                                    i.nominee_status = None
                                    frappe.db.set_value('Opportunity Nominee Details',i.name, 'nominee_status',None)
                                    frappe.db.set_value('Opportunity Nominee Details',i.name, 'nominee_remarks',None)
                                    frappe.db.commit()
                                    
                                    frappe.local.response["message"] = {
                                    "success_key": 1,
                                    "message":"This Document Status Updated",
                                    "mail-id" : user.name,
                                    "User-name" : user.username,
                                    "status" : i.nominee_status,
                                    "remarks" : i.nominee_remarks
                                    }
                                
                        if success == 0:
                            frappe.local.response["message"] = {
                                        "success_key": 0,
                                        "message":"Nominee not exists",
                                        }
                            
                else : 
            
                    frappe.local.response["message"] = {
                    "success_key": 0,
                    "message":"This Customer Is Not Completed E-signed",
                    }
                    
                if fun == 0:
                    frappe.local.response["message"] = {
                    "success_key": 0,
                    "message":"Check The Document Type",
                    }
                    
        else : 
            # frappe.errprint(user_roles)
            frappe.local.response["message"] = {
            "success_key": 0,
            "message":"This User Has No permission",
            }
        # else :  
        #     frappe.errprint("1")   
        #     frappe.local.response["message"] = {
        #     "success_key": 0,
        #     "message":"This User Has No Permissions",
        #     }                  
            
    except Exception as e:
       
        frappe.local.response["message"] = {
            "error": "Document Not Found"
        }