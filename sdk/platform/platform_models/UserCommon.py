"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class UserCommon(BaseSchema):

    
    company_id = fields.Int(required=False)
    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    

