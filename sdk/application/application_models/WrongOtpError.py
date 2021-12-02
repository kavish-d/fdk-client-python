"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class WrongOtpError(BaseSchema):

    
    is_verified_flag = fields.Boolean(required=False)
    
    success = fields.Str(required=False)
    
    description = fields.Str(required=False)
    

