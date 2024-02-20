import frappe

@frappe.whitelist(allow_guest=True)

def pp_rm_top_performer(from_date = None,to_date = None):
    try :
        if from_date is None:
                from_date = frappe.utils.today()
        if to_date is None:
                to_date = frappe.utils.add_days(frappe.utils.today(), 1)

        oppr_filters = [['modified', 'between', [from_date, to_date]],
                        ['status','in',['Open','In-Progress','Completed','Approved','Rejected','Active']],
                        ['fsl_referral_by','not in',['','online']]]

        rms = frappe.db.get_list('Opportunity',filters=oppr_filters,
                        fields=['count(name) as count', 'fsl_referral_by'],
                        group_by='fsl_referral_by',
                        order_by='count desc',
                        page_length=10,
                    )

        return {"status": "Ok", "rm_oppr_count": rms}
    except Exception as e:
        return {"status": "Not Ok", "Error": f"An error occurred while processing the request:{e}"}