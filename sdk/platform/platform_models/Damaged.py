"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class Damaged(Schema):

    
    updated_at = fields.Str(required=False)
    
    count = fields.Int(required=False)
    

