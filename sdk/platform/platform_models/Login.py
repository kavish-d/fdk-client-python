"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class Login(BaseSchema):

    
    password = fields.Boolean(required=False)
    
    otp = fields.Boolean(required=False)
    

