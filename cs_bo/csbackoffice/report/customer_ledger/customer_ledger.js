// Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
// For license information, please see license.txt
/* eslint-disable */
const toDate = frappe.datetime.get_today();
const fromDate = frappe.datetime.add_days(toDate, -30);
frappe.query_reports["Customer Ledger"] = {
	
	"filters": [
		{
			fieldname: "ucc",
			label: __("Customer Code"),
			fieldtype: "Link",
			options: "Customer",
			// default: frappe.defaults.get_user_default("Company"),
		},
		{
			fieldname: "from_date",
			label: __("From Date"),
			fieldtype: "Date",
			"default": fromDate
			
		},
		{
			fieldname: "to_date",
			label: __("To Date"),
			fieldtype: "Date",
			"default": frappe.datetime.get_today()
			
		}
	]
};
