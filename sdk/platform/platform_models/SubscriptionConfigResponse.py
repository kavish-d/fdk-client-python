"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class SubscriptionConfigResponse(BaseSchema):

    
    config = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    

