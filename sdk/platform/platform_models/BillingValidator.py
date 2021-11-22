"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class BillingValidator:
    
    class createSubscriptionCharge(Schema):
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
         
    
    class getSubscriptionCharge(Schema):
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        subscription_id = fields.Str(required=False)
         
    
    class cancelSubscriptionCharge(Schema):
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        subscription_id = fields.Str(required=False)
         
    
    class getInvoices(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getInvoiceById(Schema):
        
        company_id = fields.Str(required=False)
        
        invoice_id = fields.Str(required=False)
         
    
    class getCustomerDetail(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class upsertCustomerDetail(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getSubscription(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getFeatureLimitConfig(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class activateSubscriptionPlan(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class cancelSubscriptionPlan(Schema):
        
        company_id = fields.Str(required=False)
         
    