import frappe

@frappe.whitelist(allow_guest= True)
def customer_ticket_count(ucc):

    cus_exists = frappe.db.exists("Customer",ucc)
    if cus_exists:
        customer = frappe.get_doc("Customer",ucc)
       
        total = frappe.db.count('HD Ticket', {'customer': ucc})
        open_count = frappe.db.count('HD Ticket', {'status': 'Open','customer': ucc})
        in_progress_statuses = ['Resolved', 'In-Progress', 'Replied']
        cancelled_statuses = ['Closed', 'Closed - Duplicate', 'Cancel']

        in_progress_count = frappe.db.count('HD Ticket', {'status': ['in', in_progress_statuses], 'customer': ucc})

        cancelled_count = frappe.db.count('HD Ticket', {'status': ['in', cancelled_statuses], 'customer': ucc})

        frappe.local.response["message"] = {
            "success_key": 1,
            "data": {
                "ucc": customer.fsl_ucc_code,
                "customer_name": customer.customer_name,
                "branch_id": customer.fsl_branch_id,
                "total": total,
                "open_count": open_count,
                "in_progress_count": in_progress_count,
                "cancelled_count": cancelled_count
            }
        }
    else :
        frappe.local.response["message"] = {
            "success_key": 0,
            "data": {
                "error": "Customer Not Exists",
            }
        }


@frappe.whitelist(allow_guest= True)
def employee_ticket_count(emp_email_id):

    emp_exists = frappe.db.exists("Employee",{"user_id":emp_email_id})
    if emp_exists:
        emp = frappe.get_last_doc("Employee",filters = {"user_id":emp_email_id})
       
        total = frappe.db.count('HD Ticket', {'owner': emp_email_id})
        open_count = frappe.db.count('HD Ticket', {'status': 'Open','owner': emp_email_id})
        in_progress_statuses = ['Resolved', 'In-Progress', 'Replied']
        cancelled_statuses = ['Closed', 'Closed - Duplicate', 'Cancel']

        in_progress_count = frappe.db.count('HD Ticket', {'status': ['in', in_progress_statuses], 'owner': emp_email_id})

        cancelled_count = frappe.db.count('HD Ticket', {'status': ['in', cancelled_statuses], 'owner': emp_email_id})

        frappe.local.response["message"] = {
            "success_key": 1,
            "data": {
                "employee_id": emp.name,
                "employee_name": emp.employee_name,
                "branch_id": emp.branch,
                "total": total,
                "open_count": open_count,
                "in_progress_count": in_progress_count,
                "cancelled_count": cancelled_count
            }
        }
    else :
        frappe.local.response["message"] = {
            "success_key": 0,
            "data": {
                "error": "Employee Not Exists",
            }
        }

@frappe.whitelist(allow_guest= True)
def branch_ticket_count(branch_id):

    branch_exists = frappe.db.exists("Branch",branch_id)
    if branch_exists:
        branch = frappe.get_doc("Branch",branch_id)
        
        total = frappe.db.count('HD Ticket', {'fsl_branch_id': branch_id})
        open_count = frappe.db.count('HD Ticket', {'status': 'Open','fsl_branch_id': branch_id})
        in_progress_statuses = ['Resolved', 'In-Progress', 'Replied']
        cancelled_statuses = ['Closed', 'Closed - Duplicate', 'Cancel']

        in_progress_count = frappe.db.count('HD Ticket', {'status': ['in', in_progress_statuses], 'fsl_branch_id': branch_id})

        cancelled_count = frappe.db.count('HD Ticket', {'status': ['in', cancelled_statuses], 'fsl_branch_id': branch_id})

        frappe.local.response["message"] = {
            "success_key": 1,
            "data": {
                "branch_id": branch.name,
                "branch_name": branch.fsl_branch_name,
                "total": total,
                "open_count": open_count,
                "in_progress_count": in_progress_count,
                "cancelled_count": cancelled_count
            }
        }
    else :
        frappe.local.response["message"] = {
            "success_key": 0,
            "data": {
                "error": "Branch Not Exists",
            }
        }


@frappe.whitelist(allow_guest= True)
def department_ticket_count(department):

    depart = ["INST","PAL","PCG","RETAIL"]
    if department in depart:
        dep_branch = frappe.db.get_list('Branch',filters={'fsl_fo_front_code': department},fields={'name'})
        dep_branch_names = [item['name'] for item in dep_branch]

        total = frappe.db.count('HD Ticket', {'fsl_branch_id': ['in',dep_branch_names]})
        open_count = frappe.db.count('HD Ticket', {'status': 'Open','fsl_branch_id': ['in',dep_branch_names]})
       
        in_progress_statuses = ['Resolved', 'In-Progress', 'Replied']
        cancelled_statuses = ['Closed', 'Closed - Duplicate', 'Cancel']

        in_progress_count = frappe.db.count('HD Ticket', {'status': ['in', in_progress_statuses], 'fsl_branch_id': ['in',dep_branch_names]})

        cancelled_count = frappe.db.count('HD Ticket', {'status': ['in', cancelled_statuses], 'fsl_branch_id': ['in',dep_branch_names]})

        frappe.local.response["message"] = {
            "success_key": 1,
            "data": {
                "department": department,
                "branch_type": "Branch",
                "total": total,
                "open_count": open_count,
                "in_progress_count": in_progress_count,
                "cancelled_count": cancelled_count
            }
        }

    else :
        frappe.local.response["message"] = {
            "success_key": 0,
            "data": {
                "error": "Department Not Exists",
            }
        }