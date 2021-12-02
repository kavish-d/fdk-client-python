"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema














class PaymentGatewayConfigResponse(BaseSchema):

    
    excluded_fields = fields.List(fields.Str(required=False), required=False)
    
    created = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    aggregators = fields.List(fields.Dict(required=False), required=False)
    
    display_fields = fields.List(fields.Str(required=False), required=False)
    

