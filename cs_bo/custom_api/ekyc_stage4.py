from frappe import _
import json

import frappe

@frappe.whitelist()

def get_customer_profile(opportunity):
    try:
        customer_profile = frappe.get_last_doc("Customer Profile",filters={'fsl_from_opportunity': opportunity})
        oppr = frappe.get_doc("Opportunity",opportunity)
#             ["active_status", "legal_action_statement", "annual_income", "applicant_name", "application_id","fatca","father_name","mother_name","gender","legal_action",
# "marital_status","net_worth","net_worth_date","occupation","political_exposure","settlement_cycle","standinginstructios","standing_instruction_one","standing_instruction_two",
# "standing_instruction_three","standing_instruction_four","standing_instruction_five","standing_instruction_six","standing_instruction_seven","standing_instruction_eight","standing_instruction_nine","standing_instruction_ten","standing_instruction_eleven","standing_instruction_twelve","title","tax_outside_india","trading_experience"])
        # tot_data ={}
        tot_data=customer_profile  # Use the fetched data directly

        frappe.response["message"] = {
            "Success_key" : "1",
            "data": {
                "created_on":customer_profile.creation,
                "active_status":customer_profile.active_status,
                "legal_action_statement":customer_profile.legal_action_statement,
                "annual_income":customer_profile.annual_income,
                "applicant_name":customer_profile.applicant_name,
                "application_id":customer_profile.application_id,
                "fatca":customer_profile.fatca,
                "father_name":customer_profile.father_name,
                "mother_name":customer_profile.mother_name,
                "gender":customer_profile.gender,
                "legal_action":customer_profile.legal_action,
                "marital_status":customer_profile.marital_status,
                "net_worth":customer_profile.net_worth,
                "net_worth_date":customer_profile.net_worth_date,
                "occupation":customer_profile.occupation,
                "political_exposure":customer_profile.political_exposure,
                "settlement_cycle":customer_profile.settlement_cycle,
                "standinginstructios":customer_profile.standinginstructios,
                "standing_instruction_one":customer_profile.standing_instruction_one,
                "standing_instruction_two":customer_profile.standing_instruction_two,
                "standing_instruction_three":customer_profile.standing_instruction_three,
                "standing_instruction_four":customer_profile.standing_instruction_four,
                "standing_instruction_five":customer_profile.standing_instruction_five,
                "standing_instruction_six":customer_profile.standing_instruction_six,
                "standing_instruction_seven":customer_profile.standing_instruction_seven,
                "standing_instruction_eight":customer_profile.standing_instruction_eight,
                "standing_instruction_nine":customer_profile.standing_instruction_nine,
                "standing_instruction_ten":customer_profile.standing_instruction_ten,
                "standing_instruction_eleven":customer_profile.standing_instruction_eleven,
                "standing_instruction_twelve":customer_profile.standing_instruction_twelve,
                "title":customer_profile.title,
                "tax_outside_india":customer_profile.tax_outside_india,
                "trading_experience":customer_profile.trading_experience,
                "trackwizz_passkey":customer_profile.trackwizz_passkey   
            }
        }
    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }


# @frappe.whitelist(allow_guest=True)
# def update_customer_profile(data):
#     for i in data:
#         try:
#             Customer_Profile = frappe.get_last_doc("Customer Profile",filters={"fsl_from_opportunity":i["opportunity"]}) 
#             if Customer_Profile:
#                 for datas in i:
#                     Customer_Profile.update({
#                         datas : i[datas]
#                     })
#                     # data["opportunity"] = str(data["opportunity"])
#                 Customer_Profile.save()
#                 frappe.response["message"] = {
#                     "success_key" : 1,
#                     "data": i
                    
#                 }
#             else:
#                 frappe.response["message"] = {
#                 "error":"customer profile Not Exists"
#             }
               
#         except:
#             frappe.response["message"] = {
#                 "error":"Not Updated"
#             }
        

# @frappe.whitelist(allow_guest=True)
# def update_customer_profile(data):
#     for i in data:
         
#         frappe.errprint(i["opportunity"])
#         if isinstance(data, dict):
#             opportunity = data["opportunity"]
            
#             if opportunity is not None:
#                 Customer_Profile = frappe.get_last_doc("Customer Profile", filters={"opportunity": opportunity})
                
#                 if Customer_Profile:
#                     for key, value in data.items():
#                         Customer_Profile.set(key, value)
                    
