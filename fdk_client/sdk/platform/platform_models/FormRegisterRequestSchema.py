"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema











from .FormRegisterRequestSchemaPhone import FormRegisterRequestSchemaPhone




class FormRegisterRequestSchema(BaseSchema):

    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    phone = fields.Nested(FormRegisterRequestSchemaPhone, required=False)
    
    register_token = fields.Str(required=False)
    
