import frappe
# from frappe.contacts.doctype.contact.contact import add_email

@frappe.whitelist(allow_guest=True)
def customer_contact_update(id, mobile=None, email_id=None):
    try:
        # frappe.errprint("try")

        customer = frappe.get_doc('Customer', id)

        primary_contact = customer.get('customer_primary_contact')

        contact_doc = frappe.get_doc('Contact', primary_contact)

        if contact_doc:
            if email_id:
                p_email_id = 0
                # frappe.errprint("bf_sv")
                for j in contact_doc.email_ids:
                    if j.is_primary == 1:
                        p_email_id = j.email_id
                #         frappe.errprint(j.email_id)
                # frappe.errprint("if if")
                
                contact_doc.append("email_ids",{
                "email_id" : email_id,
                "is_primary":0
                })
                
                for j in contact_doc.email_ids:
                    if j.email_id == p_email_id:
                        # frappe.errprint(j.email_id)
                        j.is_primary = 0
                        # frappe.errprint(j.is_primary)
                    else:
                        pass
                
                for j in contact_doc.email_ids:
                    if j.email_id == email_id:
                        # frappe.errprint(j.email_id)
                        j.is_primary = 1
                        # frappe.errprint(j.is_primary)

                contact_doc.save()
                # frappe.errprint("af sv")
                # for i in contact_doc.email_ids:
                    # frappe.errprint(i.email_id)
                frappe.db.commit()
                # frappe.msgprint("Email ID updated successfully!")
                frappe.response["message"] = {
                        "success_key": 1,
                        "ucc_code":customer.name,
                        "updated_email_id": email_id,
                    }
                # Optional: Display success message

            if mobile:
                p_phone = 0
                # frappe.errprint("bf sv")
                for j in contact_doc.phone_nos:
                    if j.is_primary_mobile_no == 1:
                        p_phone = j.phone
                    else:
                        pass
                #         frappe.errprint(j.phone)
                # frappe.errprint("if if")
                
                contact_doc.append("phone_nos",{
                "phone" : mobile,
                "is_primary_mobile_no":0
                })
                
                for j in contact_doc.phone_nos:
                    if j.phone == p_phone:
                        # frappe.errprint(j.phone)
                        j.is_primary_mobile_no = 0
                        # frappe.errprint(j.is_primary_mobile_no)
                
                for j in contact_doc.phone_nos:
                    if j.phone == mobile:
                        # frappe.errprint(j.phone)
                        j.is_primary_mobile_no = 1
                        # frappe.errprint(j.is_primary_mobile_no)

                contact_doc.save()
                # frappe.errprint("af sv")
                # for i in contact_doc.phone_nos:
                    # frappe.errprint(i.phone)
                frappe.db.commit()
                # frappe.msgprint("MOBILE updated successfully!") 
                frappe.response["message"] = {
                        "success_key": 1,
                        "ucc_code":customer.name,
                        "updated_mobile": mobile,
                    }

    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }




@frappe.whitelist(allow_guest=True)
def customer_contact_update1(id, mobile = None, email_id = None):
    try :
        customer = frappe.get_last_doc('Customer',filters={'name':id})

        contact_doc = customer.customer_primary_contact
        # primary = ""
        customer_contact = frappe.get_doc('Contact',contact_doc)
        frappe.errprint(customer_contact)
        if email_id is not None:
            frappe.errprint(email_id)
            for j in customer_contact.email_ids:
                frappe.errprint(j.email_id)
                # if j.is_primary == 1:
                #     primary = j.email_id
            #         frappe.errprint(j.email_id)
            #         frappe.errprint()
            new_email_id = customer_contact.append("email_ids", {})
            new_email_id.email_id = email_id
            new_email_id.is_primary = 1 
            # add_email(contact, email_id, is_primary=1)
            # customer_contact.append("email_ids",{
            #     "email_id" : email_id
            # })   
            frappe.errprint("before update")
            customer_contact.save()

            # for j in customer_contact.email_ids:
            #     frappe.errprint("jihji")

            #     if j.is_primary == 1:
            #         frappe.errprint(j.email_id)
            #         j.is_primary = 0
            #         frappe.errprint(j.is_primary )
            #         customer_contact.insert()
            #         frappe.db.commit()

            #         for i in customer_contact.email_ids:
            #             if i.email_id == email:
            #                 frappe.errprint(i.email_id)
            #                 i.is_primary = 1
            #                 customer_contact.insert()
            #                 frappe.db.commit()
            #                 frappe.errprint(i.is_primary )

                
                #     j.email_id = email
                #     j.save() 
                #     frappe.response["message"] = {
                #         "success_key": 1,
                #         "updated_email_id": j.email_id,
                #     }
                
                # else:
                #     frappe.response["message"] = {
                #     "success_key": 0,
                #     "error":"An Error Occured While Processing"
                #     }

        # customer = frappe.get_doc("Customer", id)
        # frappe.errprint(customer.mobile_no)
        # # Add the new mobile number to the existing mobile numbers list
        # customer.append("phone_nos", {
        #     "mobile": mobile,
        #     "is_primary_mobile_no": 0  # Set to 1 if it's the primary mobile number
        # })
        # if mobile is not None:

        #     for j in customer_contact.phone_nos:
                
        #         if j.is_primary_phone == 1:
                    
        #             j.phone = mobile
        #             j.save() 
        #             frappe.response["message"] = {
        #                 "success_key": 1,
        #                 "updated_phone_no": j.phone,
        #             }
                    
        #         elif j.is_primary_mobile_no == 1:
        #             j.phone = "1000567890"
        #             j.save()
        frappe.response["message"] = {
            "success_key": 1,
            # "email":customer.email
            "updated_phone_no": customer.mobile_no
        }

        #         else :
        #                 frappe.response["message"] = {
        #                 "success_key": 0,
        #                 "error":"An Error Occured While Processing"
        #                 }

        # else :
        #     frappe.local.response["message"] = {
        #             "error": "Customer Not Found"
        #         }

    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }