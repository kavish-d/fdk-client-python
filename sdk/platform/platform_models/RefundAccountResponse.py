"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class RefundAccountResponse(BaseSchema):

    
    success = fields.Boolean(required=False)
    
    is_verified_flag = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    

