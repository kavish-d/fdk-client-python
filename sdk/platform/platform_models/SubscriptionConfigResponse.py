"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class SubscriptionConfigResponse(BaseSchema):

    
    aggregator = fields.Str(required=False)
    
    config = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    