#                     Customer_Profile.save()
#                     frappe.response["message"] = {
#                         "data": Customer_Profile.as_dict()
#                     }
#                     return
#                 else:
#                     frappe.response["message"] = {
#                     "error": "Customer profile not found"
#                     }
#                     return
#             else:
#                 frappe.response["message"] = {
#                     "error": "Opportunity not provided in data"
#                 }
#         else:
#             frappe.response["message"] = {
#                 "error": "Data is not a dictionary"
#             }




# @frappe.whitelist(allow_guest=True)
# def post_customer_profile(data):  
#     try:
#             Customer_Profile = frappe.new_doc("Customer Profile")
#             Customer_Profile.active_status = data["active_status"]
#             Customer_Profile.legal_action_statement = data["legal_action_statement"]
#             Customer_Profile.annual_income = data["annual_income"]  
#             Customer_Profile.applicant_name = data["applicant_name"]
#             # Customer_Profile.application_id = data["application_id"]
#             Customer_Profile.fatca = data["fatca"]
#             Customer_Profile.father_name = data["father_name"]
#             Customer_Profile.mother_name = data["mother_name"]
#             Customer_Profile.gender = data["gender"]  
#             Customer_Profile.legal_action = data["legal_action"]
#             Customer_Profile.marital_status = data["marital_status"]
#             Customer_Profile.net_worth = data["net_worth"]
#             Customer_Profile.net_worth_date = data["net_worth_date"]
#             Customer_Profile.occupation = data["occupation"]
#             Customer_Profile.political_exposure = data["political_exposure"]  
#             Customer_Profile.settlement_cycle = data["settlement_cycle"]
#             Customer_Profile.standinginstructios = data["standinginstructios"]
#             Customer_Profile.standing_instruction_one = data["standing_instruction_one"]
#             Customer_Profile.standing_instruction_two = data["standing_instruction_two"]
#             Customer_Profile.standing_instruction_three = data["standing_instruction_three"]
#             Customer_Profile.standing_instruction_four = data["standing_instruction_four"]  
#             Customer_Profile.standing_instruction_five = data["standing_instruction_five"]
#             Customer_Profile.standing_instruction_six = data["standing_instruction_six"]
#             Customer_Profile.standing_instruction_seven = data["standing_instruction_seven"]
#             Customer_Profile.standing_instruction_eight = data["standing_instruction_eight"]
#             Customer_Profile.standing_instruction_nine = data["standing_instruction_nine"]
#             Customer_Profile.standing_instruction_ten = data["standing_instruction_ten"]  
#             Customer_Profile.standing_instruction_eleven = data["standing_instruction_eleven"]
#             Customer_Profile.standing_instruction_twelve = data["standing_instruction_twelve"]
#             Customer_Profile.standing_instruction_one = data["standing_instruction_one"]
#             Customer_Profile.title = data["title"]
#             Customer_Profile.tax_outside_india = data["tax_outside_india"]
#             Customer_Profile.trading_experience = data["trading_experience"]  
#             Customer_Profile.save()
            
#             data1 = {
#                 "active_status" : Customer_Profile.active_status,
#                 "legal_action_statement" : Customer_Profile.legal_action_statement,
#                 "annual_income" : Customer_Profile.annual_income,
#                 "applicant_name" : Customer_Profile.applicant_name,
#                 # "application_id" : Customer_Profile.application_id,
#                 "fatca" :Customer_Profile.fatca,
#                 "father_name" : Customer_Profile.father_name,
#                 "mother_name" : Customer_Profile.mother_name,
#                 "legal_action" : Customer_Profile.legal_action,
#                 "marital_status" : Customer_Profile.marital_status,
#                 "net_worth" : Customer_Profile.net_worth,
#                 "net_worth_date" :Customer_Profile.net_worth_date,
#                 "occupation" : Customer_Profile.occupation,
#                 "political_exposure" : Customer_Profile.political_exposure,
#                 "settlement_cycle" : Customer_Profile.settlement_cycle,
#                 "standinginstructios" : Customer_Profile.standinginstructios,
#                 "standing_instruction_one" : Customer_Profile.standing_instruction_one,
#                 "standing_instruction_two" :Customer_Profile.standing_instruction_two,
#                 "standing_instruction_three" : Customer_Profile.standing_instruction_three,
#                 "standing_instruction_four" : Customer_Profile.standing_instruction_four,
#                 "standing_instruction_five" : Customer_Profile.standing_instruction_five,
#                 "standing_instruction_six" : Customer_Profile.standing_instruction_six,
#                 "standing_instruction_seven" : Customer_Profile.standing_instruction_seven,
#                 "standing_instruction_eight" :Customer_Profile.standing_instruction_eight,
#                 "standing_instruction_nine" :Customer_Profile.standing_instruction_nine,
#                 "standing_instruction_ten" : Customer_Profile.father_name,
#                 "standing_instruction_eleven" : Customer_Profile.standing_instruction_eleven,
#                 "standing_instruction_twelve" : Customer_Profile.standing_instruction_twelve,
#                 "title" : Customer_Profile.title,
#                 "tax_outside_india" : Customer_Profile.tax_outside_india,
#                 "trading_experience" :Customer_Profile.trading_experience
#             }
#             # tot_data.append(data)
#             frappe.response["message"] = {
#                 "success_key": 1,
#                 "id":Customer_Profile.name,
#                 "data":data1
#             }

