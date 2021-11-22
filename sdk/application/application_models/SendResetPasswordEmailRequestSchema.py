"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class SendResetPasswordEmailRequestSchema(Schema):

    
    email = fields.Str(required=False)
    
    captcha_code = fields.Str(required=False)
    

