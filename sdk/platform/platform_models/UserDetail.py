"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class UserDetail(BaseSchema):

    
    user_id = fields.Str(required=False)
    
    full_name = fields.Str(required=False)
    
    username = fields.Str(required=False)
    