#     except Exception as e:
#         # Initialize frappe.local.response as an empty dictionary
#         frappe.local.response = {}
#         frappe.local.response["message"] = {
#             "error": f"An error occurred: {str(e)}"
#         }


###################### latest code ##################


@frappe.whitelist()
def post_customer_profile(data):

    datas ={}  
    # data = data.get("Customer Profile")
    for i in data:
            Success = 0         
            # Customer_Profile = frappe.get_last_doc("Customer Profile", filters={'data': data})
            try:
                Customer_Profile = frappe.get_last_doc("Customer Profile",filters={"fsl_from_opportunity":i["fsl_from_opportunity"]}) 
                datas["fsl_from_opportunity"] = i["fsl_from_opportunity"]           
                if Customer_Profile:
                    Success = 1
                    # Customer_Profile = frappe.new_doc("Customer Profile")
                    if "active_status" in i:
                        Customer_Profile.active_status = i["active_status"]
                        datas["active_status"] = i["active_status"]
                    if "legal_action_statement" in i:
                        Customer_Profile.legal_action_statement = i["legal_action_statement"]
                        datas["legal_action_statement"] = i["legal_action_statement"]
                    if "annual_income" in i:
                        Customer_Profile.annual_income = i["annual_income"]
                        datas["annual_income"] = i["annual_income"]
                    if "applicant_name" in i:
                        Customer_Profile.applicant_name = i["applicant_name"]
                        datas["applicant_name"] = i["applicant_name"]
                    if "application_id" in i:
                        Customer_Profile.application_id = i["application_id"]
                        datas["application_id"] = i["application_id"]
                    if "fatca" in i:
                        Customer_Profile.fatca = i["fatca"]
                        datas["fatca"] = i["fatca"]
                    if "father_name" in i:
                        Customer_Profile.father_name = i["father_name"]
                        datas["father_name"] = i["father_name"]


                    if "mother_name" in i:
                        Customer_Profile.mother_name = i["mother_name"]
                        datas["mother_name"] = i["mother_name"]

                    if "gender" in i:
                        Customer_Profile.gender = i["gender"]
                        datas["gender"] = i["gender"]

                    if "legal_action" in i:
                        Customer_Profile.legal_action = i["legal_action"]
                        datas["legal_action"] = i["legal_action"]
                        
                    if "marital_status" in i:
                        Customer_Profile.marital_status = i["marital_status"]
                        datas["marital_status"] = i["marital_status"]

                    if "net_worth" in i:
                        Customer_Profile.net_worth = i["net_worth"]
                        datas["net_worth"] = i["net_worth"]

                    if "net_worth_date" in i:
                        Customer_Profile.net_worth_date = i["net_worth_date"]
                        datas["net_worth_date"] = i["net_worth_date"]

                    if "occupation" in i:
                        Customer_Profile.occupation = i["occupation"]
                        datas["occupation"] = i["occupation"]

                    if "political_exposure" in i:
                        Customer_Profile.political_exposure = i["political_exposure"]
                        datas["political_exposure"] = i["political_exposure"]

                    if "settlement_cycle" in i:
                        Customer_Profile.settlement_cycle = i["settlement_cycle"]
                        datas["settlement_cycle"] = i["settlement_cycle"]

                    if "standinginstructios" in i:
                        Customer_Profile.standinginstructios = i["standinginstructios"]
                        datas["standinginstructios"] = i["standinginstructios"]

                    if "standing_instruction_one" in i:
                        Customer_Profile.standing_instruction_one = i["standing_instruction_one"]
                        datas["standing_instruction_one"] = i["standing_instruction_one"]

                    if "standing_instruction_two" in i:
                        Customer_Profile.standing_instruction_two = i["standing_instruction_two"]
                        datas["standing_instruction_two"] = i["standing_instruction_two"]

                    if "standing_instruction_three" in i:
                        Customer_Profile.standing_instruction_three = i["standing_instruction_three"]
                        datas["standing_instruction_three"] = i["standing_instruction_three"]
                        
                    if "standing_instruction_four" in i:
                        Customer_Profile.standing_instruction_four = i["standing_instruction_four"]
                        datas["standing_instruction_four"] = i["standing_instruction_four"]

                    if "standing_instruction_five" in i:
                        Customer_Profile.standing_instruction_five = i["standing_instruction_five"]
                        datas["standing_instruction_five"] = i["standing_instruction_five"]

                    if "standing_instruction_six" in i:
                        Customer_Profile.standing_instruction_six = i["standing_instruction_six"]
                        datas["standing_instruction_six"] = i["standing_instruction_six"]

                    if "standing_instruction_seven" in i:
                        Customer_Profile.standing_instruction_seven = i["standing_instruction_seven"]
                        datas["standing_instruction_seven"] = i["standing_instruction_seven"]

                    if "standing_instruction_eight" in i:
                        Customer_Profile.standing_instruction_eight = i["standing_instruction_eight"]
                        datas["standing_instruction_eight"] = i["standing_instruction_eight"]

                    if "standing_instruction_nine" in i:
                        Customer_Profile.standing_instruction_nine = i["standing_instruction_nine"]
                        datas["standing_instruction_nine"] = i["standing_instruction_nine"]

                    if "standing_instruction_ten" in i:
                        Customer_Profile.standing_instruction_ten = i["standing_instruction_ten"]
                        datas["standing_instruction_ten"] = i["standing_instruction_ten"]

                    if "standing_instruction_eleven" in i:
                        Customer_Profile.standing_instruction_eleven = i["standing_instruction_eleven"]
                        datas["standing_instruction_eleven"] = i["standing_instruction_eleven"]

                    if "standing_instruction_twelve" in i:
                        Customer_Profile.standing_instruction_twelve = i["standing_instruction_twelve"]
                        datas["standing_instruction_twelve"] = i["standing_instruction_twelve"]

                    if "title" in i:
                        Customer_Profile.title = i["title"]
                        datas["title"] = i["title"]

                    if "tax_outside_india" in i:
                        Customer_Profile.tax_outside_india = i["tax_outside_india"]
                        datas["tax_outside_india"] = i["tax_outside_india"]

                    if "trading_experience" in i:
                        Customer_Profile.trading_experience = i["trading_experience"]
                        datas["trading_experience"] = i["trading_experience"]
                        
                    if "trackwizz_passkey" in i:
                        Customer_Profile.trackwizz_passkey = i["trackwizz_passkey"]
                        datas["trackwizz_passkey"] = i["trackwizz_passkey"]
                        
                    Customer_Profile.save()

                    frappe.response["message"] = {
                            "Success": Success,
                            "message": " Customer Profile Update.",
                            "data": datas
                        
                        }
            except Exception as e:
                    Success = 1
                    Customer_Profile = frappe.new_doc("Customer Profile")
                    datas["fsl_from_opportunity"] = i["fsl_from_opportunity"]
                    
                    try:
                        Customer_Profile.fsl_from_opportunity = i["fsl_from_opportunity"]
                        if "active_status" in i:
                            Customer_Profile.active_status = i["active_status"]
                            datas["active_status"] = i["active_status"]
                        if "legal_action_statement" in i:
                            Customer_Profile.legal_action_statement = i["legal_action_statement"]
                            datas["legal_action_statement"] = i["legal_action_statement"]
                        if "annual_income" in i:
                            Customer_Profile.annual_income = i["annual_income"]
                            datas["annual_income"] = i["annual_income"]
                        if "applicant_name" in i:
                            Customer_Profile.applicant_name = i["applicant_name"]
                            datas["applicant_name"] = i["applicant_name"]
                        if "application_id" in i:
                            Customer_Profile.application_id = i["application_id"]
                            datas["application_id"] = i["application_id"]
                        if "fatca" in i:
                            Customer_Profile.fatca = i["fatca"]
                            datas["fatca"] = i["fatca"]
                        if "father_name" in i:
                            Customer_Profile.father_name = i["father_name"]
                            datas["father_name"] = i["father_name"]


                        if "mother_name" in i:
                            Customer_Profile.mother_name = i["mother_name"]
                            datas["mother_name"] = i["mother_name"]

                        if "gender" in i:
                            Customer_Profile.gender = i["gender"]
                            datas["gender"] = i["gender"]

                        if "legal_action" in i:
                            Customer_Profile.legal_action = i["legal_action"]
                            datas["legal_action"] = i["legal_action"]
                            
                        if "marital_status" in i:
                            Customer_Profile.marital_status = i["marital_status"]
                            datas["marital_status"] = i["marital_status"]

                        if "net_worth" in i:
                            Customer_Profile.net_worth = i["net_worth"]
                            datas["net_worth"] = i["net_worth"]

                        if "net_worth_date" in i:
                            Customer_Profile.net_worth_date = i["net_worth_date"]
                            datas["net_worth_date"] = i["net_worth_date"]

                        if "occupation" in i:
                            Customer_Profile.occupation = i["occupation"]
                            datas["occupation"] = i["occupation"]

                        if "political_exposure" in i:
                            Customer_Profile.political_exposure = i["political_exposure"]
                            datas["political_exposure"] = i["political_exposure"]

                        if "settlement_cycle" in i:
                            Customer_Profile.settlement_cycle = i["settlement_cycle"]
                            datas["settlement_cycle"] = i["settlement_cycle"]

                        if "standinginstructios" in i:
                            Customer_Profile.standinginstructios = i["standinginstructios"]
                            datas["standinginstructios"] = i["standinginstructios"]

                        if "standing_instruction_one" in i:
                            Customer_Profile.standing_instruction_one = i["standing_instruction_one"]
                            datas["standing_instruction_one"] = i["standing_instruction_one"]

                        if "standing_instruction_two" in i:
                            Customer_Profile.standing_instruction_two = i["standing_instruction_two"]
                            datas["standing_instruction_two"] = i["standing_instruction_two"]

                        if "standing_instruction_three" in i:
                            Customer_Profile.standing_instruction_three = i["standing_instruction_three"]
                            datas["standing_instruction_three"] = i["standing_instruction_three"]
                            
                        if "standing_instruction_four" in i:
                            Customer_Profile.standing_instruction_four = i["standing_instruction_four"]
                            datas["standing_instruction_four"] = i["standing_instruction_four"]

                        if "standing_instruction_five" in i:
                            Customer_Profile.standing_instruction_five = i["standing_instruction_five"]
                            datas["standing_instruction_five"] = i["standing_instruction_five"]

                        if "standing_instruction_six" in i:
                            Customer_Profile.standing_instruction_six = i["standing_instruction_six"]
                            datas["standing_instruction_six"] = i["standing_instruction_six"]

                        if "standing_instruction_seven" in i:
                            Customer_Profile.standing_instruction_seven = i["standing_instruction_seven"]
                            datas["standing_instruction_seven"] = i["standing_instruction_seven"]

                        if "standing_instruction_eight" in i:
                            Customer_Profile.standing_instruction_eight = i["standing_instruction_eight"]
                            datas["standing_instruction_eight"] = i["standing_instruction_eight"]

                        if "standing_instruction_nine" in i:
                            Customer_Profile.standing_instruction_nine = i["standing_instruction_nine"]
                            datas["standing_instruction_nine"] = i["standing_instruction_nine"]

                        if "standing_instruction_ten" in i:
                            Customer_Profile.standing_instruction_ten = i["standing_instruction_ten"]
                            datas["standing_instruction_ten"] = i["standing_instruction_ten"]

                        if "standing_instruction_eleven" in i:
                            Customer_Profile.standing_instruction_eleven = i["standing_instruction_eleven"]
                            datas["standing_instruction_eleven"] = i["standing_instruction_eleven"]

                        if "standing_instruction_twelve" in i:
                            Customer_Profile.standing_instruction_twelve = i["standing_instruction_twelve"]
                            datas["standing_instruction_twelve"] = i["standing_instruction_twelve"]

                        if "title" in i:
                            Customer_Profile.title = i["title"]
                            datas["title"] = i["title"]

                        if "tax_outside_india" in i:
                            Customer_Profile.tax_outside_india = i["tax_outside_india"]
                            datas["tax_outside_india"] = i["tax_outside_india"]

                        if "trading_experience" in i:
                            Customer_Profile.trading_experience = i["trading_experience"]
                            datas["trading_experience"] = i["trading_experience"]
                            
                        if "trackwizz_passkey" in i:
                            Customer_Profile.trackwizz_passkey = i["trackwizz_passkey"]
                            datas["trackwizz_passkey"] = i["trackwizz_passkey"]
                        
                        Customer_Profile.save()

                        frappe.response["message"] = {
                                "Success": Success,
                                "message": " Customer Profile Created.",
                                "data":datas
                            }
                    except:
                        frappe.local.response["error"] = {
                            "error": "Opportunity not found"
                        }


    # else:
    #     frappe.response["message"] = {
    #         "Success": Success,
    #         "message": "Customer Profile not found"
    #     }


