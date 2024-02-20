import frappe

@frappe.whitelist(allow_guest=True)
def hd_ticket_creation(self, event):  
    if self.email_account == "RMS1":
        subject = self.subject
        raised_by = self.sender
        description = self.content
        
        hd_ticket = frappe.new_doc("HD Ticket")

        hd_ticket.update({
            "fsl_source": "Mail",
            "subject": subject,
            "raised_by": raised_by,
            "description": description
        })

        if frappe.db.exists("Customer", {'email_id' : raised_by}):
            hd_ticket.customer = frappe.db.get_value('Customer', {'email_id':raised_by }, ['name'])

        if frappe.db.exists("Employee", {'user_id' : raised_by}):
            hd_ticket.employee = frappe.db.get_value('Employee', {'user_id':raised_by }, ['name'])

        hd_ticket.insert(ignore_permissions=True,ignore_mandatory=True)
        frappe.db.commit()
        frappe.errprint("HD Ticket updated")
