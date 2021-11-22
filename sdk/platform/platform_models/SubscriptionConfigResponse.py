"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class SubscriptionConfigResponse(Schema):

    
    aggregator = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    config = fields.Dict(required=False)
    

