"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Phone import Phone

from .SubscriptionBillingAddress import SubscriptionBillingAddress


















class SubscriptionCustomer(Schema):

    
    phone = fields.Nested(Phone, required=False)
    
    billing_address = fields.Nested(SubscriptionBillingAddress, required=False)
    
    _id = fields.Str(required=False)
    
    unique_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    

