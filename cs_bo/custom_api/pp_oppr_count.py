import frappe

@frappe.whitelist(allow_guest=True)
def oppr_count(from_date=None, to_date=None, zone=None, branch=None, region_code=None):
    try:
        result_data = []
        response_msg = {"status": "Not Ok", "opprs_count": "No data found"}

        if from_date is None:
            from_date = frappe.utils.today()
        if to_date is None:
            to_date = frappe.utils.add_days(frappe.utils.today(), 1)

        # oppr_filters = [['creation', 'between', [from_date, to_date]]]

        if zone or region_code or branch:
            if branch == "online":
                response_msg["status"] = "Ok"
                dormant_count = frappe.db.count("Opportunity", filters = {'status': 'Dormant', 
                                                                            'modified': ['between', [from_date, to_date]],
                                                                            
                                                                            } )    
                pdf_gen_count = frappe.db.count("Opportunity",  filters={'status': 'Pdf Generated',
                                                                            'modified': ['between', [from_date, to_date]]
                                                                            
                                                                            })
                in_active_count = frappe.db.count("Opportunity",  filters={'status': 'Inactive',
                                                                            'modified': ['between', [from_date, to_date]]
                                                                            
                                                                            })        
                in_progress_count = frappe.db.count("Opportunity", filters = {'status': 'In-Progress', 
                                                                                'modified': ['between', [from_date, to_date]],
                                                                                
                                                                                } )
                completed_count = frappe.db.count("Opportunity",  filters = {'status': 'Completed',
                                                                                'modified': ['between', [from_date, to_date]],
                                                                                
                                                                                    } )
                approved_count = frappe.db.count("Opportunity",  filters = {'status': 'Approved',
                                                                            'modified': ['between', [from_date, to_date]],
                                                                            
                                                                            } )
                rejected_count = frappe.db.count("Opportunity",  filters = {'status': 'Rejected',
                                                                            'modified': ['between', [from_date, to_date]],
                                                                            
                                                                            } )
                active_count = frappe.db.count("Opportunity",  filters={'status': 'Active',
                                                                            'modified': ['between', [from_date, to_date]]
                                                                            
                                                                            })
                assigned_count = frappe.db.count("Opportunity",  filters={'status': 'Assigned',
                                                                            'modified': ['between', [from_date, to_date]]
                                                                            
                                                                            })
            
                result_data.append({
                    'dormant_count': dormant_count,
                    'in_progress_count': in_progress_count,
                    'completed_count' : completed_count,
                    'approved_count' : approved_count,
                    'rejected_count' : rejected_count,
                    'active_count' : active_count,
                    'in_active_count' : in_active_count,
                    'pdf_gen_count' : pdf_gen_count,
                    'assigned_count' : assigned_count
                })
                response_msg["opprs_count"] = result_data

                
            else:
                branches_filter = None

                if zone:
                    branches_filter = {"fsl_zone": zone}
                elif region_code:
                    branches_filter = {"fsl_region_code": region_code}
                elif branch:
                    branches_filter = {"name": branch}
                
                branches_in_filter = frappe.get_all("Branch", filters=branches_filter, pluck="name")

                employee_in_branch = frappe.get_all("Employee", filters={"branch": ["in", branches_in_filter]}, pluck="name")
                
                if not branches_in_filter or not employee_in_branch:                    
                    return {"status": "Not Ok", "opprs_count":"No branches found for the specified criteria"}
                    
                else :
                    response_msg["status"] = "Ok"

                    dormant_count = frappe.db.count("Opportunity", filters = {'status': 'Dormant', 
                                                                            'modified': ['between', [from_date, to_date]],
                                                                            
                                                                            } )    
                    pdf_gen_count = frappe.db.count("Opportunity",  filters={'status': 'Pdf Generated',
                                                                                'modified': ['between', [from_date, to_date]]
                                                                                
                                                                                })
                    in_active_count = frappe.db.count("Opportunity",  filters={'status': 'Inactive',
                                                                                'modified': ['between', [from_date, to_date]]
                                                                                
                                                                                })        
                    in_progress_count = frappe.db.count("Opportunity", filters = {'status': 'In-Progress', 
                                                                                    'modified': ['between', [from_date, to_date]],
                                                                                    
                                                                                    } )
                    completed_count = frappe.db.count("Opportunity",  filters = {'status': 'Completed',
                                                                                    'modified': ['between', [from_date, to_date]],
                                                                                    
                                                                                        } )
                    approved_count = frappe.db.count("Opportunity",  filters = {'status': 'Approved',
                                                                                'modified': ['between', [from_date, to_date]],
                                                                                
                                                                                } )
                    rejected_count = frappe.db.count("Opportunity",  filters = {'status': 'Rejected',
                                                                                'modified': ['between', [from_date, to_date]],
                                                                                
                                                                                } )
                    active_count = frappe.db.count("Opportunity",  filters={'status': 'Active',
                                                                                'modified': ['between', [from_date, to_date]]
                                                                                
                                                                                })
                    assigned_count = frappe.db.count("Opportunity",  filters={'status': 'Assigned',
                                                                                'modified': ['between', [from_date, to_date]]
                                                                                
                                                                                })
                
                    result_data.append({
                        'dormant_count': dormant_count,
                        'in_progress_count': in_progress_count,
                        'completed_count' : completed_count,
                        'approved_count' : approved_count,
                        'rejected_count' : rejected_count,
                        'active_count' : active_count,
                        'in_active_count' : in_active_count,
                        'pdf_gen_count' : pdf_gen_count,
                        'assigned_count' : assigned_count
                    })
                    response_msg["opprs_count"] = result_data
                    
        if response_msg["status"] == "Not Ok" :
            # frappe.errprint('hiii'+from_date+to_date)
            response_msg["status"] = "Ok"
            
            dormant_count = frappe.db.count("Opportunity", filters = {'status': 'Dormant', 
                                                                            'modified': ['between', [from_date, to_date]],
                                                                            
                                                                            } )    
            pdf_gen_count = frappe.db.count("Opportunity",  filters={'status': 'Pdf Generated',
                                                                        'modified': ['between', [from_date, to_date]]
                                                                        
                                                                        })
            in_active_count = frappe.db.count("Opportunity",  filters={'status': 'Inactive',
                                                                        'modified': ['between', [from_date, to_date]]
                                                                        
                                                                        })        
            in_progress_count = frappe.db.count("Opportunity", filters = {'status': 'In-Progress', 
                                                                            'modified': ['between', [from_date, to_date]],
                                                                            
                                                                            } )
            completed_count = frappe.db.count("Opportunity",  filters = {'status': 'Completed',
                                                                            'modified': ['between', [from_date, to_date]],
                                                                            
                                                                                } )
            approved_count = frappe.db.count("Opportunity",  filters = {'status': 'Approved',
                                                                        'modified': ['between', [from_date, to_date]],
                                                                        
                                                                        } )
            rejected_count = frappe.db.count("Opportunity",  filters = {'status': 'Rejected',
                                                                        'modified': ['between', [from_date, to_date]],
                                                                        
                                                                        } )
            active_count = frappe.db.count("Opportunity",  filters={'status': 'Active',
                                                                        'modified': ['between', [from_date, to_date]]
                                                                        
                                                                        })
            assigned_count = frappe.db.count("Opportunity",  filters={'status': 'Assigned',
                                                                        'modified': ['between', [from_date, to_date]]
                                                                        
                                                                        })

            # frappe.errprint('hiii567'+ ''+ str(active_count))
            result_data.append({
                'dormant_count': dormant_count,
                'in_progress_count': in_progress_count,
                'completed_count' : completed_count,
                'approved_count' : approved_count,
                'rejected_count' : rejected_count,
                'active_count' : active_count,
                'in_active_count' : in_active_count,
                'pdf_gen_count' : pdf_gen_count,
                'assigned_count' : assigned_count
                
            })

            response_msg["opprs_count"] = result_data
        return response_msg


    except Exception as e:
        return {"Error": f"An error occurred while processing the request:{e}"}