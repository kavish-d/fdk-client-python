"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class LoyaltyPointsConfig(Schema):

    
    enabled = fields.Boolean(required=False)
    
    auto_apply = fields.Boolean(required=False)
    

