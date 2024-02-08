import frappe
import random

@frappe.whitelist(allow_guest=True)
def create_support_code(self,event):   
    self.fsl_support_code = str(random.randint(1000, 9999))

    self.save() 
    frappe.errprint("customer updated")
        
@frappe.whitelist(allow_guest=True)
def create_support_code_alreadyexist(): 
        cust=frappe.get_all("Customer")

        for i in cust:
            name1 = i.name
            if i<100:
                create_code(name1)
            else:
                break
            # cus.fsl_support_code = str(random.randint(1000, 9999))
            # cus.save()
        frappe.errprint("final Success")

@frappe.whitelist(allow_guest=True)
def create_code(name1):   
    create_code(name1)
    cus = frappe.get_doc("Customer",name1)
    cus.fsl_support_code = str(random.randint(1000, 9999))
    cus.save()
    frappe.errprint("Success")
