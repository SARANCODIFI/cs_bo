
import unittest
import frappe
from cs_bo.custom_api.ekyc_stage1 import post_opportunity, create_opportunity  # Import your functions
 
# class TestOpportunityFunctions(unittest.TestCase):
@frappe.whitelist(allow_guest=True)
def test_post_opportunity_customer_exists():

    # Simulate the case where the customer already exists

    mob = [ '1111111110', '2222222220', '3333333333', '984272345', '6666666000', '9346744567', '9345150402', 
            '8015453500', '8825808189', '4444444444', '6666343666', '5555555555', '6666666666', '7777777777',  
           '7777777770', '8888888880', '9999999990', '9976944712', '9823190001', '7871972524', '7576666666',      
           '8220559200', '8100025874', '1111111112', '2222222211', '3333333311', '9706503596', '7400688990', '9585170707', '6666669096', '9433068849', '9380585566', '4444444400', '5555555500', '6666666600', '9939738006', '9346743345', '7871972524', '7871972524', '4567890123', '1111111111', '2222222222', '3333333333', '4444444444', '5555555555', '6666666666', '7777777777', '6777666666', '8888888888', '9999999999', '2222222200', '3333333300', '1111111110', '2222222220', '3333333333', '984272345', '6666666000', '9346744567', '9345150402', '8015453500', '8825808189', '4444444567', '5566343666', '9955555555', '8966666666', '2377777777', '7457777770', '8248888880', '2499999990', '2476944712', '4523190001', '5671972524', '6776666666', '8890559200', '8990025874', '1341111112', '1322222211', '3463333311', '4530650356', '5700688990', '9785170707', '6666669096', '943350849', '950085566', '504444400', '555055500', '506666600', '993975006', '934650345', '787150224', '787195054','456785013', '111111501', '222222502', '333335033', '444450444', '555055555', '666650666','777775077', '677750666', '885088888', '999509999', '222250200', '333333500']

    for num in mob:
        frappe.errprint(num)
        response = post_opportunity(

            mobile=num,

            smsverified="1",

            referral_by="Direct",

            otp="1234",

            fsl_mode_of_application="Online"

        )
        frappe.errprint("final")

        # self.assertEqual(response["success_key"], 1)

        # self.assertEqual(response["message"], "Customer Already Exists")

        # self.assertIn("stage", response["data"])

    def test_post_opportunity_opportunity_exists(self):

        # Simulate the case where the opportunity already exists

        response = post_opportunity(

            mobile="9876543210",

            smsverified="1",

            referral_by="Referral456",

            otp="5678",

            fsl_mode_of_application="Offline"

        )

        self.assertEqual(response["success_key"], 1)

        self.assertEqual(response["message"], "Opportunity Already Exists and Referral ID is Updated")

        self.assertIn("opportunity_id", response["data"])

        self.assertIn("stage", response["data"])

        self.assertIn("Referral Id", response["data"])
 
    def test_post_opportunity_create_opportunity(self):

        # Simulate the case where a new opportunity is created

        response = post_opportunity(

            mobile="1112223333",

            smsverified="1",

            referral_by="Referral789",

            otp="9876",

            fsl_mode_of_application="Online"

        )

        self.assertEqual(response["success_key"], 1)

        self.assertEqual(response["message"], "Opportunity Created")

        self.assertIn("opportunity", response["data"])

        self.assertIn("stage", response["data"])

        self.assertIn("fsl_mode_of_application", response["data"])
 
    def test_post_opportunity_missing_otp(self):

        # Simulate the case where OTP is missing

        response = post_opportunity(

            mobile="5556667777",

            smsverified="1",

            referral_by="Referral123",

            otp=None,  # OTP is missing

            fsl_mode_of_application="Offline"

        )

        self.assertEqual(response["success_key"], 0)

        self.assertEqual(response["message"], "OTP is Mandatory")
 
    def test_create_opportunity(self):

        # Simulate the creation of a new opportunity

        oppor = create_opportunity(

            mobile="8889990000",

            referral_by="Referral999",

            otp="1234",

            fsl_mode_of_application="Online"

        )

        self.assertTrue(oppor.name.startswith("OPP-"))  # Verify that the opportunity has a name
 
if __name__ == '__main__':

    unittest.main()
