"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class UpdatePasswordRequestSchema(Schema):

    
    old_password = fields.Str(required=False)
    
    new_password = fields.Str(required=False)
    

