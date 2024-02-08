frappe.ui.form.on("Opportunity", {
	on_refresh: function(frm){
        console.log("here")
        frappe.msgprint("hiii")
    }
})