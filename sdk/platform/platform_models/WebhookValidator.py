"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class WebhookValidator:
    
    class getSubscribersByCompany(Schema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        company_id = fields.Int(required=False)
        
        extension_id = fields.Str(required=False)
         
    
    class registerSubscriberToEvent(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class updateSubscriberConfig(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class getSubscribersByExtensionId(Schema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        company_id = fields.Int(required=False)
        
        extension_id = fields.Str(required=False)
         
    
    class getSubscriberById(Schema):
        
        company_id = fields.Int(required=False)
        
        subscriber_id = fields.Int(required=False)
         
    
    class fetchAllEventConfigurations(Schema):
        
        company_id = fields.Int(required=False)
         
    