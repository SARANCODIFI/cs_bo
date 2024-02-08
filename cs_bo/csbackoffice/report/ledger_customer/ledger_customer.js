frappe.ui.form.on('Ledger Customer', {
    "filters": [
		{
			fieldname: "ucc",
			label: __("Customer Code"),
			fieldtype: "Link",
			options: "Customer",
			// default: frappe.defaults.get_user_default("Company"),
		}
		]
});
