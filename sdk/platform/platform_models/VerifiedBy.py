"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class VerifiedBy(Schema):

    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    

