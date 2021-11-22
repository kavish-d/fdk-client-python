"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class SubscriptionLimitApplication(Schema):

    
    enabled = fields.Boolean(required=False)
    
    hard_limit = fields.Int(required=False)
    
    soft_limit = fields.Int(required=False)
    

