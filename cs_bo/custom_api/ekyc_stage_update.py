import frappe
from frappe.utils import now_datetime
current_datetime = now_datetime()

@frappe.whitelist()
def put_stage_update(id, stage=None):
    try:
        oppor = frappe.get_doc("Opportunity", id)

        if oppor:
            if stage:
                oppor.fsl_stage = stage
                present = 0
                if stage == "13":
                        # frappe.errprint("stage")
                        # frappe.errprint(stage)
                        oppor.fsl_stage13_timing = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
                    
                if stage == 13:
                    # frappe.errprint("stage 13")
                    # frappe.errprint(stage)
                    oppor.fsl_stage13_timing = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
                for i in oppor.fsl_stage_table:
                    if stage == i.stages:
                        present = 1
                       
                if present == 0:
                    # frappe.errprint(stage)
                    
                    
                    oppor.append("fsl_stage_table", {
                    "stages": stage,
                    "timing": current_datetime.strftime('%Y-%m-%d %H:%M:%S')
                })

            oppor.save()

            frappe.local.response["message"] = {
                "success_key": 1,
                "message": "Opportunity stage Updated",
                "stage": oppor.fsl_stage
            }
    # except:
    #     frappe.local.response["message"] = {
    #         "success_key": 0,
    #         "message": "Opportunity Not Exists"
    #     }
    except Exception as e:
        frappe.local.response["message"] = {
            "error": f"An error occurred: {str(e)}"
        }