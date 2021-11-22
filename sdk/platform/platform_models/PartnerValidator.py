"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class PartnerValidator:
    
    class addProxyPath(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
         
    
    class removeProxyPath(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        attached_path = fields.Str(required=False)
         
    