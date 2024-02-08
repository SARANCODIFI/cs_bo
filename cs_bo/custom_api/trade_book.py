from frappe import _

import frappe

# @frappe.whitelist(allow_guest=True)

# def get_trade_book(ucc, from_date,to_date, segment):
#     try:
#         tradebooks = frappe.get_all("Tradebook",
#             filters={'ucc': ucc,"trade_date": ["between", [from_date, to_date]], "segment": segment},
#             fields=["ucc", "trade_time", "branch", "order_id", "symbol", "trade_id", "segment", "qty", "exchange", "price", "trade_date", "expiry_date", "tags", "type", "value"])

#         tot_data = tradebooks  # Use the fetched data directly

#         frappe.response["message"] = {
#             "Success_key" : 1,
#             "data": tot_data
#         }
#     except Exception as e:
#         frappe.local.response["message"] = {
#             "error": "Trade book data not found"
#         }

# from frappe import _

# import frappe

@frappe.whitelist(allow_guest=True)
def su_trade_book(from_date = None, to_date = None):
    try:
        tradebooks = frappe.get_all("Tradebook",
            filters={"trade_date": ["between", [from_date, to_date]]},
            fields=["ucc", "trade_time", "branch", "order_id", "symbol", "trade_id", "segment", "qty", "exchange", "price", "trade_date", "expiry_date", "tags", "type", "value"])

        tot_data = tradebooks

        frappe.response["message"] = {
            "Success_key": 1,
            "data": tot_data
        }
    except Exception as e:
        frappe.local.response["message"] = {
            "error": "Trade book data not found"
        }




@frappe.whitelist(allow_guest=True)
def post_trade_book(data):
    tot_data = {}
    rdata = []
    table = data.get("tradebook")
    for i in table:
    
        try:
            tradebook = frappe.new_doc("Tradebook")
            
            tradebook.ucc = i["ucc"]
            tradebook.trade_time = i["trade_time"]
            tradebook.branch = i["branch"]
            tradebook.order_id = i["order_id"]
            tradebook.symbol = i["symbol"]
            tradebook.trade_id = i["trade_id"]
            tradebook.segment = i["segment"]
            tradebook.qty = i["qty"]
            tradebook.exchange = i["exchange"]
            tradebook.price = i["price"]
            tradebook.trade_date = i["trade_date"]
            tradebook.expiry_date = i["expiry_date"]
            tradebook.tags = i["tags"] 
            tradebook.type = i["type"] 
            tradebook.value = i["value"]
            tradebook.insert()

            rdata = {
                "ucc" : tradebook.ucc,
                "trade_time" : tradebook.trade_time,
                "branch" : tradebook.branch,
                "order_id" : tradebook.order_id,
                "symbol" : tradebook.symbol,
                "trade_id" : tradebook.trade_id ,
                "segment" : tradebook.segment,
                "qty" : tradebook.qty,
                "exchange" : tradebook.exchange,
                "price" : tradebook.price,
                "trade_date" : tradebook.trade_date,
                "expiry_date" : tradebook.expiry_date,
                "tags" : tradebook.tags,
                "type" : tradebook.type,
                "value" : tradebook.value,
            }
            tot_data.append(rdata)
            


        except Exception as e:
            frappe.local.response["message"] = {
                "error": "Trade book data not found"
            }
    frappe.response["message"] = {
        "success_key": 1,
        "data":tot_data
     }


@frappe.whitelist(allow_guest=True)
def get_trade_book(ucc, from_date=None, to_date=None, segment=None):
    try:
        filters = {'ucc': ucc}
        
        if from_date and to_date:
            filters['trade_date'] = ["between", [from_date, to_date]]
        
        if segment:
            filters['segment'] = segment

        tradebooks = frappe.get_all("Tradebook",
            filters=filters,
            fields=["ucc", "trade_time", "branch", "order_id", "symbol", "trade_id", "segment", "qty", "exchange", "price", "trade_date", "expiry_date", "tags", "type", "value"])

        tot_data = tradebooks  # Use the fetched data directly

        frappe.response["message"] = {
            "Success_key" : 1,
            "data": tot_data
        }
    except Exception as e:
        frappe.local.response["message"] = {
            "error": "Trade book data not found"
        }
