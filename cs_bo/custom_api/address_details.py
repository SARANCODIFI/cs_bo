from frappe import _

import frappe

@frappe.whitelist(allow_guest=True)

def get_address(opportunity):
    try:
        address = frappe.get_last_doc("Address",
            filters={'fsl_from_opportunity': opportunity})
            # fields=["fsl_active_status", "fsl_aadhaar_no", "fsl_access_token", "fsl_address_confirm", "fsl_application_id","fsl_digi_name","fsl_digi_dob","fsl_digi_gender","fsl_digi_cur_address","fsl_digi_cur_country","fsl_digi_cur_district","fsl_digi_cur_locality","fsl_digi_cur_pincode","fsl_digi_cur_state","fsl_digi_per_address","fsl_digi_per_country","fsl_digi_per_district","fsl_digi_per_locality","fsl_digi_per_pincode","fsl_digi_per_state","fsl_is_kra","fsl_is_manual","fsl_is_digi","fsl_kra_address_1","fsl_kra_address_2","fsl_kra_address_3","fsl_kra_city","fsl_kra_country","fsl_kra_per_address_1","fsl_kra_per_address_2","fsl_kra_per_address_3","fsl_kra_per_city","fsl_kra_per_country","fsl_kra_per_pin","fsl_kra_per_state","fsl_kra_address_proof","fsl_kra_proof_idnumber","fsl_from_opportunity","fsl_kra_pin","fsl_from_lead","fsl_kra_state","fsl_from_customer","fsl_kra_push_needed","fsl_kra_mobile_number","fsl_kra_email_id"])

        response_data = {
                    "fsl_active_status": address.fsl_active_status,
                    "fsl_aadhaar_no": address.fsl_aadhaar_no,
                    "fsl_access_token": address.fsl_access_token,
                    "fsl_address_confirm": address.fsl_address_confirm,
                    "fsl_application_id": address.fsl_application_id,
                    "fsl_digi_name": address.fsl_digi_name,
                    "fsl_digi_dob": address.fsl_digi_dob,
                    "fsl_digi_gender": address.fsl_digi_gender,
                    "fsl_digi_cur_address": address.fsl_digi_cur_address,
                    "fsl_digi_cur_country": address.fsl_digi_cur_country,
                    "fsl_digi_cur_district": address.fsl_digi_cur_district,
                    "fsl_digi_cur_locality": address.fsl_digi_cur_locality,
                    "fsl_digi_cur_pincode": address.fsl_digi_cur_pincode,
                    "fsl_digi_cur_state": address.fsl_digi_cur_state,
                    "fsl_digi_per_address": address.fsl_digi_per_address,
                    "fsl_digi_per_country": address.fsl_digi_per_country,
                    "fsl_digi_per_district": address.fsl_digi_per_district,
                    "fsl_digi_per_locality": address.fsl_digi_per_locality,
                    "fsl_digi_per_pincode": address.fsl_digi_per_pincode,
                    "fsl_digi_per_state": address.fsl_digi_per_state,
                    "fsl_is_kra": address.fsl_is_kra,
                    "fsl_is_manual": address.fsl_is_manual,
                    "fsl_is_digi": address.fsl_is_digi,
                    "fsl_kra_address_1": address.fsl_kra_address_1,
                    "fsl_kra_address_2": address.fsl_kra_address_2,
                    "fsl_kra_address_3": address.fsl_kra_address_3,
                    "fsl_kra_city": address.fsl_kra_city,
                    "fsl_kra_country": address.fsl_kra_country,
                    "fsl_kra_per_address_1": address.fsl_kra_per_address_1,
                    "fsl_kra_per_address_2": address.fsl_kra_per_address_2,
                    "fsl_kra_per_address_3": address.fsl_kra_per_address_3,
                    "fsl_kra_per_city": address.fsl_kra_per_city,
                    "fsl_kra_per_country": address.fsl_kra_per_country,
                    "fsl_kra_per_pin": address.fsl_kra_per_pin,
                    "fsl_kra_per_state": address.fsl_kra_per_state,
                    "fsl_kra_address_proof": address.fsl_kra_address_proof,
                    "fsl_kra_proof_idnumber": address.fsl_kra_proof_idnumber,
                    "fsl_from_opportunity": address.fsl_from_opportunity,
                    "fsl_kra_pin": address.fsl_kra_pin,
                    "fsl_from_lead": address.fsl_from_lead,
                    "fsl_kra_state": address.fsl_kra_state,
                    "fsl_from_customer": address.fsl_from_customer,
                    "fsl_kra_push_needed": address.fsl_kra_push_needed,
                    "fsl_kra_mobile_number": address.fsl_kra_mobile_number,
                    "fsl_kra_email_id": address.fsl_kra_email_id
                    
                }

        frappe.local.response["message"] = {
            "success_key": 1,
            "message": "Address updated successfully",
            "data": response_data
        }

    except Exception as e:
        frappe.local.response["message"] = {
            "error": "An error occurred."
        }




