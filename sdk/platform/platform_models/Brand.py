"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Logo import Logo






class Brand(Schema):

    
    logo = fields.Nested(Logo, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

