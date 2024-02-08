import frappe

@frappe.whitelist()
def get_trading_scheme(opp_id):

    try:
        
        ts = frappe.get_last_doc('Trading Scheme', filters={"opportunity_id": opp_id})    

        frappe.local.response["message"] = {
            "success_key": 1,
            "opportunity_id" : ts.opportunity_id,
            "active_status" : ts.active_status,
            "ddpi" : ts.ddpi,
            "ddpi_one" : ts.ddpi_one,
            "ddpi_two" :  ts.ddpi_two,
            "ddpi_three" : ts.ddpi_three,
            "ddpi_four" : ts.ddpi_four,
            "trading_scheme" : ts.trading_scheme,
            "db_scheme" : ts.db_scheme
            } 
                

    except :
        frappe.local.response["message"] = {
        "success_key": 0,
        "message":"This Opportunity Not Exists"
        }



@frappe.whitelist()
def put_trading_scheme(data):
 
    for i in data:
        try:
            
            ts = frappe.get_last_doc('Trading Scheme', filters={"opportunity_id": i["opportunity_id"]})
            
            if "active_status" in i:
                ts.active_status = i["active_status"]
            if "ddpi" in i:
                ts.ddpi = i["ddpi"]
            if "ddpi_one" in i:
                ts.ddpi_one = i["ddpi_one"]
            if "ddpi_two" in i:
                ts.ddpi_two = i["ddpi_two"]
            if "ddpi_three" in i:
                ts.ddpi_three = i["ddpi_three"]
            if "ddpi_four" in i:
                ts.ddpi_four = i["ddpi_four"]
            if "trading_scheme" in i:
                ts.trading_scheme = i["trading_scheme"]
            if "db_scheme" in i:
                ts.db_scheme = i["db_scheme"]
            ts.save()

            frappe.local.response["message"] = {
                "success_key": 1,
                "message":"Opportunity Updated",
                "opportunity_id": ts.opportunity_id,
                "active_status": ts.active_status,
                "ddpi": ts.ddpi,
                "ddpi_one": ts.ddpi_one,
                "ddpi_two": ts.ddpi_two,
                "ddpi_three": ts.ddpi_three,
                "ddpi_four": ts.ddpi_four,
                "trading_scheme": ts.trading_scheme,
                "db_scheme": ts.db_scheme
                } 
                    

        except :
            
            try:
                ts = frappe.new_doc('Trading Scheme')

                ts.opportunity_id = i.get("opportunity_id")
                ts.active_status = i.get("active_status", None)
                ts.ddpi = i.get("ddpi", None)
                ts.ddpi_one = i.get("ddpi_one", None)
                ts.ddpi_two = i.get("ddpi_two", None)
                ts.ddpi_three = i.get("ddpi_three", None)
                ts.ddpi_four = i.get("ddpi_four", None)
                ts.trading_scheme = i.get("trading_scheme", None)
                ts.db_scheme = i.get("db_scheme", None)

                ts.save()

                frappe.local.response["message"] = {
                    "success_key": 1,
                    "message": "Opportunity Created",
                    "opportunity_id": ts.opportunity_id,
                    "active_status": ts.active_status,
                    "ddpi": ts.ddpi,
                    "ddpi_one": ts.ddpi_one,
                    "ddpi_two": ts.ddpi_two,
                    "ddpi_three": ts.ddpi_three,
                    "ddpi_four": ts.ddpi_four,
                    "trading_scheme": ts.trading_scheme,
                    "db_scheme": ts.db_scheme
                }
            except :
               
                print("Error Occured While Processing Trading Scheme")



# @frappe.whitelist(allow_guest=True)
# def post_trading_scheme(data):
 
#     for i in data:
#         try:
#             ts = frappe.new_doc('Trading Scheme')

#             ts.opportunity_id = i["opportunity_id"]

#             if i["active_status"] in i:
#                 ts.active_status = i["active_status"]

#             if i["ddpi"] in i:
#                 ts.ddpi = i["ddpi"]

#             if i["ddpi_one"] in i:
#                 ts.ddpi_one = i["ddpi_one"]
                
#             if i["ddpi_two"] in i:
#                 ts.ddpi_two = i["ddpi_two"]

#             if i["ddpi_three"] in i:
#                 ts.ddpi_three = i["ddpi_three"]

#             if i["ddpi_four"] in i:
#                 ts.ddpi_four = i["ddpi_four"]

#             if i["trading_scheme"] in i:
#                 ts.trading_scheme = i["trading_scheme"]

#             if i["db_scheme"] in i:
#                 ts.db_scheme = i["db_scheme"]

#             ts.save()

#             frappe.local.response["message"] = {
#                 "success_key": 1,
#                 "message":"Opportunity Created",
#                 "opportunity_id" : ts.opportunity_id if "opportunity_id" in i else None,
#                 "active_status" : ts.active_status if "active_status" in i else None,
#                 "ddpi" : ts.ddpi if "ddpi" in i else None,
#                 "ddpi_one" : ts.ddpi_one if "ddpi_one" in i else None,
#                 "ddpi_two" :  ts.ddpi_two if "ddpi_two" in i else None,
#                 "ddpi_three" : ts.ddpi_three if "ddpi_three" in i else None,
#                 "ddpi_four" : ts.ddpi_four if "ddpi_four" in i else None,
#                 "trading_scheme" : ts.trading_scheme if "trading_scheme" in i else None,
#                 "db_scheme" : ts.db_scheme if "db_scheme" in i else None
#                 } 
                    

#         # except :
#         #     frappe.local.response["message"] = {
#         #     "success_key": 0,
#         #     "message":"This Opportunity Not Exists"
#         #     }
#         except Exception as e:
#             frappe.local.response["message"] = {
#                 "error": f"An error occurred..: {str(e)}"
#             }

# @frappe.whitelist(allow_guest=True)
# def post_trading_scheme(data):
#     for i in data:
        # try:
        #     ts = frappe.new_doc('Trading Scheme')

        #     ts.opportunity_id = i.get("opportunity_id", None)
        #     ts.active_status = i.get("active_status", None)
        #     ts.ddpi = i.get("ddpi", None)
        #     ts.ddpi_one = i.get("ddpi_one", None)
        #     ts.ddpi_two = i.get("ddpi_two", None)
        #     ts.ddpi_three = i.get("ddpi_three", None)
        #     ts.ddpi_four = i.get("ddpi_four", None)
        #     ts.trading_scheme = i.get("trading_scheme", None)
        #     ts.db_scheme = i.get("db_scheme", None)

        #     ts.save()

        #     frappe.local.response["message"] = {
        #         "success_key": 1,
        #         "message": "Opportunity Created",
        #         "opportunity_id": ts.opportunity_id,
        #         "active_status": ts.active_status,
        #         "ddpi": ts.ddpi,
        #         "ddpi_one": ts.ddpi_one,
        #         "ddpi_two": ts.ddpi_two,
        #         "ddpi_three": ts.ddpi_three,
        #         "ddpi_four": ts.ddpi_four,
        #         "trading_scheme": ts.trading_scheme,
        #         "db_scheme": ts.db_scheme
        #     }
        # except Exception as e:
        #     # Handle any exceptions that may occur during document creation
        #     print(f"Error creating Trading Scheme: {e}")
