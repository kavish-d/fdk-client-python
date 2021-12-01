"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class ForgotPasswordRequestSchema(BaseSchema):

    
    code = fields.Str(required=False)
    
    password = fields.Str(required=False)
    