@frappe.whitelist(allow_guest=True)
def update_address(data):
    for i in data:
        try:
            address = frappe.get_last_doc("Address",filters={"fsl_from_opportunity":i["opportunity"]}) 
            if address:
                for datas in i:
                    address.update({
                        datas : i[datas]
                    })
                address.save()
                frappe.response["message"] = {
                    "id":address.name,
                    "data": {
                        address
                    }
                }
        except:
                frappe.response["message"] = {
                "error":"address  Not Exists"
            }
        
        # except:
        #     frappe.response["message"] = {
        #         "error":"Not Updated"
        #     }
# @frappe.whitelist(allow_guest=True, methods=["PUT"])
# def update_address(data):

#     try:
#         data_dict = frappe.parse_json(data)

#         opportunity = data_dict.get('fsl_from_opportunity')

#         address = frappe.get_list_doc("Address", filters={'fsl_from_opportunity': data})
#         frappe.errprint(["opportunity"])

#         response_data = {}

#         if address:
#             address = address.name
#             address = frappe.get_list("Address", filters={
#                 "fsl_from_opportunity": opportunity
#             })

#             if address:
#                 address = address[0]
#                 response_data = {
#                     "fsl_active_status": address.fsl_active_status,
#                     "fsl_aadhaar_no": address.fsl_aadhaar_no,
#                     "fsl_access_token": address.last_name,
#                     "fsl_address_confirm": address.mobile_no,
#                     "fsl_application_id": address.fsl_application_id,
#                     "fsl_digi_name": address.fsl_digi_name,
#                     "fsl_digi_dob": address.fsl_digi_dob,
#                     "fsl_digi_gender": address.fsl_digi_gender,
#                     "fsl_digi_cur_address": address.fsl_digi_cur_address,
#                     "fsl_digi_cur_country": address.fsl_digi_cur_country,
#                     "fsl_digi_cur_district": address.fsl_digi_cur_district,
#                     "fsl_digi_cur_locality": address.fsl_digi_cur_locality,
#                     "fsl_digi_cur_pincode": address.fsl_digi_cur_pincode,
#                     "fsl_digi_cur_state": address.fsl_digi_cur_state,
#                     "fsl_digi_per_address": address.fsl_digi_per_address,
#                     "fsl_digi_per_country": address.fsl_digi_per_country,
#                     "fsl_digi_per_district": address.fsl_digi_per_district,
#                     "fsl_digi_per_locality": address.fsl_digi_per_locality,
#                     "fsl_digi_per_pincode": address.fsl_digi_per_pincode,
#                     "fsl_digi_per_state": address.fsl_digi_per_state,
#                     "fsl_is_kra": address.fsl_is_kra,
#                     "fsl_is_manual": address.fsl_is_manual,
#                     "fsl_is_digi": address.fsl_is_digi,
#                     "fsl_kra_address_1": address.fsl_kra_address_1,
#                     "fsl_kra_address_2": address.fsl_kra_address_2,
#                     "fsl_kra_address_3": address.fsl_kra_address_3,
#                     "fsl_kra_city": address.fsl_kra_city,
#                     "fsl_kra_country": address.fsl_kra_country,
#                     "fsl_kra_per_address_1": address.fsl_kra_per_address_1,
#                     "fsl_kra_per_address_2": address.fsl_kra_per_address_2,
#                     "fsl_kra_per_address_3": address.fsl_kra_per_address_3,
#                     "fsl_kra_per_city": address.fsl_kra_per_city,
#                     "fsl_kra_per_country": address.fsl_kra_per_country,
#                     "fsl_kra_per_pin": address.fsl_kra_per_pin,
#                     "fsl_kra_per_state": address.fsl_kra_per_state,
#                     "fsl_kra_address_proof": address.fsl_kra_address_proof,
#                     "fsl_kra_proof_idnumber": address.fsl_kra_proof_idnumber,
#                     "fsl_from_opportunity": address.fsl_from_opportunity,
#                     "fsl_kra_pin": address.fsl_kra_pin,
#                     "fsl_from_lead": address.fsl_from_lead,
#                     "fsl_kra_state": address.fsl_kra_state,
#                     "fsl_from_customer": address.fsl_from_customer,
#                     "fsl_kra_push_needed": address.fsl_kra_push_needed,
#                     "fsl_kra_mobile_number": address.fsl_kra_mobile_number,
#                     "fsl_kra_email_id": address.fsl_kra_email_id
                    
