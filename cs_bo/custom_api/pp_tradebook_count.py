
import frappe
from frappe import _
from datetime import datetime, timedelta

@frappe.whitelist(allow_guest=True)
def get_tradebook_count(from_date=None, to_date=None, ucc=None, zone=None, branch=None, region_code=None, segment=None, token=None, symbol=None, type=None, unique_ucc=None, unique_order_id=None):
    try:
        empty = 1
        # filters = []

        if from_date is None:
            from_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
            
        if to_date is None:
            to_date = frappe.utils.today()
            
        brokerage_filters = [
            ['trade_date', 'between', [from_date,to_date]]
        ]

        if segment:
            # filters.append(["exchange", "=", exchange])
            brokerage_filters.append(["segment", "=", segment])
        if token:
            # filters.append(["token", "=", token])
            brokerage_filters.append(["token", "=", token])
        if symbol:
            # filters.append(["symbol", "=", symbol])
            brokerage_filters.append(["symbol", "=", symbol])
        if type:
            # filters.append(["buysell", "=", buysell])
            brokerage_filters.append(["type", "=", type])
        
        if zone:
            empty = 0
            branches_in_zone = frappe.get_all("Branch", filters={"fsl_zone": zone}, pluck="name")
           
            if branches_in_zone:

                customers_in_branch = frappe.get_all("Customer", filters={"fsl_branch_id": ["in", branches_in_zone]}, pluck="fsl_ucc_code")
                
                if customers_in_branch:
                    brokerage_filters.append(["ucc", "in", customers_in_branch])
                    
                    if unique_ucc :
                        unique_ucc_list = frappe.get_all('Tradebook', filters=brokerage_filters, distinct=True, pluck='ucc')
                        brokerage_total = len(unique_ucc_list)
                    elif unique_order_id:
                        unique_ucc_list = frappe.get_all('Tradebook', filters=brokerage_filters, distinct=True, pluck='order_id')
                        brokerage_total = len(unique_ucc_list)
                    else :
                        brokerage_total = frappe.db.count('Tradebook', filters=brokerage_filters )
            
                    frappe.local.response["message"] = {
                                "status" : "Ok",
                                "total_count": brokerage_total
                            }
                else:
                    frappe.local.response["message"] = {
                        "status" : "Not Ok",
                        "error": "Customer Not Found For This zone"
                    }
            else:
                frappe.local.response["message"] = {
                        "status" : "Not Ok",
                        "error": "Branch Not Found For This zone"
                    }
        
        if region_code:
            empty = 0
            branches_in_zone = frappe.get_all("Branch", filters={"fsl_region_code": region_code}, pluck="name")
           
            if branches_in_zone:

                customers_in_branch = frappe.get_all("Customer", filters={"fsl_branch_id": ["in", branches_in_zone]}, pluck="fsl_ucc_code")
                
                if customers_in_branch:
                    brokerage_filters.append(["ucc", "in", customers_in_branch])
                    
                    if unique_ucc :
                        unique_ucc_list = frappe.get_all('Tradebook', filters=brokerage_filters, distinct=True, pluck='ucc')
                        brokerage_total = len(unique_ucc_list)
                    elif unique_order_id:
                        unique_ucc_list = frappe.get_all('Tradebook', filters=brokerage_filters, distinct=True, pluck='order_id')
                        brokerage_total = len(unique_ucc_list)
                    else :
                        brokerage_total = frappe.db.count('Tradebook', filters=brokerage_filters )
            
                    frappe.local.response["message"] = {
                                "status" : "Ok",
                                "total_count": brokerage_total
                            }
                else:
                    frappe.local.response["message"] = {
                        "status" : "Not Ok",
                        "error": "Customer Not Found For This region_code"
                    }
            else:
                frappe.local.response["message"] = {
                        "status" : "Not Ok",
                        "error": "Branch Not Found For This region_name"
                    }
            
        if branch:
            empty = 0
            customers_in_branch = frappe.get_all("Customer", filters={"fsl_branch_id": branch}, pluck="fsl_ucc_code")
                
            if customers_in_branch:
                brokerage_filters.append(["ucc", "in", customers_in_branch])
                
                if unique_ucc :
                        unique_ucc_list = frappe.get_all('Tradebook', filters=brokerage_filters, distinct=True, pluck='ucc')
                        brokerage_total = len(unique_ucc_list)
                elif unique_order_id:
                        unique_ucc_list = frappe.get_all('Tradebook', filters=brokerage_filters, distinct=True, pluck='order_id')
                        brokerage_total = len(unique_ucc_list)
                else :
                        brokerage_total = frappe.db.count('Tradebook', filters=brokerage_filters )
            
                frappe.local.response["message"] = {
                            "status" : "Ok",
                            "total_count": brokerage_total
                        }
            else :
                frappe.local.response["message"] = {
                        "status" : "Not Ok",
                        "error": "Customer Not Found For This branch"
                    }
            
        if ucc:
            brokerage_filters.append(["ucc", "=", ucc])
           
        if empty :
            if unique_ucc :
                unique_ucc_list = frappe.get_all('Tradebook', filters=brokerage_filters, distinct=True, pluck='ucc')
                brokerage_total = len(unique_ucc_list)
            elif unique_order_id:
                        unique_ucc_list = frappe.get_all('Tradebook', filters=brokerage_filters, distinct=True, pluck='order_id')
                        brokerage_total = len(unique_ucc_list)
            else :
                brokerage_total = frappe.db.count('Tradebook', filters=brokerage_filters )
            
            frappe.local.response["message"] = {
                        "status" : "Ok",
                        "total_count": brokerage_total
                    }

    except Exception as e:
        
        return {f"Error in get_brokerage_summary: {e}"}