# @frappe.whitelist(allow_guest=True)
# def post_customer_profile(data):
#     data = data.get("Customer Profile")
#     Success = 0
#     Customer_Profile = frappe.get_last_doc("Customer Profile", filters={'fsl_from_opportunity': data})
    
#     if not Customer_Profile:
#         Customer_Profile = frappe.new_doc("Customer Profile")

#     if "active_status" in data:
#         Customer_Profile.active_status = data["active_status"]
#     if "legal_action_statement" in data:
#         Customer_Profile.legal_action_statement = data["legal_action_statement"]
#     if "annual_income" in data:
#         Customer_Profile.annual_income = data["annual_income"]
#     if "applicant_name" in data:
#         Customer_Profile.applicant_name = data["applicant_name"]
#     if "application_id" in data:
#         Customer_Profile.application_id = data["application_id"]
#     if "fatca" in data:
#         Customer_Profile.fatca = data["fatca"]
#     if "father_name" in data:
#         Customer_Profile.father_name = data["father_name"]
#     if "mother_name" in data:
#         Customer_Profile.mother_name = data["mother_name"]
#     if "gender" in data:
#         Customer_Profile.gender = data["gender"]
#     if "legal_action" in data:
#         Customer_Profile.legal_action = data["legal_action"]
#     if "marital_status" in data:
#         Customer_Profile.marital_status = data["marital_status"]
#     if "net_worth" in data:
#         Customer_Profile.net_worth = data["net_worth"]
#     if "net_worth_date" in data:
#         Customer_Profile.net_worth_date = data["net_worth_date"]
#     if "occupation" in data:
#         Customer_Profile.occupation = data["occupation"]
#     if "political_exposure" in data:
#         Customer_Profile.political_exposure = data["political_exposure"]
#     if "settlement_cycle" in data:
#         Customer_Profile.settlement_cycle = data["settlement_cycle"]
#     if "standinginstructios" in data:
#         Customer_Profile.standinginstructios = data["standinginstructios"]
#     if "standing_instruction_one" in data:
#         Customer_Profile.standing_instruction_one = data["standing_instruction_one"]
#     if "standing_instruction_two" in data:
#         Customer_Profile.standing_instruction_two = data["standing_instruction_two"]
#     if "standing_instruction_three" in data:
#         Customer_Profile.standing_instruction_three = data["standing_instruction_three"]
#     if "standing_instruction_four" in data:
#         Customer_Profile.standing_instruction_four = data["standing_instruction_four"]
#     if "standing_instruction_five" in data:
#         Customer_Profile.standing_instruction_five = data["standing_instruction_five"]
#     if "standing_instruction_six" in data:
#         Customer_Profile.standing_instruction_six = data["standing_instruction_six"]
#     if "standing_instruction_seven" in data:
#         Customer_Profile.standing_instruction_seven = data["standing_instruction_seven"]
#     if "standing_instruction_eight" in data:
#         Customer_Profile.standing_instruction_eight = data["standing_instruction_eight"]
#     if "standing_instruction_nine" in data:
#         Customer_Profile.standing_instruction_nine = data["standing_instruction_nine"]
#     if "standing_instruction_ten" in data:
#         Customer_Profile.standing_instruction_ten = data["standing_instruction_ten"]
#     if "standing_instruction_eleven" in data:
#         Customer_Profile.standing_instruction_eleven = data["standing_instruction_eleven"]
#     if "standing_instruction_twelve" in data:
#         Customer_Profile.standing_instruction_twelve = data["standing_instruction_twelve"]
#     if "title" in data:
#         Customer_Profile.title = data["title"]
#     if "tax_outside_india" in data:
#         Customer_Profile.tax_outside_india = data["tax_outside_india"]
#     if "trading_experience" in data:
#         Customer_Profile.trading_experience = data["trading_experience"]

#     Customer_Profile.save()

#     if Success == 1:
#         frappe.response["message"] = {
#             "Success": Success,
#             "message": "Customer Profile Updated."
#         }
#     else:
#         frappe.response["message"] = {
#             "Success": Success,
#             "message": "Customer Profile not found"
#         }
