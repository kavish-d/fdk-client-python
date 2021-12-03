"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema














class OAuthRequestSchemaProfile(BaseSchema):

    
    last_name = fields.Str(required=False)
    
    image = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    full_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
