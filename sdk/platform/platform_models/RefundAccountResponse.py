"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class RefundAccountResponse(Schema):

    
    message = fields.Str(required=False)
    
    is_verified_flag = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    

