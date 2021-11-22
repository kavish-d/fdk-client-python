"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class WrongOtpError(Schema):

    
    success = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    is_verified_flag = fields.Boolean(required=False)
    

