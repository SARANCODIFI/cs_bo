

# Copyright (c) 2023, White Hat Global and contributors
# For license information, please see license.txt
# 
from __future__ import unicode_literals
import frappe
from frappe import auth
import json
from frappe.utils import floor, flt, today, cint
from frappe import _
from frappe.core.doctype.user.user import generate_keys
from frappe.utils.password import get_decrypted_password

from cryptography.fernet import Fernet

# Function to encrypt the API secret
# def encrypt_secret(api_secret, encryption_key):
#     cipher_suite = Fernet(encryption_key)
#     encrypted_secret = cipher_suite.encrypt(api_secret.encode())
#     return encrypted_secret
# @frappe.whitelist(allow_guest=True)
# def sign_up(email: str, full_name: str, redirect_to: str) -> tuple[int, str]:
# @frappe.whitelist( allow_guest=True )
# def fun(email,password):
#     login(email,password)
    
    

@frappe.whitelist(allow_guest=True)
def login(email,password):
    try:
        frappe.errprint(email)
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=email, pwd=password)
        login_manager.post_login()
        user = frappe.get_doc('User',email)
        frappe.errprint(user.name)
        doc = frappe.get_doc("User Secret",user.name)
        frappe.errprint(doc.name)
        secret = doc.secret
        frappe.errprint("1")
        # api_generate = generate_keys(email)
        # user_document = frappe.get_doc('User', email)

        # Get the decrypted password for the 'api_secret' field
        # decrypted_secret = frappe.utils.password.get_decrypted_password(
        #     "User", user_document, fieldname="api_secret"
        # )
        token = "token "+str(user.api_key)+":"+str(secret)

        
        frappe.local.response["message"] = {
        "success_key": 1,
        "data": {  
            "user":email,
            "Role": user.role_profile_name,
            "type":"Logged In",
            "token":token,
            "api_secret":secret,
            # "api_key":user1.api_key,
            # "api_secret":decrypted_secret,
            "sid": frappe.session.sid,
            "system_user":"yes"
            
        }}
    except frappe.exceptions.AuthenticationError:
        frappe.local.response["message"] = {
        "success_key": 0,
        "error": {
            "message": "Invalid Credentials, Authentication Failed"
        }
    }
    

# @frappe.whitelist(allow_guest=True)
# def generate_keys(user):
#     user_details = frappe.get_doc("User",user)
#     api_secret = frappe.generate_hash(length=15)
    
#     if not user_details.api_key:
#         api_key = frappe.generate_hash(length=15)
#         user_details.api_key = api_key
#     else:
#         api_key = user_details.api_key
#         # user_details.api_key = api_key
#         # user_details.api_secret = api_secret
#     # user_details.save()
#     frappe.db.set_value('User', user, 'api_key', api_key)
#     frappe.db.set_value('User', user, 'api_secret',api_secret)
#     frappe.db.commit()

#     return [api_secret,api_key]
    


# @frappe.whitelist()
# def generate_keys(user):
    
#   """
#   generate api key and api secret

#   :param user: str
#   """
#   # frappe.only_for("System Manager")
 
#   user_details = frappe.get_doc("User", user)
#   api_secret = frappe.generate_hash(length=15)
#   # if api key is not set generate api key
#   if not user_details.api_key:
#       api_key = frappe.generate_hash(length=15)
#       user_details.api_key = api_key
#   user_details.api_secret = api_secret
#   user_details.save()
    

#   return [api_secret,api_key]


# def generate_keys(email):
#     user_details = frappe.get_doc('User', email)
#     frappe.errprint(user_details.middle_name)
#     user_details.save()
#     api_secret = frappe.generate_hash(length=15)

#     if not user_details.api_key:
#         api_key = frappe.generate_hash(length=15)
#         user_details.api_key = api_key
#         user_details.save()
#         frappe.errprint(user_details.api_key)

#     user_details.api_secret = api_secret
    
#     try:
#         user_details.save()
#         frappe.db.commit()
#         frappe.errprint(user_details.api_secret)
#         return [user_details.api_secret, user_details.api_key]
#     except Exception as e:
#         frappe.errprint(f"Error saving user details: {str(e)}")
#         return "Error generating keys"
    # user2= frappe.new_doc("User Permission")
    # user2.update(
    #   {
    #       "user": email,
    #       "allow": "Agent",
    #       "for_value": phone
    #   }
    # )
    # user2.insert() 
# def generate_keys(user):
#     user_details = frappe.get_doc('User', user)
#     api_secret = frappe.generate_hash(length=15)

#     if not user_details.api_key:
#         api_key = frappe.generate_hash(length=15)
#         user_details.api_key = api_key
#     user_details.api_secret = api_secret
#     user_details.save()
#     return api_secret

# @frappe.whitelist( allow_guest=True )
# def login1(email, password,name,phone):
#     login_manager = frappe.auth.LoginManager()
#     login_manager.authenticate(user=email, pwd=password)
#     login_manager.post_login()
   
#     agent1= frappe.new_doc("Agent")
#     agent1.update(
#         {
#                 "name": name,
#                 "agent_name": name,
#                 "phone_number": phone,
#                 "email_address": email,
#                 "password": password  
#         }
#     )
#     agent1.insert()
#     user2= frappe.new_doc("User Permission")
#     user2.update(
#       {
#           "user": email,
#           "allow": "Agent",
#           "for_value": phone
#       }
  
#   )
#     user2.insert()
    
#     api_generate = generate_keys(frappe.session.user)
#     user = frappe.get_doc('User',email)
#     user_permission(phone,email)
#     frappe.local.response["message"] = {
#         "success_key": 1,
#         "error": {
#             "code": 200,
#             "message": "Authentication Success"
#         },
#         "data": {
#             "sid": frappe.session.sid,
#             "api_secret":api_generate[0],
#             "api_key":api_generate[1],
#             # "username":user.username,
#             "email":user.email,
#             "user_image":user.user_image,s
#             "roles":"Agent"
#         }
#     }
    
#     # create_agent(email,password,name,phone)


# @frappe.whitelist( allow_guest=True )      
# def user_permission(phone,email):
#     agent_per = frappe.get_doc("User",email)
#     agent_per.update(
#         {
#             "role_profile_name":"Agent",
#             "user_type":"System User",
#             "module_profile":"Agent",
#             "roles": [
#                 {
#                     "role": "Agent"
#                 }
#             ]
#         }
#     )
#     agent_per.db_update()

