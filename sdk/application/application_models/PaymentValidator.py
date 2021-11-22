"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class PaymentValidator:
    
    class getAggregatorsConfig(Schema):
        
        x_api_token = fields.Str(required=False)
        
        refresh = fields.Boolean(required=False)
         
    
    class attachCardToCustomer(Schema):
        
        pass 
    
    class getActiveCardAggregator(Schema):
        
        refresh = fields.Boolean(required=False)
         
    
    class getActiveUserCards(Schema):
        
        force_refresh = fields.Boolean(required=False)
         
    
    class deleteUserCard(Schema):
        
        pass 
    
    class verifyCustomerForPayment(Schema):
        
        pass 
    
    class verifyAndChargePayment(Schema):
        
        pass 
    
    class initialisePayment(Schema):
        
        pass 
    
    class checkAndUpdatePaymentStatus(Schema):
        
        pass 
    
    class getPaymentModeRoutes(Schema):
        
        amount = fields.Int(required=False)
        
        cart_id = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        refresh = fields.Boolean(required=False)
        
        card_reference = fields.Str(required=False)
        
        user_details = fields.Str(required=False)
         
    
    class getPosPaymentModeRoutes(Schema):
        
        amount = fields.Int(required=False)
        
        cart_id = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        refresh = fields.Boolean(required=False)
        
        card_reference = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
        
        user_details = fields.Str(required=False)
         
    
    class getRupifiBannerDetails(Schema):
        
        pass 
    
    class getActiveRefundTransferModes(Schema):
        
        pass 
    
    class enableOrDisableRefundTransferMode(Schema):
        
        pass 
    
    class getUserBeneficiariesDetail(Schema):
        
        order_id = fields.Str(required=False)
         
    
    class verifyIfscCode(Schema):
        
        ifsc_code = fields.Str(required=False)
         
    
    class getOrderBeneficiariesDetail(Schema):
        
        order_id = fields.Str(required=False)
         
    
    class verifyOtpAndAddBeneficiaryForBank(Schema):
        
        pass 
    
    class addBeneficiaryDetails(Schema):
        
        pass 
    
    class addRefundBankAccountUsingOTP(Schema):
        
        pass 
    
    class verifyOtpAndAddBeneficiaryForWallet(Schema):
        
        pass 
    
    class updateDefaultBeneficiary(Schema):
        
        pass 
    