"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ForgotPasswordRequestSchema(Schema):

    
    code = fields.Str(required=False)
    
    password = fields.Str(required=False)
    

