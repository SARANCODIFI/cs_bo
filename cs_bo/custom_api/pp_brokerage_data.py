
import frappe
from frappe import _
from datetime import datetime, timedelta

@frappe.whitelist(allow_guest=True)
def get_brokerage_summary(from_date=None, to_date=None, ucc=None, zone=None, branch=None, region_code=None, exchange=None, token=None, symbol=None, buysell=None):
    try:
        empty = 1
        # filters = []

        if from_date is None:
            from_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
            
        if to_date is None:
            to_date = frappe.utils.today()
            
        brokerage_filters = [
            ['dtoftran', 'between', [from_date,to_date]]
        ]

        if exchange:
            # filters.append(["exchange", "=", exchange])
            brokerage_filters.append(["exchange", "=", exchange])
        if token:
            # filters.append(["token", "=", token])
            brokerage_filters.append(["token", "=", token])
        if symbol:
            # filters.append(["symbol", "=", symbol])
            brokerage_filters.append(["symbol", "=", symbol])
        if buysell:
            # filters.append(["buysell", "=", buysell])
            brokerage_filters.append(["buysell", "=", buysell])
        
        if zone:
            empty = 0
            branches_in_zone = frappe.get_all("Branch", filters={"fsl_zone": zone}, pluck="name")
           
            if branches_in_zone:

                customers_in_branch = frappe.get_all("Customer", filters={"fsl_branch_id": ["in", branches_in_zone]}, pluck="fsl_ucc_code")
                
                if customers_in_branch:
                    brokerage_filters.append(["ucc", "in", customers_in_branch])
                    
                    brokerage_total = frappe.db.get_list("BrokerageDetails", 
                        filters=brokerage_filters, 
                        fields=["ucc","exchange","dtoftran","symbol","token","buysell","quantity","market","brokerage"]
                        )

                    # result = [{"total_brokerage": brokerage_total}]
                    
                    frappe.local.response["message"] = {
                        "status" : "Ok",
                        "zone" : zone,
                        "brokerage_summary": brokerage_total
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
                    
                    brokerage_total = frappe.db.get_list("BrokerageDetails", 
                        filters=brokerage_filters, 
                        fields=["ucc","exchange","dtoftran","symbol","token","buysell","quantity","market","brokerage"]
                        )


                    # result = [{"total_brokerage": brokerage_total}]
                    
                    frappe.local.response["message"] = {
                        "status" : "Ok",
                        "region_code" : region_code,
                        "brokerage_summary": brokerage_total
                    }
                else:
                    frappe.local.response["message"] = {
                        "status" : "Not Ok",
                        "error": "Customer Not Found For This region_code"
                    }
            else:
                frappe.local.response["message"] = {
                        "status" : "Not Ok",
                        "error": "Branch Not Found For This region_code"
                    }
            
        if branch:
            empty = 0
            customers_in_branch = frappe.get_all("Customer", filters={"fsl_branch_id": branch}, pluck="fsl_ucc_code")
                
            if customers_in_branch:
                brokerage_filters.append(["ucc", "in", customers_in_branch])
                
                brokerage_total = frappe.db.get_list("BrokerageDetails", 
                        filters=brokerage_filters, 
                        fields=["ucc","exchange","dtoftran","symbol","token","buysell","quantity","market","brokerage"]
                        )

                frappe.local.response["message"] = {
                        "status" : "Ok",
                        "branch" : branch,
                        "brokerage_summary": brokerage_total
                    }
            else :
                frappe.local.response["message"] = {
                        "status" : "Not Ok",
                        "error": "Customer Not Found For This branch"
                    }
            
        if ucc:
            brokerage_filters.append(["ucc", "=", ucc])
           
        if empty :
            brokerage_total = frappe.db.get_list("BrokerageDetails", 
                        filters=brokerage_filters, 
                        fields=["ucc","exchange","dtoftran","symbol","token","buysell","quantity","market","brokerage"]
                        )
           
            frappe.local.response["message"] = {
                        "status" : "Ok",
                        "brokerage_summary": brokerage_total
                    }

    except Exception as e:
        
        return {f"Error in get_brokerage_summary: {e}"}