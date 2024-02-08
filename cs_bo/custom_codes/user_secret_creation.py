from __future__ import unicode_literals
import frappe
from frappe import auth
import json
from frappe.utils import floor, flt, today, cint
from frappe import _
from frappe.core.doctype.user.user import generate_keys

from cryptography.fernet import Fernet

@frappe.whitelist(allow_guest=True)
def generate_key(user):
    frappe.errprint("in fun")
    key = generate_keys(user)
    frappe.errprint(key)
    
    # frappe.errprint(new1.name)
    frappe.errprint(key['api_secret'])
    if (frappe.db.exists("User Secret",{"name":user})):
        frappe.errprint("if")
        doc = frappe.get_doc("User Secret",user)
        doc.secret = key['api_secret']
        doc.save()
    else:
        frappe.errprint("else")
        new1 = frappe.new_doc("User Secret")
        new1.user = user
        new1.secret = key['api_secret']
        new1.insert()
    # user_roles = frappe.get_roles(user)
    # if 'System Manager' in user_roles:
    #     user = frappe.session.user
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
    #     frappe.errprint("completed")
    #     return [api_secret,api_key]
        
        

@frappe.whitelist(allow_guest=True)
def generate(self,event):
    frappe.errprint("hi")