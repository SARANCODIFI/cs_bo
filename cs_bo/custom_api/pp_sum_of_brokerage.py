
import frappe
from frappe import _
from datetime import datetime, timedelta

@frappe.whitelist(allow_guest=True)
def get_brokerage_summary(from_date=None, to_date=None, ucc=None, zone=None, branch=None, region_name=None, exchange=None, token=None, symbol=None, buysell=None):
    try:
        empty = 1

        if from_date is None:
            from_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
            
        if to_date is None:
            to_date = frappe.utils.today()
            
        brokerage_filters = [
            ['dtoftran', 'between', [from_date,to_date]]
        ]

        if exchange:
            brokerage_filters.append(["exchange", "=", exchange])
        if token:
            brokerage_filters.append(["token", "=", token])
        if symbol:
            brokerage_filters.append(["symbol", "=", symbol])
        if buysell:
            brokerage_filters.append(["buysell", "=", buysell])
        
        if zone:
            empty = 0
            branches_in_zone = frappe.get_all("Branch", filters={"fsl_zone": zone}, pluck="name")
           
            if branches_in_zone:

                customers_in_branch = frappe.get_all("Customer", filters={"fsl_branch_id": ["in", branches_in_zone]}, pluck="fsl_ucc_code")
                
                if customers_in_branch:
                    brokerage_filters.append(["ucc", "in", customers_in_branch])
                    
                    brokerage_total = frappe.get_all("BrokerageDetails", 
                        filters=brokerage_filters, 
                        fields=["SUM(brokerage) as total_brokerage"]
                        )[0].get("total_brokerage") or 0

                    result = [{"total_brokerage": brokerage_total}]
                    
                    return result[0] if result else {"total_brokerage": 0}
                else:
                    return {"total_brokerage": 0}
            else:
                return {"total_brokerage": 0}
        
        if region_name:
            empty = 0
            branches_in_zone = frappe.get_all("Branch", filters={"fsl_region_name": region_name}, pluck="name")
           
            if branches_in_zone:

                customers_in_branch = frappe.get_all("Customer", filters={"fsl_branch_id": ["in", branches_in_zone]}, pluck="fsl_ucc_code")
                
                if customers_in_branch:
                    brokerage_filters.append(["ucc", "in", customers_in_branch])
                    
                    brokerage_total = frappe.get_all("BrokerageDetails", 
                        filters=brokerage_filters, 
                        fields=["SUM(brokerage) as total_brokerage"]
                        )[0].get("total_brokerage") or 0


                    result = [{"total_brokerage": brokerage_total}]
                    
                    return result[0] if result else {"total_brokerage": 0}
                else:
                    return {"total_brokerage": 0}
            else:
                return {"total_brokerage": 0}
            
        if branch:
            empty = 0
            sql_query = """
                SELECT
                    SUM(brokerage) AS total_brokerage
                FROM
                    `tabBrokerageDetails`
                WHERE
                    ucc IN (
                        SELECT fsl_ucc_code
                        FROM `tabCustomer`
                        WHERE fsl_branch_id = %s
                    )
            """
            result = frappe.db.sql(sql_query, (branch,), as_dict=True)
        
            
        if ucc:
            brokerage_filters.append(["ucc", "=", ucc])
           
        if empty :
            brokerage_total = frappe.get_all("BrokerageDetails",             
                filters=brokerage_filters,
                fields=["SUM(brokerage) as total_brokerage"]
                )[0].get("total_brokerage") or 0

            result = [{"total_brokerage": brokerage_total}]
                        
        frappe.local.response["message"] = {
            "total_brokerage": result[0].get("total_brokerage") if result else 0
        }

    except Exception as e:
        frappe.errprint(f"Error in get_brokerage_summary: {e}")
        return {"error": _("Error in API execution")}