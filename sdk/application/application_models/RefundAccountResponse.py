"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *










class RefundAccountResponse(Schema):

    
    success = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    
    is_verified_flag = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    

