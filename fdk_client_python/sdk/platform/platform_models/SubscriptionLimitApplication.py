"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class SubscriptionLimitApplication(BaseSchema):

    
    enabled = fields.Boolean(required=False)
    
    hard_limit = fields.Int(required=False)
    
    soft_limit = fields.Int(required=False)
    

