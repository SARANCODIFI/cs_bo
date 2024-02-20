import frappe
from datetime import datetime, timedelta

def get_phase(oppr_stage):
    stage_map = {
        "0.5": "SMS verification",
        "1": "E-mail verification",
        "1.1": "Password verification",
        "2": "Pan verification",
        "2.1": "Pan NSDL Data Confirm verification",
        "2.2": "Pan Confirm verification",
        "2.3": "Pan KRA DOB Entry verification",
        "3": "Aadhar verification",
        "4": "Profile verification",
        "5": "Bank verification",
        "5.1": "Penny verification",
        "6": "Segment verification",
        "7": "Payment verification",
        "8": "Nominee verification",
        "8.1": "Nominee_1 verification",
        "8.2": "Nominee_2 verification",
        "8.3": "Nominee_3 verification",
        "9": "Document verification",
        "10": "IPV verification",
        "11": "PDF Download verification",
        "12": "E-Sign verification",
        "13": "Complete Email Attached verification"
    }
    return stage_map.get(oppr_stage, oppr_stage)  # Return stage description or original stage if not found

@frappe.whitelist(allow_guest=True)
def oppr_account_details(from_date=None, to_date=None, zone=None, branch=None, region_code=None):
    try:
        result_data = []
        response_msg = {"status": "Not Ok", "opprs_details": "No data found"}

        if from_date is None:
            from_date = frappe.utils.today()
        if to_date is None:
            to_date = frappe.utils.today()

        oppr_filters = [['creation', 'between', [from_date, to_date]]]

        if zone or region_code or branch:
            if branch == "online":
                oppr_filters.append(["fsl_referral_by", "=", "online"])
            else:
                branches_filter = None

                if zone:
                    branches_filter = {"fsl_zone": zone}
                elif region_code:
                    branches_filter = {"fsl_region_code": region_code}
                elif branch:
                    branches_filter = {"name": branch}
                
                branches_in_filter = frappe.get_all("Branch", filters=branches_filter, pluck="name")
                
                if not branches_in_filter:                    
                    return {"status": "Not Ok", "opprs_details":"No branches found for the specified criteria"}
                    
                

                employee_in_branch = frappe.get_all("Employee", filters={"branch": ["in", branches_in_filter]}, pluck="name")
                if not employee_in_branch:  # No employees found for the specified branch
                    return {"status": "Not Ok", "opprs_details": "No employees found for the specified branch"}

                oppr_filters.append(["fsl_referral_by", "in", employee_in_branch])
                response_msg["status"] = "Ok"

        opprs_details = frappe.db.get_list('Opportunity',
                                            filters=oppr_filters,
                                            fields=['name', 'creation', 'modified', 'fsl_stage', 'fsl_stage13_timing'],
                                            as_list=True
                                            )
        if opprs_details:
            response_msg["status"] = "Ok"

        for oppr_details in opprs_details:
            result_item = {
                "name": oppr_details[0],
                "creation": oppr_details[1],
                "modified": oppr_details[2],
                "stage": get_phase(oppr_details[3]), 
            }
            stage13_timing = oppr_details[4]
            if stage13_timing is not None:
                result_item["stage13_timing"] = stage13_timing
            result_data.append(result_item)

        response_msg["opprs_details"] = result_data
        return response_msg

    except Exception as e:
        return {"Error": "An error occurred while processing the request"}
