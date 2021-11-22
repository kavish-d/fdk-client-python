"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class PaymentValidator:
    
    class getBrandPaymentGatewayConfig(Schema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class saveBrandPaymentGatewayConfig(Schema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateBrandPaymentGatewayConfig(Schema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getPaymentModeRoutes(Schema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        refresh = fields.Boolean(required=False)
        
        request_type = fields.Str(required=False)
         
    
    class getAllPayouts(Schema):
        
        company_id = fields.Int(required=False)
        
        unique_external_id = fields.Str(required=False)
         
    
    class savePayout(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class updatePayout(Schema):
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
    
    class activateAndDectivatePayout(Schema):
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
    
    class deletePayout(Schema):
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
    
    class getSubscriptionPaymentMethod(Schema):
        
        company_id = fields.Int(required=False)
        
        unique_external_id = fields.Str(required=False)
         
    
    class deleteSubscriptionPaymentMethod(Schema):
        
        company_id = fields.Int(required=False)
        
        unique_external_id = fields.Str(required=False)
        
        payment_method_id = fields.Str(required=False)
         
    
    class getSubscriptionConfig(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class saveSubscriptionSetupIntent(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class addBeneficiaryDetails(Schema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class verifyIfscCode(Schema):
        
        company_id = fields.Int(required=False)
        
        ifsc_code = fields.Str(required=False)
         
    
    class getUserOrderBeneficiaries(Schema):
        
        order_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getUserBeneficiaries(Schema):
        
        order_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class confirmPayment(Schema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    