#                 }

#         frappe.local.response["message"] = {
#             "success_key": 1,
#             "message": "Address updated successfully",
#             "data": response_data
#         }
#     except Exception as e:
#         frappe.log_error(f"Error in update_address: {str(e)}")
#         frappe.local.response["message"] = {
#             "success_key": 0,
#             "message": f"Error: {str(e)}"
#         }


@frappe.whitelist(allow_guest=True)
def create_address(data): 
   for i in data:
        Success = 0   
        
        # frappe.errprint("add")
        
        try:
            address = frappe.get_last_doc("Address",filters={"fsl_from_opportunity":i["fsl_from_opportunity"]}) 
            data_dict = {}
            
            if address:
                Success = 1
                if "fsl_active_status" in i:
                    address.fsl_active_status = i["fsl_active_status"]
                    data_dict["fsl_active_status"]=i["fsl_active_status"]
                if "address_title" in i:
                    address.address_title = i["address_title"]
                    data_dict["address_title"]=i["address_title"]
                if "fsl_aadhaar_no" in i:
                    address.fsl_aadhaar_no = i["fsl_aadhaar_no"]
                    data_dict["fsl_aadhaar_no"]=i["fsl_aadhaar_no"]
                if "fsl_access_token" in i:
                    address.fsl_access_token = i["fsl_access_token"]
                    data_dict["fsl_access_token"]=i["fsl_access_token"]
                if "fsl_address_confirm" in i:
                    address.fsl_address_confirm = i["fsl_address_confirm"]
                    data_dict["fsl_address_confirm"]=i["fsl_address_confirm"]
                if "fsl_application_id" in i:
                    address.fsl_application_id = i["fsl_application_id"]
                    data_dict["fsl_application_id"]=i.fsl_application_id
                if "fsl_digi_name" in i:
                    address.fsl_digi_name = i["fsl_digi_name"]
                    data_dict["fsl_digi_name"]=address.fsl_digi_name
                if "fsl_digi_dob" in i:
                    address.fsl_digi_dob = i["fsl_digi_dob"]
                    data_dict["fsl_digi_dob"]=address.fsl_digi_dob
                if "fsl_digi_gender" in i:
                    address.fsl_digi_gender = i["fsl_digi_gender"]
                    data_dict["fsl_digi_gender"]=address.fsl_digi_gender
                if "fsl_digi_cur_address" in i:
                    address.fsl_digi_cur_address = i["fsl_digi_cur_address"] 
                    data_dict["fsl_digi_cur_address"]=address.fsl_digi_cur_address 
                if "fsl_digi_cur_country" in i:
                    address.fsl_digi_cur_country = i["fsl_digi_cur_country"]
                    data_dict["fsl_digi_cur_country"]=address.fsl_digi_cur_country
                if "fsl_digi_cur_district" in i:
                    address.fsl_digi_cur_district = i["fsl_digi_cur_district"]
                    data_dict["fsl_digi_cur_district"]=address.fsl_digi_cur_district
                if "fsl_digi_cur_locality" in i:
                    address.fsl_digi_cur_locality = i["fsl_digi_cur_locality"]
                    data_dict["fsl_digi_cur_locality"]=address.fsl_digi_cur_locality
                if "fsl_digi_cur_pincode" in i:
                    address.fsl_digi_cur_pincode = i["fsl_digi_cur_pincode"]
                    data_dict["fsl_digi_cur_pincode"]=address.fsl_digi_cur_pincode
                if "fsl_digi_cur_state" in i:
                    address.fsl_digi_cur_state = i["fsl_digi_cur_state"]
                    data_dict["fsl_digi_cur_state"]=address.fsl_digi_cur_state
                if "fsl_digi_per_address" in i:
                    address.fsl_digi_per_address = i["fsl_digi_per_address"] 
                    data_dict["fsl_digi_per_address"]=address.fsl_digi_per_address 
                if "fsl_digi_per_country" in i:
                    address.fsl_digi_per_country = i["fsl_digi_per_country"]
                    data_dict["fsl_digi_per_country"]=address.fsl_digi_per_country
                if "fsl_digi_per_district" in i:
                    address.fsl_digi_per_district = i["fsl_digi_per_district"]
                    data_dict["fsl_digi_per_district"]=address.fsl_digi_per_district
                if "fsl_digi_per_locality" in i:
                    address.fsl_digi_per_locality = i["fsl_digi_per_locality"]
                    data_dict["fsl_digi_per_locality"]=address.fsl_digi_per_locality
                if "fsl_digi_per_pincode" in i:
                    address.fsl_digi_per_pincode = i["fsl_digi_per_pincode"]
                    data_dict["fsl_digi_per_pincode"]=address.fsl_digi_per_pincode
                if "fsl_digi_per_state" in i:
                    address.fsl_digi_per_state = i["fsl_digi_per_state"]
                    data_dict["fsl_digi_per_state"]=address.fsl_digi_per_state
                if "fsl_is_kra" in i:
                    address.fsl_is_kra = i["fsl_is_kra"]  
                    data_dict["fsl_is_kra"]=address.fsl_is_kra
                if "fsl_is_manual" in i:
                    address.fsl_is_manual = i["fsl_is_manual"]
                    data_dict["fsl_is_manual"]=address.fsl_is_manual
                if "fsl_is_digi" in i:
                    address.fsl_is_digi = i["fsl_is_digi"]
                    data_dict["fsl_is_digi"]=address.fsl_is_digi
                if "fsl_kra_address_1" in i:
                    address.fsl_kra_address_1 = i["fsl_kra_address_1"]
                    data_dict["fsl_kra_address_1"]=address.fsl_kra_address_1
                if "fsl_kra_address_2" in i:
                    address.fsl_kra_address_2 = i["fsl_kra_address_2"]
                    data_dict["fsl_kra_address_2"]=address.fsl_kra_address_2
                if "fsl_kra_address_3" in i:
                    address.fsl_kra_address_3 = i["fsl_kra_address_3"]
                    data_dict["fsl_kra_address_3"]=address.fsl_kra_address_3
                if "fsl_kra_city" in i:
                    address.fsl_kra_city = i["fsl_kra_city"]  
                    data_dict["fsl_kra_city"]=address.fsl_kra_city
                if "fsl_kra_country" in i:
                    address.fsl_kra_country = i["fsl_kra_country"]
                    data_dict["fsl_kra_country"]=address.fsl_kra_country
                if "fsl_kra_per_address_1" in i:
                    address.fsl_kra_per_address_1 = i["fsl_kra_per_address_1"]
                    data_dict["fsl_kra_per_address_1"]=address.fsl_kra_per_address_1
                if "fsl_kra_per_address_2" in i:
                    address.fsl_kra_per_address_2 = i["fsl_kra_per_address_2"]
                    data_dict["fsl_kra_per_address_2"]=address.fsl_kra_per_address_2
                if "fsl_kra_per_address_3" in i:
                    address.fsl_kra_per_address_3 = i["fsl_kra_per_address_3"]
                    data_dict["fsl_kra_per_address_3"]=address.fsl_kra_per_address_3
                if "fsl_kra_per_city" in i:
                    address.fsl_kra_per_city = i["fsl_kra_per_city"]
                    data_dict["fsl_kra_per_city"]=address.fsl_kra_per_city
                if "fsl_kra_per_country" in i:
                    address.fsl_kra_per_country = i["fsl_kra_per_country"]
                    data_dict["fsl_kra_per_country"]=address.fsl_kra_per_country
                if "fsl_kra_per_pin" in i:
                    address.fsl_kra_per_pin = i["fsl_kra_per_pin"]
                    data_dict["fsl_kra_per_pin"]=address.fsl_kra_per_pin
                if "fsl_kra_per_state" in i:
                    address.fsl_kra_per_state = i["fsl_kra_per_state"] 
                    data_dict["fsl_kra_per_state"]=address.fsl_kra_per_state
                if "fsl_kra_address_proof" in i: 
                    address.fsl_kra_address_proof = i["fsl_kra_address_proof"]
                    data_dict["fsl_kra_address_proof"]=address.fsl_kra_address_proof
                if "fsl_kra_proof_idnumber" in i:
                    address.fsl_kra_proof_idnumber = i["fsl_kra_proof_idnumber"]
                    data_dict["fsl_kra_proof_idnumber"]=address.fsl_kra_proof_idnumber
                if "fsl_from_opportunity" in i:
                    address.fsl_from_opportunity = i["fsl_from_opportunity"]
                    data_dict["fsl_from_opportunity"]=address.fsl_from_opportunity
                if "fsl_kra_per_address_3" in i:
                    address.fsl_kra_per_address_3 = i["fsl_kra_per_address_3"]
                    data_dict["fsl_kra_per_address_3"]=address.fsl_kra_per_address_3
                if "fsl_kra_pin" in i:
                    address.fsl_kra_pin = i["fsl_kra_pin"]
                    data_dict["fsl_kra_pin"]=address.fsl_kra_pin
                # if data["fsl_from_lead"]:
                #     address.fsl_from_lead = data["fsl_from_lead"]
                if "fsl_kra_state" in i:
                    address.fsl_kra_state = i["fsl_kra_state"]
                    data_dict["fsl_kra_state"]=address.fsl_kra_state
                if "fsl_from_customer" in i:
                    address.fsl_from_customer = i["fsl_from_customer"]
                    data_dict["fsl_from_customer"]=address.fsl_from_customer
                if "fsl_kra_push_needed" in i:
                    address.fsl_kra_push_needed = i["fsl_kra_push_needed"]
                    data_dict["fsl_kra_push_needed"]=address.fsl_kra_push_needed
                if "fsl_kra_mobile_number" in i:
                    address.fsl_kra_mobile_number = i["fsl_kra_mobile_number"]
                    data_dict["fsl_kra_mobile_number"]=address.fsl_kra_mobile_number
                if "fsl_kra_email_id" in i:
                    address.fsl_kra_email_id = i["fsl_kra_email_id"]  
                    data_dict["fsl_kra_email_id"]=address.fsl_kra_email_id
                
                address.save()
                frappe.response["message"] = {
                    "id":address.name,
                    "Success": Success,
                    "data":data_dict
                }

        except: 
            data_dict = {}
            address = frappe.new_doc("Address")
            if "fsl_active_status" in i:
                address.fsl_active_status = i["fsl_active_status"]
                data_dict["fsl_active_status"]=i["fsl_active_status"]
            if "address_title" in i:
                address.address_title = i["address_title"]
                data_dict["address_title"]=i["address_title"]
            if "fsl_aadhaar_no" in i:
                address.fsl_aadhaar_no = i["fsl_aadhaar_no"]
                data_dict["fsl_aadhaar_no"]=i["fsl_aadhaar_no"]
            if "fsl_access_token" in i:
                address.fsl_access_token = i["fsl_access_token"]
                data_dict["fsl_access_token"]=i["fsl_access_token"]
            if "fsl_address_confirm" in i:
                address.fsl_address_confirm = i["fsl_address_confirm"]
                data_dict["fsl_address_confirm"]=i["fsl_address_confirm"]
            if "fsl_application_id" in i:
                address.fsl_application_id = i["fsl_application_id"]
                data_dict["fsl_application_id"]=i.fsl_application_id
            if "fsl_digi_name" in i:
                address.fsl_digi_name = i["fsl_digi_name"]
                data_dict["fsl_digi_name"]=address.fsl_digi_name
            if "fsl_digi_dob" in i:
                address.fsl_digi_dob = i["fsl_digi_dob"]
                data_dict["fsl_digi_dob"]=address.fsl_digi_dob
            if "fsl_digi_gender" in i:
                address.fsl_digi_gender = i["fsl_digi_gender"]
                data_dict["fsl_digi_gender"]=address.fsl_digi_gender
            if "fsl_digi_cur_address" in i:
                address.fsl_digi_cur_address = i["fsl_digi_cur_address"] 
                data_dict["fsl_digi_cur_address"]=address.fsl_digi_cur_address 
            if "fsl_digi_cur_country" in i:
                address.fsl_digi_cur_country = i["fsl_digi_cur_country"]
                data_dict["fsl_digi_cur_country"]=address.fsl_digi_cur_country
            if "fsl_digi_cur_district" in i:
                address.fsl_digi_cur_district = i["fsl_digi_cur_district"]
                data_dict["fsl_digi_cur_district"]=address.fsl_digi_cur_district
            if "fsl_digi_cur_locality" in i:
                address.fsl_digi_cur_locality = i["fsl_digi_cur_locality"]
                data_dict["fsl_digi_cur_locality"]=address.fsl_digi_cur_locality
            if "fsl_digi_cur_pincode" in i:
                address.fsl_digi_cur_pincode = i["fsl_digi_cur_pincode"]
                data_dict["fsl_digi_cur_pincode"]=address.fsl_digi_cur_pincode
            if "fsl_digi_cur_state" in i:
                address.fsl_digi_cur_state = i["fsl_digi_cur_state"]
                data_dict["fsl_digi_cur_state"]=address.fsl_digi_cur_state
            if "fsl_digi_per_address" in i:
                address.fsl_digi_per_address = i["fsl_digi_per_address"] 
                data_dict["fsl_digi_per_address"]=address.fsl_digi_per_address 
            if "fsl_digi_per_country" in i:
                address.fsl_digi_per_country = i["fsl_digi_per_country"]
                data_dict["fsl_digi_per_country"]=address.fsl_digi_per_country
            if "fsl_digi_per_district" in i:
                address.fsl_digi_per_district = i["fsl_digi_per_district"]
                data_dict["fsl_digi_per_district"]=address.fsl_digi_per_district
            if "fsl_digi_per_locality" in i:
                address.fsl_digi_per_locality = i["fsl_digi_per_locality"]
                data_dict["fsl_digi_per_locality"]=address.fsl_digi_per_locality
            if "fsl_digi_per_pincode" in i:
                address.fsl_digi_per_pincode = i["fsl_digi_per_pincode"]
                data_dict["fsl_digi_per_pincode"]=address.fsl_digi_per_pincode
            if "fsl_digi_per_state" in i:
                address.fsl_digi_per_state = i["fsl_digi_per_state"]
                data_dict["fsl_digi_per_state"]=address.fsl_digi_per_state
            if "fsl_is_kra" in i:
                address.fsl_is_kra = i["fsl_is_kra"]  
                data_dict["fsl_is_kra"]=address.fsl_is_kra
            if "fsl_is_manual" in i:
                address.fsl_is_manual = i["fsl_is_manual"]
                data_dict["fsl_is_manual"]=address.fsl_is_manual
            if "fsl_is_digi" in i:
                address.fsl_is_digi = i["fsl_is_digi"]
                data_dict["fsl_is_digi"]=address.fsl_is_digi
            if "fsl_kra_address_1" in i:
                address.fsl_kra_address_1 = i["fsl_kra_address_1"]
                data_dict["fsl_kra_address_1"]=address.fsl_kra_address_1
            if "fsl_kra_address_2" in i:
                address.fsl_kra_address_2 = i["fsl_kra_address_2"]
                data_dict["fsl_kra_address_2"]=address.fsl_kra_address_2
            if "fsl_kra_address_3" in i:
                address.fsl_kra_address_3 = i["fsl_kra_address_3"]
                data_dict["fsl_kra_address_3"]=address.fsl_kra_address_3
            if "fsl_kra_city" in i:
                address.fsl_kra_city = i["fsl_kra_city"]  
                data_dict["fsl_kra_city"]=address.fsl_kra_city
            if "fsl_kra_country" in i:
                address.fsl_kra_country = i["fsl_kra_country"]
                data_dict["fsl_kra_country"]=address.fsl_kra_country
            if "fsl_kra_per_address_1" in i:
                address.fsl_kra_per_address_1 = i["fsl_kra_per_address_1"]
                data_dict["fsl_kra_per_address_1"]=address.fsl_kra_per_address_1
            if "fsl_kra_per_address_2" in i:
                address.fsl_kra_per_address_2 = i["fsl_kra_per_address_2"]
                data_dict["fsl_kra_per_address_2"]=address.fsl_kra_per_address_2
            if "fsl_kra_per_address_3" in i:
                address.fsl_kra_per_address_3 = i["fsl_kra_per_address_3"]
                data_dict["fsl_kra_per_address_3"]=address.fsl_kra_per_address_3
            if "fsl_kra_per_city" in i:
                address.fsl_kra_per_city = i["fsl_kra_per_city"]
                data_dict["fsl_kra_per_city"]=address.fsl_kra_per_city
            if "fsl_kra_per_country" in i:
                address.fsl_kra_per_country = i["fsl_kra_per_country"]
                data_dict["fsl_kra_per_country"]=address.fsl_kra_per_country
            if "fsl_kra_per_pin" in i:
                address.fsl_kra_per_pin = i["fsl_kra_per_pin"]
                data_dict["fsl_kra_per_pin"]=address.fsl_kra_per_pin
            if "fsl_kra_per_state" in i:
                address.fsl_kra_per_state = i["fsl_kra_per_state"] 
                data_dict["fsl_kra_per_state"]=address.fsl_kra_per_state
            if "fsl_kra_address_proof" in i: 
                address.fsl_kra_address_proof = i["fsl_kra_address_proof"]
                data_dict["fsl_kra_address_proof"]=address.fsl_kra_address_proof
            if "fsl_kra_proof_idnumber" in i:
                address.fsl_kra_proof_idnumber = i["fsl_kra_proof_idnumber"]
                data_dict["fsl_kra_proof_idnumber"]=address.fsl_kra_proof_idnumber
            if "fsl_from_opportunity" in i:
                address.fsl_from_opportunity = i["fsl_from_opportunity"]
                data_dict["fsl_from_opportunity"]=address.fsl_from_opportunity
            if "fsl_kra_per_address_3" in i:
                address.fsl_kra_per_address_3 = i["fsl_kra_per_address_3"]
                data_dict["fsl_kra_per_address_3"]=address.fsl_kra_per_address_3
            if "fsl_kra_pin" in i:
                address.fsl_kra_pin = i["fsl_kra_pin"]
                data_dict["fsl_kra_pin"]=address.fsl_kra_pin
            # if data["fsl_from_lead"]:
            #     address.fsl_from_lead = data["fsl_from_lead"]
            if "fsl_kra_state" in i:
                address.fsl_kra_state = i["fsl_kra_state"]
                data_dict["fsl_kra_state"]=address.fsl_kra_state
            if "fsl_from_customer" in i:
                address.fsl_from_customer = i["fsl_from_customer"]
                data_dict["fsl_from_customer"]=address.fsl_from_customer
            if "fsl_kra_push_needed" in i:
                address.fsl_kra_push_needed = i["fsl_kra_push_needed"]
                data_dict["fsl_kra_push_needed"]=address.fsl_kra_push_needed
            if "fsl_kra_mobile_number" in i:
                address.fsl_kra_mobile_number = i["fsl_kra_mobile_number"]
                data_dict["fsl_kra_mobile_number"]=address.fsl_kra_mobile_number
            if "fsl_kra_email_id" in i:
                address.fsl_kra_email_id = i["fsl_kra_email_id"]  
                data_dict["fsl_kra_email_id"]=address.fsl_kra_email_id
            
            address.save()
            # tot_data.append(data)address
            frappe.response["message"] = {
                "id":address.name,
                "success_key":Success,
                "data":data_dict
                }
        # except:
        #     frappe.local.response["error"] = {
        #                     "error": "Opportunity not found"
        #                 }
