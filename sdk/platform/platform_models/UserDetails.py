"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class UserDetails(Schema):

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    

