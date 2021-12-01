"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class SendResetPasswordEmailRequestSchema(BaseSchema):

    
    email = fields.Str(required=False)
    
    captcha_code = fields.Str(required=False)
    

