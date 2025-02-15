"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class SubscriptionLimitApplication(BaseSchema):
    # Billing swagger.json

    
    enabled = fields.Boolean(required=False)
    
    hard_limit = fields.Int(required=False)
    
    soft_limit = fields.Int(required=False)
    

