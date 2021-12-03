"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class RefundAccountResponse(BaseSchema):

    
    is_verified_flag = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
