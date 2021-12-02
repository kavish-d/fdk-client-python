"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema
















class SmsProviderReq(BaseSchema):

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    sender = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    authkey = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    

