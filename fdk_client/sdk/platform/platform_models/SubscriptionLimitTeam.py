"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class SubscriptionLimitTeam(BaseSchema):
    # Billing swagger.json

    
    limit = fields.Int(required=False)
    

