# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Tradebook(Document):
	pass

@frappe.whitelist(allow_guest=True)
def after_insert(self,event):
	frappe.errprint("after_insert")
	# all_doc= frappe.get_list("Tradebook",filters={'ucc':"SKY34914"})
	# for i in all_doc:
	# self = frappe.get_doc("Tradebook",i.name) 
	frappe.errprint(self.name)
	try:
		# frappe.errprint("try")
		trade_log = frappe.get_last_doc("Trade Log",filters={'ucc':self.ucc,'trade_date':self.trade_date,'trade_segment':self.segment})
		frappe.errprint(trade_log.segment)
		# if(self.segment == "NSE" or self.segment == "BSE" ):
		frappe.errprint("Equity")
		if(trade_log.segment == "Equity"):
			trade_log.qty += float(self.qty)
			# frappe.errprint("qty"+str(self.qty)+str(trade_log.qty))
			trade_log.save()

		# elif(self.segment == "NFO" or self.segment == "BFO" ):
		frappe.errprint("F&O")
		if(trade_log.segment == "F&O"):
			trade_log.qty += float(self.qty)
			trade_log.save()
			

		# elif(self.segment == "CDS" or self.segment == "BCD" ):
		frappe.errprint("Currency")
		if(trade_log.segment == "Currency"):
			trade_log.qty += float(self.qty)
			trade_log.save()

		# elif(self.segment == "MCX"):
		frappe.errprint("Commodity")
		if(trade_log.segment == "Commodity"):
			trade_log.qty += float(self.qty)
			trade_log.save()
		frappe.errprint("Success")
		# break

		# else:
		# 	frappe.errprint("else try")
		# 	# trade_log = frappe.new_doc("Trade Log")
			# trade_log.ucc = self.ucc
			# trade_log.trade_date = self.trade_date
			# trade_log.qty = self.qty
			# if(self.segment == "NSE" or self.segment == "BSE" ):
			#   trade_log.segment = "Equity"
			# elif(self.segment == "NFO" or self.segment == "BFO" ):
			#   trade_log.segment = "F&O"
			# elif(self.segment == "CDS" or self.segment == "BCD" ):
			#   trade_log.segment = "Currency"
			# elif(self.segment == "MCX"):
			#   trade_log.segment = "Commodity"
			# else:
			#   frappe.errprint("else except")
			# trade_log.insert()                

	# create trade log doctype based on when insert a new trade book
	except:
		frappe.errprint("except")
		trade_log = frappe.new_doc("Trade Log")
		trade_log.ucc = self.ucc
		trade_log.trade_date = self.trade_date
		trade_log.qty = self.qty
		trade_log.trade_segment = self.segment
		if(self.segment == "NSE" or self.segment == "BSE" ):
			trade_log.segment = "Equity"
		elif(self.segment == "NFO" or self.segment == "BFO" ):
			trade_log.segment = "F&O"
		elif(self.segment == "CDS" or self.segment == "BCD" ):
			trade_log.segment = "Currency"
		elif(self.segment == "MCX"):
			trade_log.segment = "Commodity"
		else:
			frappe.errprint("else except")
		trade_log.insert()
		frappe.errprint("Success")
		# break


@frappe.whitelist(allow_guest=True)
def create_support_code(self,event):    
	# for create support code in customer after insert
		
	cus_list = frappe.get_doc("Customer",self.name)   # for create support code in all customer
	code = frappe.generate_hash(length=4)
	cus_list.fsl_support_code = code
	cus_list.save()
	frappe.errprint("customer updated")
		

	# for i in cus_list:
# cus_list = frappe.get_doc("Customer",i.name)


