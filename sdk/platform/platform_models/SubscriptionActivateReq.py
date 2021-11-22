"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *












class SubscriptionActivateReq(Schema):

    
    unique_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    product_suite = fields.Str(required=False)
    
    plan_id = fields.Str(required=False)
    
    payment_method = fields.Str(required=False)
    

