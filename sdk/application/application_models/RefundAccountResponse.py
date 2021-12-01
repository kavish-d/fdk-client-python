"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class RefundAccountResponse(BaseSchema):

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    is_verified_flag = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    

