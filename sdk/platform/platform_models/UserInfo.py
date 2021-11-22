"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class UserInfo(Schema):

    
    username = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    

